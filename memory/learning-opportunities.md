# 技能学习机会追踪

> 自动扫描 ClawHub/GitHub 发现的潜在有价值技能
> 最后更新: 2026-03-10 08:01

---

## 🔥 高价值技能（建议优先关注）

### 1. AI Meeting Notes ⭐⭐⭐⭐⭐
- **技能名**: ai-meeting-notes
- **评分**: 3.573
- **描述**: 杂乱笔记→清晰行动项。粘贴会议记录、转录或文本，获取摘要、带负责人和截止日期的行动项。自动保存、可搜索、集成待办追踪
- **价值**: ⭐⭐⭐⭐⭐ 会议自动化处理，与 ai-daily-briefing 互补
- **状态**: 未安装
- **建议**: 无需机器人、订阅或设置，即用型会议助手
- **安装**: `clawhub install ai-meeting-notes`
- **版本**: 1.0.3 | 更新: 2026-02-25

### 2. AI Notes of Video ⭐⭐⭐⭐⭐
- **技能名**: ai-notes-of-video
- **评分**: 3.506
- **描述**: 通过视频URL生成文档、大纲和图文AI笔记，使用百度视频分析和笔记提取API
- **价值**: ⭐⭐⭐⭐⭐ 与现有 video-frames 形成完整视频处理矩阵
- **状态**: 未安装
- **建议**: 适合学习、会议记录、内容分析场景
- **安装**: `clawhub install ai-notes-of-video`
- **版本**: 1.0.0 | 更新: 2026-02-26

### 3. Filesystem MCP ⭐⭐⭐⭐⭐
- **技能名**: filesystem-mcp
- **评分**: 3.509
- **描述**: 安全、沙盒化的文件系统访问，支持列出、读取、写入、创建、移动、删除、搜索文件和目录
- **价值**: ⭐⭐⭐⭐⭐ 与现有 mcp-lark 形成 MCP 协议矩阵
- **状态**: 未安装（已有 mcp-lark 1.0.0）
- **建议**: 增强文件操作能力，标准化文件系统访问
- **安装**: `clawhub install filesystem-mcp`
- **版本**: 1.0.0 | 更新: 2026-02-25

### 4. Codex CLI Task ⭐⭐⭐⭐⭐
- **技能名**: codex-cli-task
- **评分**: 3.095 (新发布，评分待稳定)
- **描述**: 在后台异步启动 OpenAI Codex CLI，自动推送到 Telegram/WhatsApp。用于编码、重构、代码库研究、文件生成
- **价值**: ⭐⭐⭐⭐⭐ 最新发布，Codex 工作流增强
- **状态**: 未安装
- **建议**: 与 codex-orchestrator 形成完整 Codex 生态
- **安装**: `clawhub install codex-cli-task`
- **版本**: 1.1.2 | 发布: 2026-03-09

### 5. Codex Orchestrator ⭐⭐⭐⭐
- **技能名**: codex-orchestrator
- **评分**: 3.542
- **描述**: 监控、控制和编排后台 Codex 会话。跟踪进度、处理中断、确保长时间编码任务完成
- **价值**: ⭐⭐⭐⭐ 与现有 coding-agent 形成互补
- **状态**: 未安装（已有 coding-agent 在 /opt/openclaw/skills/）
- **建议**: 适合复杂多代理编码任务协调
- **安装**: `clawhub install codex-orchestrator`
- **版本**: 1.0.0 | 更新: 2026-02-28

### 6. Video Subtitles ⭐⭐⭐⭐
- **技能名**: video-subtitles
- **评分**: 3.489
- **描述**: 从视频/音频生成SRT字幕，支持翻译。转录希伯来语(ivrit.ai)和英语(whisper)，多语言翻译，烧录字幕到视频
- **价值**: ⭐⭐⭐⭐ 与现有 video-frames 形成视频处理矩阵
- **状态**: 未安装（video-frames 在 /opt/openclaw/skills/）
- **建议**: 适合多媒体内容创作、社交媒体字幕
- **安装**: `clawhub install video-subtitles`
- **版本**: 1.0.0 | 更新: 2026-03-09

### 7. Fast Browser Use ⭐⭐⭐⭐
- **技能名**: fast-browser-use
- **评分**: 3.623
- **描述**: 高性能浏览器自动化，适用于重度爬取、多标签管理和精确DOM提取。支持高级状态管理（cookies/local storage）
- **价值**: ⭐⭐⭐⭐ 可作为 agent-browser 的性能优化候选
- **状态**: 未安装（已有 agent-browser 0.2.0）
- **建议**: 评估性能差异后决定是否升级替换
- **安装**: `clawhub install fast-browser-use`
- **版本**: 1.0.5 | 更新: 2026-03-09

### 8. Agent Scorecard ⭐⭐⭐⭐
- **技能名**: agent-scorecard
- **评分**: 3.199
- **描述**: AI 代理输出的可配置质量评估。定义标准、运行评估、跟踪质量。无需 LLM-as-judge，基于模式
- **价值**: ⭐⭐⭐⭐ 代理质量监控和评估
- **状态**: 未安装
- **建议**: 适合生产环境代理质量保障
- **安装**: `clawhub install agent-scorecard`
- **版本**: 1.0.3 | 更新: 2026-03-09

### 9. ASR Skill (语音转文字) ⭐⭐⭐⭐
- **技能名**: asr-skill
- **评分**: 2.777 (新技能，评分待稳定)
- **描述**: 基于 Qwen3-ASR-0.6B 的语音转文字，支持22种中文方言和多语言识别，可用方言与 OpenClaw 交流
- **价值**: ⭐⭐⭐⭐ 中文方言支持，语音交互增强
- **状态**: 未安装
- **建议**: 适合中文用户语音交互场景
- **安装**: `clawhub install asr-skill`
- **版本**: 1.2.0 | 更新: 2026-03-09

### 10. MemoryAI ⭐⭐⭐⭐
- **技能名**: memoryai
- **评分**: 3.221
- **描述**: AI 代理的持久长期记忆。存储、回忆、推理，零上下文丢失无缝切换会话
- **价值**: ⭐⭐⭐⭐ 与现有 agent-brain、elite-longterm-memory 形成互补
- **状态**: 未安装
- **建议**: 评估与现有记忆技能的差异
- **安装**: `clawhub install memoryai`
- **版本**: 0.5.2 | 更新: 2026-03-09

### 11. Xiaohongshu MCP ⭐⭐⭐
- **技能名**: xiaohongshu-mcp
- **评分**: 3.615
- **描述**: 小红书自动化内容运营：发布图文视频、搜索笔记趋势、分析帖子评论、管理用户资料
- **价值**: ⭐⭐⭐ 社交媒体自动化
- **状态**: 未安装
- **建议**: 适合小红书内容创作者
- **安装**: `clawhub install xiaohongshu-mcp`
- **版本**: 1.0.0 | 更新: 2026-03-09

### 12. OpenClaw Shield UPX ⭐⭐⭐
- **技能名**: openclaw-shield-upx
- **评分**: 3.320
- **描述**: OpenClaw 的SIEM安全监控和威胁检测
- **价值**: ⭐⭐⭐ 安全增强
- **状态**: 未安装（已有 arc-security-audit）
- **建议**: 评估与现有安全技能的差异
- **安装**: `clawhub install openclaw-shield-upx`
- **版本**: 1.2.5 | 更新: 2026-03-09

### 13. Telegram Bot ⭐⭐⭐
- **技能名**: telegram-bot
- **评分**: 3.528
- **描述**: 通过 Telegram Bot API 构建和管理 Telegram 机器人。创建机器人、发送消息、处理 webhook、管理群组和频道
- **价值**: ⭐⭐⭐ 作为 Feishu 的备选消息平台
- **状态**: 未安装
- **建议**: 适合国际化场景
- **安装**: `clawhub install telegram-bot`
- **版本**: 1.0.0 | 更新: 2026-02-27

### 14. HeyGen Avatar Lite ⭐⭐⭐
- **技能名**: heygen-avatar-lite
- **评分**: 3.490
- **描述**: 使用 HeyGen API 创建AI数字人视频，免费入门指南
- **价值**: ⭐⭐⭐ 补充现有 ai-avatar-generation 的静态头像能力
- **状态**: 未安装（已有 ai-avatar-generation）
- **建议**: 适合视频内容创作
- **安装**: `clawhub install heygen-avatar-lite`
- **版本**: 1.1.1 | 更新: 2026-03-07

---

## 🆕 最新发现技能（explore 扫描）

### 15. 抖音创作者 ⭐⭐⭐
- **技能名**: douyin-creator
- **版本**: 1.3.0 | 更新: 13分钟前
- **描述**: 抖音内容创作与运营助手。抖音运营、涨粉、短视频创作、标题标签、SEO、账号运营

### 16. Tushare 股票技能 ⭐⭐⭐
- **技能名**: tushare-stock-skill
- **版本**: 1.3.0 | 更新: 23分钟前
- **描述**: 面向中国A股的 Tushare 专用技能，提供股票数据获取、个股分析与交易观察能力

### 17. Excalidraw 图表生成 ⭐⭐⭐
- **技能名**: excalidraw-diagram
- **版本**: 1.3.1 | 更新: 9分钟前
- **描述**: 从文本内容生成 Excalidraw 图表。手绘风格图表生成

### 18. Mermaid 可视化 ⭐⭐⭐
- **技能名**: mermaid-visualizer
- **版本**: 1.0.1 | 更新: 10分钟前
- **描述**: 将文本内容转换为专业 Mermaid 图表

### 19. Obsidian Canvas 创建 ⭐⭐⭐
- **技能名**: obsidian-canvas-creator
- **版本**: 1.0.1 | 更新: 10分钟前
- **描述**: 从文本内容创建 Obsidian Canvas 文件

### 20. 智能配图与 PPT 信息图 ⭐⭐⭐
- **技能名**: smart-illustrator
- **版本**: 1.0.0 | 更新: 12分钟前
- **描述**: 智能配图与 PPT 信息图生成器。支持文章配图、信息图生成

### 21. 视频脚本生成器 ⭐⭐⭐
- **技能名**: video-script-creator
- **版本**: 1.3.0 | 更新: 23分钟前
- **描述**: 短视频脚本生成器、视频脚本、抖音文案

### 22. PPT 大纲生成 ⭐⭐⭐
- **技能名**: ppt-outline
- **版本**: 1.4.0 | 更新: 23分钟前
- **描述**: PPT大纲和HTML演示文稿生成器

### 23. 微信公众号写作 ⭐⭐⭐
- **技能名**: wechat-mp-writer
- **版本**: 1.3.0 | 更新: 3分钟前
- **描述**: 微信公众号文章生成器

### 24. HTML Coder ⭐⭐⭐
- **技能名**: html-coder
- **版本**: 2.0.1 | 更新: 23分钟前
- **描述**: 专业的HTML开发技能，用于构建网页

### 25. Page CRO ⭐⭐⭐
- **技能名**: page-cro
- **版本**: 2.1.1 | 更新: 23分钟前
- **描述**: 页面优化、改进和转化率提升

---

## 📦 已安装技能清单

当前工作区已安装 **54** 个本地技能 + **52** 个系统级技能

### 本地工作区技能 (~/.openclaw/workspace/skills/)
```
2nd-brain, academic-research, actionbook, active-maintenance, adaptlypost,
aegis-shield, agentapi, agent-brain, agent-browser (0.2.0), agent-commons,
agentic-devops, agent-spawner, agent-task-manager, agent-team-orchestration,
agent-weave, ai-avatar-generation, ai-daily-briefing, ai-news-oracle,
airadar, airc, ak-rss-24h-brief, apple-media, apple-notes,
app-store-screenshot-generation, arc-security-audit, a-share-real-time-data,
azure-devops, bat-cat, bear-notes, better-notion, blogwatcher, claw-roam,
data-analyst, department-manager, docstrange, elite-longterm-memory,
find-skills (0.1.0), fzf-fuzzy-finder, github, icloud-findmy, mac-tts,
mcp-lark (1.0.0), obsidian, openclaw-tavily-search (0.1.0), personas,
proactive-agent (3.1.0), reminder (0.1.1), restart-continuity,
searxng (1.0.3), self-improving-agent (1.0.11), session-wrap-up,
skill-vetter (1.0.0), weather-data-fetcher, wechat-article-publisher
```

### 系统级技能 (/opt/openclaw/skills/)
```
1password, apple-notes, apple-reminders, bear-notes, blogwatcher, blucli,
bluebubbles, camsnap, canvas, clawhub, coding-agent, discord, eightctl,
gemini, gh-issues, gifgrep, github, gog, goplaces, healthcheck, himalaya,
imsg, mcporter, model-usage, nano-banana-pro, nano-pdf, notion, obsidian,
openai-image-gen, openai-whisper, openai-whisper-api, openhue, oracle,
ordercli, peekaboo, sag, session-logs, sherpa-onnx-tts, skill-creator,
slack, songsee, sonoscli, spotify-player, summarize, things-mac, tmux,
trello, video-frames, voice-call, wacli, weather, xurl
```

### ClawHub 锁定技能 (clawhub list)
```
agent-browser (0.2.0), find-skills (0.1.0), github (1.0.0), mcp-lark (1.0.0),
obsidian (1.0.0), openclaw-tavily-search (0.1.0), proactive-agent (3.1.0),
reminder (0.1.1), searxng (1.0.3), self-improving-agent (1.0.11),
skill-vetter (1.0.0), youtube-transcript (1.0.1)
```

---

## 🔍 ClawHub 热门技能群扫描结果

### Browser 自动化类 (10个)
| 技能 | 评分 | 描述 |
|------|------|------|
| agent-browser | 3.800 | 最高评分浏览器技能 |
| browser-automation | 3.716 | 成熟自动化方案 |
| browser-use | 3.668 | 浏览器使用 |
| fast-browser-use | 3.623 | 快速浏览器使用 |
| agent-browser-stagehand | 3.609 | Stagehand 集成 |
| stagehand-browser-cli | 3.602 | Stagehand CLI |

### MCP 协议类 (9个)
| 技能 | 评分 | 描述 |
|------|------|------|
| mcp-skill | 3.652 | MCP 核心技能 |
| mcp-hass | 3.616 | Home Assistant MCP |
| xiaohongshu-mcp | 3.615 | 小红书 MCP |
| openclaw-mcp-plugin | 3.597 | OpenClaw MCP 插件 |
| atlassian-mcp | 3.566 | Jira/Confluence MCP |
| filesystem-mcp | 3.509 | 文件系统 MCP |

### Codex 子代理类 (10个)
| 技能 | 评分 | 描述 |
|------|------|------|
| codex-orchestrator | 3.542 | 编排器 |
| codex-sub-agents | 3.557 | OpenAI Codex 子代理 |
| codex-cli-task | 3.095 | 后台 Codex CLI |

### Video 视频类 (10个)
| 技能 | 评分 | 描述 |
|------|------|------|
| video-frames | 3.636 | 视频帧提取 |
| video-subtitles | 3.489 | 视频字幕生成 |
| ai-notes-of-video | 3.506 | AI 视频笔记 |
| demo-video | 3.509 | 演示视频创建 |

### AI 助手/记忆类 (10个)
| 技能 | 评分 | 描述 |
|------|------|------|
| ai-meeting-notes | 3.573 | AI 会议笔记 |
| elite-longterm-memory | 3.743 | 精英长期记忆 |
| memoryai | 3.221 | 持久长期记忆 |
| agent-scorecard | 3.199 | 代理质量评估 |

### Notes 笔记类 (10个)
| 技能 | 评分 | 描述 |
|------|------|------|
| apple-notes | 3.682 | Apple Notes |
| bear-notes | 3.600 | Bear Notes |
| ai-meeting-notes | 3.573 | AI 会议笔记 |

### Avatar 头像类 (5个)
| 技能 | 评分 | 描述 |
|------|------|------|
| heygen-avatar-lite | 3.490 | HeyGen AI 头像视频 |
| avatar | 3.479 | 通用头像 |

### Telegram 类 (5个)
| 技能 | 评分 | 描述 |
|------|------|------|
| telegram | 3.621 | Telegram 集成 |
| telegram-bot | 3.528 | 机器人构建 |

---

## 📊 扫描统计

- **本地技能**: 54 个
- **系统级技能**: 52 个
- **ClawHub 锁定技能**: 12 个
- **ClawHub 热门搜索**: browser(10), mcp(9), codex(10), video(10), ai(10), notes(10), avatar(5), telegram(5)
- **本次新发现 ClawHub 技能**: 25 个
- **高价值候选**: 14 个
- **最新更新技能**: 25 个（explore 扫描）

---

## 🎯 建议行动

### 🔥 高优先级（强烈推荐）

1. **ai-meeting-notes** (3.573)
   - AI 会议笔记自动生成，含行动项追踪
   - 与现有 ai-daily-briefing 形成互补
   - 无需设置，即用型

2. **ai-notes-of-video** (3.506)
   - AI 视频笔记自动生成
   - 适合学习、会议记录、内容分析
   - 与现有 video-frames 形成互补

3. **filesystem-mcp** (3.509)
   - MCP 协议标准化的文件系统访问
   - 与现有 mcp-lark 形成 MCP 协议矩阵

4. **codex-cli-task** (3.095)
   - 后台异步 Codex CLI，自动推送消息
   - 最新发布，活跃维护

5. **xiaohongshu-mcp** (3.615)
   - 小红书 MCP 自动化运营
   - 适合社交媒体内容创作

### ⭐ 中优先级

6. **codex-orchestrator** (3.542)
   - Codex 多代理编排协调
   - 适合复杂多代理编码任务

7. **video-subtitles** (3.489)
   - 视频字幕自动生成
   - 适合多媒体内容创作

8. **fast-browser-use** (3.623)
   - 高性能浏览器自动化
   - 可作为 agent-browser 升级候选

9. **agent-scorecard** (3.199)
   - 代理质量评估
   - 生产环境质量保障

10. **asr-skill** (2.777)
    - 中文方言语音转文字
    - 22种方言支持

11. **memoryai** (3.221)
    - 持久长期记忆
    - 评估与现有记忆技能差异

12. **openclaw-shield-upx** (3.320)
    - 安全监控和威胁检测
    - 评估与现有安全技能差异

### 📌 低优先级

13. **telegram-bot** (3.528)
    - Telegram 机器人构建
    - 作为 Feishu 备选消息平台

14. **heygen-avatar-lite** (3.490)
    - HeyGen AI 头像视频
    - 补充静态头像能力

---

## 🔔 高价值技能通知

**🔥 本次扫描强烈推荐关注**:

1. **ai-meeting-notes** - AI 会议笔记生成 ⭐⭐⭐⭐⭐ (评分 3.573)
2. **ai-notes-of-video** - AI 视频笔记 ⭐⭐⭐⭐⭐ (评分 3.506)
3. **filesystem-mcp** - MCP 文件系统访问 ⭐⭐⭐⭐⭐ (评分 3.509)
4. **codex-cli-task** - 后台 Codex CLI ⭐⭐⭐⭐⭐ (新发布)
5. **xiaohongshu-mcp** - 小红书 MCP 自动化 ⭐⭐⭐⭐ (评分 3.615)
6. **codex-orchestrator** - Codex 多代理编排 ⭐⭐⭐⭐ (评分 3.542)
7. **video-subtitles** - 视频字幕生成 ⭐⭐⭐⭐ (评分 3.489)
8. **fast-browser-use** - 高性能浏览器自动化 ⭐⭐⭐⭐ (评分 3.623)
9. **agent-scorecard** - 代理质量评估 ⭐⭐⭐⭐ (评分 3.199)
10. **asr-skill** - 中文方言语音识别 ⭐⭐⭐⭐ (评分 2.777)
11. **memoryai** - 持久长期记忆 ⭐⭐⭐⭐ (评分 3.221)
12. **openclaw-shield-upx** - 安全监控 ⭐⭐⭐ (评分 3.320)
13. **telegram-bot** - Telegram 机器人 ⭐⭐⭐ (评分 3.528)
14. **heygen-avatar-lite** - HeyGen AI 视频 ⭐⭐⭐ (评分 3.490)

**🆕 最新热门技能**:
- douyin-creator (抖音创作者)
- tushare-stock-skill (Tushare 股票)
- excalidraw-diagram (手绘图表)
- mermaid-visualizer (Mermaid 图表)
- smart-illustrator (智能配图)
- video-script-creator (视频脚本)
- wechat-mp-writer (公众号写作)

---

*此文档由 cron 任务自动生成 — 任务ID: 9cbde662-1490-4c6b-aabe-99b68f8f4331*

## 扫描记录

- 2026-03-09 20:01: 本地 54 技能，系统 52 技能，ClawHub 扫描完成，发现 8 个高价值候选
- 2026-03-09 22:01: 本地 54 技能，系统 52 技能，评分更新: ai-notes-of-video (3.722), filesystem-mcp (3.692), fast-browser-use (3.623)
- 2026-03-10 00:01: 本地 54 技能，系统 52 技能，评分稳定，无重大变化
- 2026-03-10 02:01: 本地 54 技能，系统 52 技能，新发现 8 个技能，包括 codex-cli-task、memoryai、agent-scorecard、asr-skill 等
- 2026-03-10 04:01: 本地 54 技能，系统 52 技能，评分更新: filesystem-mcp (3.693 ↑), ai-meeting-notes (3.573 ↑), codex-orchestrator (3.542 ↑), video-subtitles (3.489 ↑), fast-browser-use 评分下降至 3.248
- 2026-03-10 06:01: 本地 54 技能，系统 52 技能，评分更新: fast-browser-use (3.623 ↑ 回升), filesystem-mcp (3.509), memoryai (3.221), 无新技能发现
- 2026-03-10 08:01: 本地 54 技能，系统 52 技能，ClawHub 12 锁定技能，explore 扫描发现 25 个最新更新技能，包括 douyin-creator、tushare-stock-skill、excalidraw-diagram 等
