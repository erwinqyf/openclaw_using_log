# SESSION-STATE.md — Active Working Memory 🧠

> This file is the agent's "RAM" — survives compaction, restarts, distractions.
> **Rule:** Write BEFORE responding. Triggered by user input, not agent memory.

---

## Current Task
Elite Longterm Memory 文件夹结构优化完成

## Key Context
- **User**: 丰 (Asia/Shanghai)
- **Agent**: Claw 🪞 (硅基孪生体)
- **Memory System**: Elite Longterm Memory v3 (6层架构已部署)

## Elite Longterm Memory 架构
```
HOT RAM      → SESSION-STATE.md
WARM STORE   → .elite-memory/vectors/ (LanceDB)
COLD STORE   → .elite-memory/git-notes/ (Git-Notes)
CURATED      → memory/{daily,projects,people,decisions,lessons,topics}
CLOUD        → (可选) SuperMemory
AUTO-EXTRACTION → .elite-memory/mem0/
```

## User Preferences
- 联网搜索优先使用 searxng skill
- Tavily 作为备选搜索
- 每天零点自动同步 GitHub/Obsidian
- 睡前触发晚间总结流程
- 已配置 Elite Longterm Memory 系统

## Recent Decisions
- ✅ 使用 Elite Longterm Memory 解决 session 隔离
- ✅ 配置 SESSION-STATE.md 作为热内存
- ✅ 配置 Git-Notes 知识图谱
- ✅ 更新 AGENTS.md 记忆协议
- ✅ 更新 MEMORY.md 和 HEARTBEAT.md
- ⏳ 配置 LanceDB 向量存储 (可选)
- ⏳ 配置 SuperMemory 云同步 (可选)

## Pending Actions
- [x] 创建 SESSION-STATE.md 热内存
- [x] 初始化 Git-Notes
- [x] 创建记忆检索脚本
- [x] 更新 AGENTS.md 读取规则
- [x] 更新 MEMORY.md 和 HEARTBEAT.md
- [ ] 测试新 session 读取 SESSION-STATE.md
- [ ] 配置 LanceDB 向量存储 (可选)
- [ ] 配置 SuperMemory 云同步 (可选)

## Session History
- **2026-03-10 09:00**: 发现 session 隔离问题，决定安装 Elite Longterm Memory
- **2026-03-10 09:14**: 开始安装配置

---
*Last updated: 2026-03-10 09:14 CST*
*Memory System: Elite Longterm Memory v1.2.0*
