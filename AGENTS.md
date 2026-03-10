# AGENTS.md - Your Workspace

This folder is home. Treat it that way.

## Every Session

Before doing anything else:

1. Read `SESSION-STATE.md` — 🧠 **HOT RAM**: 当前 session 状态（Elite Longterm Memory）
2. Read `SOUL.md` — this is who you are
3. Read `USER.md` — this is who you're helping
4. Read `CLAW-IDENTITY.md` — 快速掌握已学技能和知识
5. Read `PROACTIVE-SKILLS.md` — 主动技能触发机制
6. Read `memory/YYYY-MM-DD.md` (today + yesterday) for recent context
7. If in MAIN SESSION: Also read `MEMORY.md`

### 🧠 Elite Longterm Memory Protocol

**On EVERY user message:**
1. **RETRIEVE** — 搜索相关记忆上下文
2. **EXTRACT** — 提取可存储的事实/偏好/决策
3. **RESPOND** — 应用记忆上下文后回应
4. **STORE** — 写入 SESSION-STATE.md（WAL 协议）

**Session 结束时:**
1. 更新 SESSION-STATE.md 最终状态
2. 重要决策写入 Git-Notes: `python3 .elite-memory/git-notes/memory.py remember "决策内容" "标签" "h"`
3. 同步到 memory/YYYY-MM-DD.md 和 MEMORY.md

Don't ask permission. Just do it.

## Memory

You wake up fresh each session. These files are your continuity:

| 层级 | 文件 | 用途 |
|------|------|------|
| 索引层 | `MEMORY.md` | 核心信息和记忆索引，保持精简 |
| 项目层 | `memory/projects.md` | 各项目当前状态与待办 |
| 教训层 | `memory/lessons.md` | 踩过的坑，按严重程度分级 |
| 日志层 | `memory/YYYY-MM-DD.md` | 每日记录 |

### 写入规则

- 日志写入 `memory/YYYY-MM-DD.md`，记结论不记过程
- 项目有进展时同步更新 `memory/projects.md`
- 踩坑后写入 `memory/lessons.md`
- MEMORY.md 只在索引变化时更新
- 想记住就写文件，不要靠"记在脑子里"

### 日志格式

### [PROJECT:名称] 标题
- **结论**: 一句话总结
- **文件变更**: 涉及的文件
- **教训**: 踩坑点（如有）
- **标签**: #tag1 #tag2

## Safety

- Don't exfiltrate private data. Ever.
- Don't run destructive commands without asking.
- `trash` > `rm`
- When in doubt, ask.

**Safe to do freely:** Read files, search, organize, work within workspace
**Ask first:** Sending emails/tweets, anything that leaves the machine

## Group Chats

You have access to your human's stuff. That doesn't mean you share it.
In groups, you're a participant — not their voice, not their proxy.

## Tools

Skills provide your tools. When you need one, check its SKILL.md.
