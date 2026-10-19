#!/usr/bin/env python3
"""Build a self-contained, neutral reading page from the complete private bank."""

import argparse
import json
import re
from pathlib import Path


AVOID = ("简历", "面试", "求职", "跳槽", "招聘")
REPLACEMENTS = (
    ("面试官", "评审者"), ("候选人", "参与者"),
    ("技术一面", "基础讨论"), ("技术二面", "进阶讨论"),
    ("负责人面", "综合讨论"), ("一面", "基础讨论"), ("二面", "进阶讨论"),
    ("简历", "材料"), ("面试", "技术讨论"), ("求职", "职业规划"),
    ("跳槽", "方向调整"), ("招聘", "团队建设"),
)
EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
MOBILE = re.compile(r"(?<!\d)(?:\+?86[ -]?)?1[3-9]\d{9}(?!\d)")
FIELDS = {
    "facts": ("id", "alias", "page", "section", "point", "source_quote", "kind"),
    "questions": ("id", "round", "priority", "basis", "fact_ids", "question", "aim",
                  "answer_type", "answer", "details", "followups", "gaps", "source_urls"),
    "sources": ("title", "url", "note"),
}


def validate(bank):
    facts, questions = bank["facts"], bank["questions"]
    fact_ids = {f["id"] for f in facts}
    assert len(fact_ids) == len(facts), "Duplicate point IDs"
    assert len({q["id"] for q in questions}) == len(questions), "Duplicate entry IDs"
    covered = set()
    followups = 0
    for q in questions:
        assert q["round"] in (1, 2, 3), "Unknown reading level"
        assert q["question"].strip() and q["answer"].strip(), "Missing entry text"
        assert q["fact_ids"] and set(q["fact_ids"]) <= fact_ids, "Invalid point mapping"
        covered.update(q["fact_ids"])
        for f in q["followups"]:
            assert f["question"].strip() and f["answer"].strip(), "Missing extension answer"
        followups += len(q["followups"])
    assert covered == fact_ids, "Unmapped points"
    return {
        "main_questions": len(questions), "followups": followups,
        "total_answers": len(questions) + followups, "atomic_points": len(facts),
        "covered_points": len(covered), "missing_points": [],
        "round_counts": {str(n): sum(q["round"] == n for q in questions) for n in (1, 2, 3)},
        "priority_counts": {p: sum(q["priority"] == p for q in questions)
                            for p in sorted({q["priority"] for q in questions})},
    }


def sanitize(value, identities):
    if isinstance(value, str):
        for identity in sorted(identities, key=len, reverse=True):
            value = re.sub(re.escape(identity), "［已省略］", value, flags=re.IGNORECASE)
        value = EMAIL.sub("［联系信息已省略］", value)
        value = MOBILE.sub("［联系信息已省略］", value)
        for before, after in REPLACEMENTS:
            value = value.replace(before, after)
        return value
    if isinstance(value, list):
        return [sanitize(v, identities) for v in value]
    if isinstance(value, dict):
        return {k: sanitize(v, identities) for k, v in value.items()}
    return value


def display_bank(bank, identities):
    stats = validate(bank)
    safe = {key: [{k: item[k] for k in fields if k in item} for item in bank[key]]
            for key, fields in FIELDS.items()}
    safe.update(version=bank.get("version", ""), stats=stats)
    safe = sanitize(safe, identities)
    assert validate(safe) == stats, "Display conversion changed coverage"
    assert [f["id"] for f in safe["facts"]] == [f["id"] for f in bank["facts"]], "Point IDs changed"
    assert [(q["id"], q["round"], q["fact_ids"], len(q["followups"])) for q in safe["questions"]] == [
        (q["id"], q["round"], q["fact_ids"], len(q["followups"])) for q in bank["questions"]
    ], "Entry IDs or point mappings changed"
    for item in safe["sources"]:
        assert item["url"].startswith("https://"), "Only HTTPS references are allowed"
    for q in safe["questions"]:
        assert all(u.startswith("https://") for u in q.get("source_urls", [])), "Invalid reference"
    return safe


def build(bank, template, identities):
    safe = display_bank(bank, identities)
    assert template.count("__DATA_JSON__") == 1, "Template needs exactly one data slot"
    payload = json.dumps(safe, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    result = template.replace("__DATA_JSON__", payload)
    assert all(word not in result for word in AVOID), "A restricted term remains"
    assert not EMAIL.search(result) and not MOBILE.search(result), "Contact data remains"
    assert all(identity.lower() not in result.lower() for identity in identities), "Identity remains"
    assert "/Users/" not in result and "source_pdf" not in result, "Private source path remains"
    return result, safe["stats"]


def self_check():
    example = {"version": "test", "facts": [{"id": "F1", "point": "简历：示例姓名"}],
               "questions": [{"id": "Q1", "round": 1, "priority": "P0", "fact_ids": ["F1"],
                              "question": "面试联系 test@example.com 13812345678", "answer": "</script>",
                              "followups": [{"question": "追问", "answer": "招聘示例姓名"}]}],
               "sources": [], "source_pdf": "/Users/private/hidden.pdf"}
    html, stats = build(example, '<script type="application/json">__DATA_JSON__</script>', ["示例姓名"])
    assert stats["total_answers"] == 2 and stats["covered_points"] == 1
    assert html.count("</script>") == 1 and "\\u003c/script\\u003e" in html
    broken = json.loads(json.dumps(example))
    broken["questions"][0]["followups"][0]["answer"] = ""
    try:
        validate(broken)
    except AssertionError:
        pass
    else:
        raise AssertionError("Incomplete answer was accepted")
    print("Self-check passed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, nargs="?")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--redact", action="append", default=[], help="Exact name or identity link to remove; repeatable")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.input or not args.output:
        parser.error("input and --output are required")
    if any(not v.strip() for v in args.redact):
        parser.error("--redact cannot be empty")
    template = Path(__file__).resolve().parents[1] / "assets" / "notes.html"
    result, stats = build(json.loads(args.input.read_text()), template.read_text(), args.redact)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")
    print(json.dumps({"output": str(args.output), "stats": stats}, ensure_ascii=False))


if __name__ == "__main__":
    main()
