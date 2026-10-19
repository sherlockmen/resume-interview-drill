<h1 align="center">Resume Interview Drill</h1>

<p align="center"><strong>一份材料，一句指令，生成分轮问答与本地网页。</strong></p>

<p align="center">
  <code>Agent Skill</code> · 技术岗位 / 产品经理 · <a href="LICENSE">MIT</a>
</p>

<p align="center">
  <a href="#quick-start">快速开始</a> ·
  <a href="#compatibility">支持平台</a> ·
  <a href="#features">核心能力</a> ·
  <a href="#tracks">岗位与预览</a> ·
  <a href="#privacy">隐私说明</a>
</p>

<a id="quick-start"></a>

## 快速开始

**1. 安装一次**

```sh
npx skills add sherlockmen/resume-interview-drill -g
```

需 Node.js/npm 与 Git，按提示选择平台。

**2. 附上简历，说一句**

```text
使用 resume-interview-drill，帮我准备面试。
```

可附岗位 JD，或指定“技术岗位”“产品经理”。完成后打开生成的本地网页；全部流程已内置，无需长提示词。

<a id="compatibility"></a>

## 支持平台

| 平台 | 安装器中选择 | 调用方式 |
| --- | --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `codex` | `$resume-interview-drill` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `claude-code` | `/resume-interview-drill` |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md) | `codex`（共享目录） | `/resume-interview-drill` |
| [OpenCode](https://opencode.ai/docs/skills/) | `opencode` | 上方自然语言请求 |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | `hermes-agent` | `/resume-interview-drill` |

同一份 [Agent Skills](https://agentskills.io/specification) 技能包。按官方规范适配，已验证安装资源与网页构建，尚未逐一实测所有客户端。

<details>
<summary><strong>运行要求与手动安装</strong></summary>

Agent 需能读取材料、写入本地文件和执行命令，环境需 Python 3.9+。PDF 解析、浏览器预览使用宿主工具；网页构建器仅依赖 Python 标准库。

[下载 ZIP](https://github.com/sherlockmen/resume-interview-drill/archive/refs/heads/master.zip)，将完整文件夹命名为 `resume-interview-drill`，放入对应用户目录：

| 平台 | 默认用户目录 |
| --- | --- |
| Codex / DeepSeek Harness | `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` |
| OpenCode | `~/.config/opencode/skills/` |
| Hermes Agent | `~/.hermes/skills/` |

保留 `SKILL.md`、`references/`、`scripts/`、`assets/` 的相对位置。DeepSeek Harness 也支持 `~/.dsh/skills/`；自定义目录以宿主配置为准。安装后未发现技能时，重新开启会话。

</details>

<a id="features"></a>

## 核心能力

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>01 · 逐点覆盖</h3>
      材料中的每个信息点都关联具体问答，低优先级信息也不遗漏。
    </td>
    <td width="50%" valign="top">
      <h3>02 · 追问有答案</h3>
      主问给出口述参考回答，每条追问都有答案，并说明考察目的。
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>03 · 事实有边界</h3>
      区分材料自述、待确认内容与假设方案，不编造经历或业绩。
    </td>
    <td width="50%" valign="top">
      <h3>04 · 网页可回查</h3>
      支持全文搜索、轮次筛选、答案折叠、逐点索引与待补清单。
    </td>
  </tr>
</table>

> **交付：** 分轮问答、覆盖表、待补信息、准备优先级、本地 HTML。
> 覆盖全部材料信息点；开放问题的变化无法穷尽。

<a id="tracks"></a>

## 岗位与预览

两条路径分别生成题库、覆盖表和网页。以下轮次为练习编排，可按岗位调整。

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>技术岗位</h3>
      <p><strong>实现 → 设计 → 判断</strong></p>
      <p>一面：还原实现，核对本人贡献。<br>
      二面：改变约束，比较方案与代价。<br>
      负责人轮：判断业务价值与交付优先级。</p>
      <a href="docs/images/overview.png"><img src="docs/images/overview.png" alt="技术路径网页：搜索、轮次筛选与问答总览" width="480"></a>
      <p><a href="docs/demo.html">演示文件</a> · <a href="references/technical-interviews.md">提问方法</a></p>
    </td>
    <td width="50%" valign="top">
      <h3>产品经理</h3>
      <p><strong>证据 → 取舍 → 价值</strong></p>
      <p>一面：复盘项目，追查需求证据。<br>
      二面：权衡优先级，验证指标与归因。<br>
      负责人轮：连接客户、投入产出与路线图。</p>
      <a href="docs/images/product-overview.png"><img src="docs/images/product-overview.png" alt="产品路径网页：经历复盘、产品分析与业务判断" width="480"></a>
      <p><a href="docs/product-demo.html">演示文件</a> · <a href="references/product-manager-interviews.md">提问方法与来源</a></p>
    </td>
  </tr>
</table>

<sub>所有效果图均来自虚构示例，未使用个人简历。下载仓库后，用浏览器打开演示 HTML。</sub>

### 答案与依据

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>主答与追问分层展开</strong><br><br>
      <a href="docs/images/answers.png"><img src="docs/images/answers.png" alt="完整主答、补充说明与带答案的连续追问" width="480"></a>
    </td>
    <td width="50%" valign="top">
      <strong>信息点与问题相互定位</strong><br><br>
      <a href="docs/images/coverage.png"><img src="docs/images/coverage.png" alt="来源引文、信息点与关联问答索引" width="480"></a>
    </td>
  </tr>
</table>

<details>
<summary><strong>窄屏效果</strong></summary>

<img src="docs/images/mobile.png" alt="窄屏下的导航、搜索与答案展开" width="340">

</details>

<a id="privacy"></a>

## 中性展示与隐私

- **中性展示：** 使用“技术笔记”“产品笔记”等名称，替换指定敏感词，隐藏身份信息。
- **快速收起：** 默认显示封面；按 Esc、切换窗口或标签时收起正文并清空搜索。
- **本地阅读：** 网页自包含，不自动加载外部资源，不保存阅读记录；默认不上传或公开部署个人材料。

中性展示不提供加密或访问控制；材料分析仍由所使用的 AI 工具处理。

<details>
<summary><strong>脱敏范围</strong></summary>

默认替换“简历、面试、求职、跳槽、招聘”，匹配常见邮箱与连续数字的中国大陆手机号。姓名、其他联系方式及身份链接由 Agent 识别并传入构建器。交付前检查正文、源码、标题与路径。

</details>

<details>
<summary><strong>文件与扩展</strong></summary>

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 完整流程、覆盖规则、答案要求与验收标准 |
| [references/](references/) | 技术、产品与 Agent 岗位的提问方法 |
| [scripts/build_notes.py](scripts/build_notes.py) | 题库校验、脱敏与网页构建 |
| [assets/notes.html](assets/notes.html) | 离线网页模板 |
| [docs/](docs/) | 虚构示例、演示页与截图 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 可选界面信息 |

题库结构、构建命令与脱敏参数见 [SKILL.md](SKILL.md#使用内置构建器)。

</details>

## 许可证

[MIT](LICENSE)。外部文章与指南保留各自权利。
