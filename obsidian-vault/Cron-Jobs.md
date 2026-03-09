# 定时任务 Cron Jobs

> 🪞 四个子 Agent 定时任务，统一使用 Asia/Shanghai 时区

---

## 已创建任务

### 1️⃣ 晨间简报 (morning-brief)

| 属性 | 值 |
|------|------|
| **Job ID** | `e24ce47c-3572-420f-a613-3c3a312f85ff` |
| **调度** | 每天 8:00 AM (Asia/Shanghai) |
| **类型** | 隔离会话 |
| **投递** | 飞书 → user:ou_adcbc44a6fb7460391e585338f9e1e35 |
| **下次运行** | 约 9 小时后 |

**任务内容**:
1. 检查天气 (wttr.in/Beijing)
2. 查看 reminders/events.yml
3. 总结今日安排
4. 输出简洁温暖的报告（<300 字，带 emoji）

---

### 2️⃣ 语言服务行业监控 (industry-monitor)

| 属性 | 值 |
|------|------|
| **Job ID** | `1bff411e-d016-423e-b01c-0d6762761530` |
| **调度** | 每周二/四/六 9:00 AM (Asia/Shanghai) |
| **类型** | 隔离会话 |
| **投递** | 飞书 → user:ou_adcbc44a6fb7460391e585338f9e1e35 |
| **下次运行** | 约 10 小时后 |

**监控对象**:
- 行业媒体：Slator, Multilingual, Nimdzi
- 重点企业：TransPerfect, RWS, Appen 等 20 家

**任务内容**:
1. 搜索监控清单（近 7 日动态）
2. 去重合并
3. 生成结构化报告（含【重点】标注）
4. 无更新则自动跳过

---

### 3️⃣ 国家新闻汇总 (daily-news)

| 属性 | 值 |
|------|------|
| **Job ID** | `191b2bf9-0732-4145-9bbe-8284cf445bab` |
| **调度** | 每天 12:00 PM (Asia/Shanghai) |
| **类型** | 隔离会话 |
| **投递** | 飞书 → user:ou_adcbc44a6fb7460391e585338f9e1e35 |
| **下次运行** | 约 13h |

**任务内容**:
1. 搜索权威新闻源（中国/亚太/北美/欧洲）
2. 过滤 24 小时内新闻
3. 去重合并
4. 输出结构化报告（区域分类）

---

### 4️⃣ 健康检查 (health-check)

| 属性 | 值 |
|------|------|
| **Job ID** | `1f5e7359-9792-47bd-83bf-9c137ee88481` |
| **调度** | 每周一 8:00 PM (Asia/Shanghai) |
| **类型** | 隔离会话 |
| **投递** | 飞书 → user:ou_adcbc44a6fb7460391e585338f9e1e35 |
| **下次运行** | 约 3 天后 |

**任务内容**:
1. 检查 ~/.openclaw/.env 和 MEMORY.md 中的 token 到期日
2. clawhub list 检查技能
3. gh repo list 检查 GitHub
4. obsidian-cli list 检查笔记
5. 输出报告（用✅⚠️❌标记状态，提供建议）

---

## 管理命令

```bash
# 查看任务
openclaw cron list

# 手动运行（测试）
openclaw cron run e24ce47c-3572-420f-a613-3c3a312f85ff --force
openclaw cron run 1f5e7359-9792-47bd-83bf-9c137ee88481 --force

# 查看运行历史
openclaw cron runs --id e24ce47c-3572-420f-a613-3c3a312f85ff --limit 10

# 编辑任务
openclaw cron edit e24ce47c-3572-420f-a613-3c3a312f85ff --message "新指令"

# 删除任务
openclaw cron remove e24ce47c-3572-420f-a613-3c3a312f85ff
```

---

## 配置文件

- **Agent 提示**: `workspace/agents/morning-brief/SYSTEM.md`
- **Agent 提示**: `workspace/agents/health-check/SYSTEM.md`
- **配置文档**: `workspace/obsidian-vault/SubAgent-Cron-Config.md`

---

_创建日期：2026-03-06 22:40_
