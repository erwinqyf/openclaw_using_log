# 子 Agent 配置 - 定时任务

> 🪞 两个专用子 Agent，通过 cron 调度执行

---

## 1️⃣ 晨间简报 Agent (morning-brief)

### 用途
每天早上 8 点自动生成简报，包含：
- 隔夜信息总结
- 当日天气
- 待办事项提醒
- 日程安排

### 配置
```json
{
  "name": "晨间简报",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * *",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "生成晨间简报：1. 检查天气 2. 查看 reminders/events.yml 3. 总结待办 4. 输出简洁报告"
  },
  "delivery": {
    "mode": "announce",
    "channel": "feishu",
    "to": "user:ou_adcbc44a6fb7460391e585338f9e1e35"
  }
}
```

### CLI 命令
```bash
openclaw cron add \
  --name "晨间简报" \
  --cron "0 8 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "生成晨间简报：1. 检查天气 2. 查看 reminders/events.yml 3. 总结待办 4. 输出简洁报告" \
  --announce \
  --channel feishu \
  --to "user:ou_adcbc44a6fb7460391e585338f9e1e35"
```

---

## 2️⃣ 健康检查 Agent (health-check)

### 用途
每周一晚上 8 点执行系统健康检查：
- 检查技能状态
- Token 到期提醒（Snyk、Tavily 等）
- GitHub 同步状态
- Obsidian 备份检查
- 更新 openclaw_using_log 仓库

### 配置
```json
{
  "name": "健康检查",
  "schedule": {
    "kind": "cron",
    "expr": "0 20 * * 1",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "执行健康检查：1. 检查 ~/.openclaw/.env 中的 token 到期日 2. 检查技能状态 3. 更新 GitHub 仓库 README 4. 输出报告"
  },
  "delivery": {
    "mode": "announce",
    "channel": "feishu",
    "to": "user:ou_adcbc44a6fb7460391e585338f9e1e35"
  }
}
```

### CLI 命令
```bash
openclaw cron add \
  --name "健康检查" \
  --cron "0 20 * * 1" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "执行健康检查：1. 检查 ~/.openclaw/.env 中的 token 到期日 2. 检查技能状态 3. 更新 GitHub 仓库 README 4. 输出报告" \
  --announce \
  --channel feishu \
  --to "user:ou_adcbc44a6fb7460391e585338f9e1e35"
```

---

## 管理命令

### 查看任务
```bash
openclaw cron list
```

### 手动运行（测试）
```bash
openclaw cron run <job-id> --force
```

### 查看运行历史
```bash
openclaw cron runs --id <job-id> --limit 10
```

### 编辑任务
```bash
openclaw cron edit <job-id> --message "新指令"
```

### 删除任务
```bash
openclaw cron remove <job-id>
```

---

_创建日期：2026-03-06_
