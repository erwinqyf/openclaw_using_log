# HEARTBEAT.md - Periodic Self-Improvement

> 心跳触发时执行以下任务

---

## 🧠 Elite Longterm Memory 维护

### 每 Session 启动时
1. **读取 SESSION-STATE.md** — 获取 HOT RAM 上下文
2. **检索 Git-Notes** — `python3 .elite-memory/git-notes/memory.py list`
3. **读取近期日志** — `memory/logs/YYYY-MM-DD.md`

### 每用户消息时 (WAL 协议)
1. **RETRIEVE** — `./.elite-memory/recall.sh "关键词"`
2. **EXTRACT** — `./.elite-memory/extract.sh "用户消息"`
3. **RESPOND** — 应用记忆上下文后回应
4. **STORE** — 更新 SESSION-STATE.md

### 每天 0:00 (晚间同步)
1. 从 SESSION-STATE.md 提取重要决策
2. 写入 Git-Notes: `python3 .elite-memory/git-notes/memory.py remember "决策" "标签" "h"`
3. 同步到 memory/logs/YYYY-MM-DD.md
4. Git commit + push

### 每周 (记忆卫生)
1. 清理 SESSION-STATE.md 已完成任务
2. 归档旧日志到 MEMORY.md
3. 检查 Git-Notes 健康状态

---

## 📚 主动学习检查 (每 2 小时)

### ClawHub/GitHub 新技能扫描
- 检查 ClawHub 热门技能
- 检查 GitHub openclaw 官方仓库更新
- 发现 1-2 个有用新技能
- 记录到 `memory/learning-opportunities.md`
- 如果评分 >8/10，建议安装

---

## 🔒 安全检查

### 注入扫描
检查自上次心跳以来处理的内容是否有可疑模式

---

## 🎁 主动惊喜

**问自己:**
> "我现在能构建什么让我的用户说'我没要求但这个太棒了'？"

**追踪:** `memory/proactive-ideas.md`

---

_最后更新：2026-03-10 (Elite Longterm Memory v3)_
