<h1 align="center">Resume Interview Drill</h1>

<p align="center"><strong>从一份简历，到逐点可查的分轮问答。</strong></p>

<p align="center">
  按技术岗位或产品经理独立组织分轮问题、连续追问和有依据的参考答案，<br>
  交付可搜索、可折叠、可离线阅读的网页。
</p>

<p align="center">
  <code>Codex Skill</code> · <code>逐点覆盖</code> · <code>追问有答案</code> · <code>中性展示</code> · <a href="LICENSE">MIT</a>
</p>

<p align="center">
  <a href="#features">核心能力</a> ·
  <a href="#quick-start">快速开始</a> ·
  <a href="#tracks">岗位路径</a> ·
  <a href="#preview">更多效果</a> ·
  <a href="#privacy">隐私说明</a>
</p>

<p align="center">
  <a href="docs/images/overview.png"><img src="docs/images/overview.png" alt="本地网页总览：全文搜索、轮次筛选和可折叠的问答" width="960"></a>
  <br><sub>使用完全虚构的练习项目，由内置构建器生成网页并实际截图；不包含真实个人材料。</sub>
</p>

<p align="center">
  <a href="docs/demo.html">技术演示</a> · <a href="docs/product-demo.html">产品演示</a><br>
  <sub>下载仓库后，用浏览器打开对应 HTML 即可体验；两套演示分别生成。</sub>
</p>

<a id="features"></a>

## 核心能力

面向技术岗位与产品经理，把经历、技能与成果展开为可练习、可回查的问答。每次先选定岗位路径，题库与网页分别交付。

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>01 · 每个信息点都涉及</h3>
      背景、教育、任职、项目、技能与成果逐项编号，关联具体问题和答案。优先级只影响准备顺序与展开深度。
    </td>
    <td width="50%" valign="top">
      <h3>02 · 主问、追问都有答案</h3>
      每道主问先给约 30—90 秒的口述回答，再按需补充实现或分析细节。每条列出的追问都提供参考答案。
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>03 · 讲清为什么这样问</h3>
      区分一面、二面与负责人轮的验证目标，说明每题考察什么、需要哪些证据，以及如何继续追问。
    </td>
    <td width="50%" valign="top">
      <h3>04 · 保留事实与未知的边界</h3>
      区分材料自述、用户确认、原理解释与假设方案。未知经历和数据标记待补，个人贡献与团队成果分别表述。
    </td>
  </tr>
</table>

**一次交付：** 分轮题库与答案、逐点覆盖表、待补信息、准备优先级，以及本地网页入口。

AI 按 Skill 指引分析材料、生成问答；Python 构建器负责校验题库、脱敏与生成网页。“全量覆盖”指当前材料中的全部信息点，开放问题的变化无法穷尽。

<a id="quick-start"></a>

## 快速开始

需要支持本地 Skills 的 **Codex**、**Python 3.9+** 和现代浏览器。Codex 需能读取材料、写入文件并运行命令；PDF 读取依赖宿主工具。网页构建器仅使用 Python 标准库。

### 1. 安装

下载仓库并解压，在包含 `SKILL.md` 的目录打开终端。以下命令适用于 macOS／Linux，安装位置遵循 Codex 的[本地 Skill 目录说明](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)：

```sh
mkdir -p "$HOME/.agents/skills/resume-interview-drill"
cp -R SKILL.md LICENSE agents assets references scripts "$HOME/.agents/skills/resume-interview-drill/"
python3 "$HOME/.agents/skills/resume-interview-drill/scripts/build_notes.py" --self-check
```

看到 `Self-check passed` 即表示构建器自检通过。已有同名 Skill 时先备份，复制会更新同名文件；若 Codex 尚未显示，重启后查看。

### 2. 提供材料，发送指令

在 Codex 中提供简历文件，按需附上目标岗位 JD，然后选择一条指令。

**技术岗位**

```text
$resume-interview-drill
根据我提供的简历，生成技术一面、技术二面和负责人轮的问题与参考答案。
覆盖每个信息点，为所有列出的追问写出答案，并说明考察目的。
未知经历与数据标记待补，假设方案单独标明。
最后生成本地网页，附逐点覆盖表、待补信息和准备优先级。
```

**产品经理**

```text
$resume-interview-drill
根据我提供的简历，使用产品经理路径，独立生成一面、二面和产品负责人轮的问答。
覆盖每个信息点，所有追问都给答案，说明每一问想确认什么。
重点追需求证据、方案取舍、个人贡献、跨团队推进、指标口径和效果归因。
未知经历标记待补，假设场景单独标明，最后生成独立的产品路径本地网页。
```

Skill 的显示名称为“研习资料”，调用名称为 `$resume-interview-drill`。没有 JD 时，说明根据材料暂定的方向与资深程度后继续；AI 产品经理使用产品路径。若同时需要两类岗位，会交付两个独立题库、覆盖表与网页。

### 3. 打开网页，逐项练习

从交付链接打开本地 HTML：搜索主题、筛选轮次、展开答案，或从覆盖表跳转到对应问题。先练准备优先级较高的内容，再补齐待确认信息。

展示入口使用 `outputs/reference-notes/` 下的中性目录与文件名：技术内容进入 `engineering/`，产品内容进入 `product/`。网页支持窄屏阅读，下载后无需启动服务。

<a id="tracks"></a>

## 两条独立的岗位路径

共用覆盖、答案与事实规则；各自使用轮次、提问逻辑、题库和网页。以下是练习编排，可按岗位调整，不代表任何公司的固定流程或官方题库。

### 技术岗位 · 实现 → 设计 → 判断

| 轮次 | 提问如何递进 | 回答需要体现什么 |
| --- | --- | --- |
| **技术一面** | 一次真实请求 → 数据与状态 → 设计原因 → 具体故障 → 效果验证 → 本人贡献 | 还原实现过程，讲清个人决策，提供可核对的细节。 |
| **技术二面** | 目标与约束 → 最小方案 → 逐次增加失败、规模、权限或成本条件 → 比较方案 → 验证 | 说明系统边界、异常恢复、方案代价与验收方法。 |
| **负责人／CTO 轮** | 选择动机 → 行动与结果 → 关键判断 → 新业务验证 → 交付计划 | 用实际行动支持观点，明确优先级、业务指标与责任。 |

涉及 Agent、RAG、LLM 或模型部署时，按经历补充执行链路、状态管理、工具调用、失败恢复与评估。详见[技术路径](references/technical-interviews.md)。

### 产品经理 · 证据 → 取舍 → 价值

| 轮次 | 提问如何递进 | 回答需要体现什么 |
| --- | --- | --- |
| **产品一面** | 具体项目 → 用户与问题 → 需求证据 → 方案形成 → 本人动作 → 结果复盘 | 还原实际工作，区分个人与团队贡献，说明证据的来源和限制。 |
| **产品二面** | 目标与约束 → 备选方案 → 优先级 → 改变一个条件 → 验证与停止条件 | 说明机会成本、指标口径、反证和效果归因，区分相关与因果。 |
| **产品负责人轮** | 过去实例 → 客户与付费方 → 竞争与替代 → 投入产出 → 路线图 → 协同决策 | 把用户问题联系到业务结果，说明资源分配、阶段验收及责任边界。 |

按岗位追加 **C 端／增长、B 端／平台、AI 产品、资深／负责人** 侧重点；产品经理不默认套用技术系统设计题。

方法综合了牛客、人人都是产品经理的公开经验分享，并以 Amazon、Atlassian 官方指南校验。来源、日期、适用边界与完整追问规则见[产品经理路径](references/product-manager-interviews.md#来源与适用边界)；经验样本不代表必问题目。

<a id="preview"></a>

## 更多效果

### 产品路径

<p>
  <a href="docs/images/product-overview.png"><img src="docs/images/product-overview.png" alt="产品笔记：独立的经历复盘、产品分析、业务判断层次，以及带答案的产品取舍问题" width="960"></a><br>
  <sub>「栖页」协作知识产品为完全虚构的演示设定；未使用真实个人经历或业务数据。</sub>
</p>

[示例数据](docs/product-demo-bank.json) · [演示页文件](docs/product-demo.html)

### 技术路径

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>答案分层，追问有回应</strong><br>
      <sub>主答、技术说明和追问答案分层展开，保留内容类型标签。</sub><br><br>
      <a href="docs/images/answers.png"><img src="docs/images/answers.png" alt="答案详情：完整主答、技术说明及两条带答案的追问" width="480"></a>
    </td>
    <td width="50%" valign="top">
      <strong>逐点索引，依据可回查</strong><br>
      <sub>从信息点定位相关答案，也可从问题回查来源依据。</sub><br><br>
      <a href="docs/images/coverage.png"><img src="docs/images/coverage.png" alt="逐点索引：来源引文、信息点与关联问题" width="480"></a>
    </td>
  </tr>
</table>

<details>
<summary><strong>查看窄屏阅读效果</strong></summary>

窄屏下调整导航与筛选布局，保留搜索、答案展开和内容收起操作。

<img src="docs/images/mobile.png" alt="窄屏效果：导航、筛选与展开的参考答案" width="340">

</details>

技术示例包含“共享器材预约练习”和“文档问答练习”两个虚构项目。产品示例为「栖页」虚构练习。**每套分别包含 5 个信息点、6 道主问题、12 条带答案的追问**，不限制实际生成规模。

<details>
<summary>从示例数据重新生成演示页</summary>

在包含 `SKILL.md` 的目录运行：

```sh
python3 scripts/build_notes.py docs/demo-bank.json --output docs/demo.html
python3 scripts/build_notes.py docs/product-demo-bank.json --output docs/product-demo.html
```

</details>

## 更多用法

<details>
<summary><strong>结合岗位 JD，调整深挖方向</strong></summary>

```text
$resume-interview-drill
结合我提供的简历和 Agent 工程师岗位 JD，组织分轮问题与参考答案。
重点深挖 Agent 执行、状态管理、工具调用、失败恢复和评估。
保留全部信息点的覆盖；缺失经历标记待补，设计题明确写成假设方案。
最后生成本地网页。
```

</details>

<details>
<summary><strong>更新材料，修订已有题库</strong></summary>

提供更新后的材料与已有题库，再发送：

```text
$resume-interview-drill
对比更新后的简历与已有题库，修订受影响的问题、答案和覆盖关系。
重新生成适合办公阅读的本地网页，使用中性标题和导航。
网页中不要出现“简历、面试、求职、跳槽、招聘”，并清理姓名、联系方式和身份链接。
```

</details>

<a id="privacy"></a>

## 中性展示与隐私

- **中性名称：** 技术页使用“技术笔记”“基础／进阶／综合”；产品页使用“产品笔记”“经历复盘／产品分析／业务判断”。正文打开前先显示封面。
- **快速收起：** 按钮、Esc、窗口失焦或切换标签均可收起正文并清空搜索；恢复焦点不会自动展开。
- **离线阅读：** HTML 自带样式、脚本和展示数据，不自动加载外部资源，不持久保存阅读记录；参考链接仅在主动点击时打开。
- **本地交付：** 默认不上传或公开部署个人材料；发布仓库时，仅保留虚构示例，排除私人材料、题库、网页和运行缓存。

<details>
<summary><strong>查看脱敏范围与使用边界</strong></summary>

构建器默认替换“简历、面试、求职、跳槽、招聘”，按内置规则匹配常见邮箱和连续数字的中国大陆手机号。姓名、其他联系方式与身份链接由代理识别，再通过 `--redact` 传入并检查。中性展示降低屏幕暴露，不提供加密或访问控制；材料分析仍由所使用的 AI 工具处理。

参考答案保留材料自述与用户确认的边界，不将业绩自述视为独立核实。未知经历使用待补标记，假设方案不能作为个人真实经历。构建校验检查映射与非空回答；事实准确性和回答是否充分仍需核对。

</details>

## 文件说明

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 工作流程、全量覆盖规则、答案要求与验收标准。 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 显示名称、简介与默认提示。 |
| [references/technical-interviews.md](references/technical-interviews.md) | 技术岗位的轮次矩阵与逐轮追问方法。 |
| [references/product-manager-interviews.md](references/product-manager-interviews.md) | 产品经理的轮次、题型、岗位分支及公开来源。 |
| [references/agent-lenses.md](references/agent-lenses.md) | Agent 相关岗位的补充考察维度。 |
| [scripts/build_notes.py](scripts/build_notes.py) | 校验已生成的 JSON 题库、脱敏并构建网页。 |
| [assets/notes.html](assets/notes.html) | 自包含网页模板与交互。 |
| [docs/](docs/) | 虚构示例数据、演示页与效果图。 |
| [LICENSE](LICENSE) | MIT 开源许可证。 |

分享时保留这些文件的相对位置。题库结构、构建命令与 `--redact` 用法见 [SKILL.md](SKILL.md#使用内置构建器)。

## 许可证

本项目采用 [MIT License](LICENSE)。引用的外部文章与指南保留各自权利；仓库仅链接来源并归纳方法。

---

<sub>文档编排参考：<a href="https://github.com/langgenius/dify">Dify</a> 的首屏与导航、<a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill">UI UX Pro Max</a> 的效果图展示、<a href="https://github.com/vercel-labs/agent-skills">Vercel Agent Skills</a> 的任务说明，以及 <a href="https://github.com/obra/superpowers">Superpowers</a> 的流程组织。</sub>
