# MEMORY.md - Long-Term Memory

## Preferences

- **联网搜索优先使用 searxng skill** —— 只要涉及联网搜索任务，优先调用 searxng 技能而非直接使用 web_search 工具。
- **Tavily 作为备选** —— 当需要深度搜索或带摘要的查询时使用（API key 已配置）

## Memory System (v2 - 优化版)

### 架构设计
参考 CLAUDE.md + notes/ 模式，采用分层持久化：

```
memory/
├── INDEX.md              # 关键词索引（自动生成，快速检索）
├── MEMORY.md             # 核心索引（本文件，全局偏好）
├── lessons.md            # 踩坑记录（全局）
├── projects.md           # 项目总览（从各项目聚合）
├── logs/
│   └── YYYY-MM-DD.md    # 每日日志（对话结论）
└── projects/
    ├── <project-name>/
    │   └── status.md    # 项目专用状态
```

### 生命周期协议
```
init (session 启动读取) → work (对话中追加) → save (晚间同步持久化)
```

### 检索命令
```bash
# 关键词搜索
grep -r "#关键词" ~/.openclaw/workspace/memory/

# 最新日志
ls -lt ~/.openclaw/workspace/memory/logs/ | head -3

# 项目状态
cat ~/.openclaw/workspace/memory/projects/*/status.md
```

## Skills & Tools

### 已安装技能
- `openclaw-tavily-search` —— Tavily 网络搜索（API key: `~/.openclaw/.env`）
- `reminder` —— 自然语言提醒（数据：`reminders/events.yml`）
- `mcp-lark` —— 飞书 MCP 集成（⏳ 待配置 MCP URL）
- `obsidian` —— Obsidian 笔记管理（Vault: `workspace/obsidian-vault`）
- `github` —— GitHub 操作（gh CLI v2.87.3，⏳ 待认证）

### 常用工具
- `web_search` —— Brave API 快速搜索
- `browser` —— 浏览器自动化（点击、输入、快照）
- `feishu_*` —— 飞书文档/云盘/知识库/Bitable
- `sessions_*` —— 子代理管理与消息传递

## Best Practices (from OpenClaw community)

### 安全优先
- 先读后写：确认 prompt 行为符合预期后再启用文件写入或网络操作
- 隔离执行：敏感操作使用 sandbox 模式
- 输入验证：处理外部输入时保持谨慎

### 记忆系统
- 日志写入 `memory/YYYY-MM-DD.md`，记结论不记过程
- 项目进展同步更新 `memory/projects.md`
- 踩坑后写入 `memory/lessons.md`
- MEMORY.md 只在索引变化时更新

### 身份文件
- `SOUL.md` —— 代理的人格与行为准则
- `AGENTS.md` —— 工作区规则与日常流程
- `USER.md` —— 用户信息与偏好
- `IDENTITY.md` —— 代理的自我认知（名字、性格、emoji）

## Useful Resources

- [OpenClaw Docs](https://docs.openclaw.ai)
- [ClawHub Skills Registry](https://clawhub.com) - 5400+ skills
- [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - 精选技能集合
- [OpenClaw Best Practices](https://www.hostinger.com/tutorials/openclaw-best-practices) - 安全生产指南

## Notes

- Created: 2026-03-05
- Updated: 2026-03-07 (配置完成，同步 GitHub 日志)

## Project Log

- **GitHub 仓库**: https://github.com/erwinqyf/openclaw_using_log
- **配置完成日**: 2026-03-06 (约 50 轮对话，4 小时)
- **对接渠道**: 飞书 (QQ Bot 因限制放弃)

## Credentials & Expiry

| 服务 | Token 位置 | 到期日 | 提醒 |
|------|------------|--------|------|
| Tavily API | `~/.openclaw/.env` | 长期 | - |
| Snyk API | `~/.openclaw/.env` | **2026-04-05** (30 天) | ⚠️ 到期前需更新 |

### Snyk Token 更新提醒
- **到期日**: 2026-04-05
- **获取方式**: https://app.snyk.io/account → API Token → KEY
- **更新操作**: 编辑 `~/.openclaw/.env` 中的 `SNYK_TOKEN`
