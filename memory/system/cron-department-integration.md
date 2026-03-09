# 定时任务 - 部门集成配置

**配置日期**: 2026-03-07  
**配置状态**: ✅ 完成

---

## 📋 定时任务与部门映射

| 定时任务 | 执行时间 | 负责部门 | 任务内容 |
|---------|---------|---------|---------|
| 晨间简报 | 每天 8:00 AM | content | 天气 + 日程 + 待办 |
| 行业监控 | 二/四/六 9:00 AM | research + content | 搜索 + 报告生成 |
| 国家新闻 | 每天 12:00 PM | research + content | 收集 + 汇总 |
| 健康检查 | 每周一 8:00 PM | engineering | Token 检查 + 系统健康 |
| 晚间同步 | 每天 0:00 AM | engineering + content | GitHub + Obsidian + 记忆更新 |

---

## 🏢 部门结构

### research 部门 📚
- **职责**: 行业监控/信息搜索/数据收集
- **模型**: dashscope-coding/qwen3.5-plus
- **定时任务**: 行业监控、国家新闻 (信息收集部分)

### content 部门 ✍️
- **职责**: 报告生成/文档编写/晨间简报
- **模型**: dashscope-coding/qwen3.5-plus
- **定时任务**: 晨间简报、行业监控 (报告生成)、国家新闻 (汇总)

### engineering 部门 🔧
- **职责**: 代码/GitHub/技能安装/系统维护
- **模型**: dashscope-coding/qwen3.5-plus
- **定时任务**: 健康检查、晚间同步

---

## 🔧 配置文件

### Crontab 配置
```bash
# 查看配置
crontab -l

# 位置
/etc/spool/cron/admin
```

### 部门委派脚本
```
/home/admin/.openclaw/scripts/delegate_tasks.py
```

### 部门管理脚本
```
/home/admin/.openclaw/workspace/skills/department-manager/scripts/departments.py
```

### 数据存储
```
~/.openclaw/department-manager/departments.json
```

---

## 📝 常用命令

### 查看部门列表
```bash
python3 ~/.openclaw/workspace/skills/department-manager/scripts/departments.py list
```

### 查看活跃任务
```bash
python3 ~/.openclaw/workspace/skills/department-manager/scripts/departments.py active
```

### 生成部门报告
```bash
python3 ~/.openclaw/workspace/skills/department-manager/scripts/departments.py report
```

### 手动委派任务
```bash
python3 ~/.openclaw/scripts/delegate_tasks.py <任务名>
# 任务名：morning | industry | news | health | evening
```

### 查看执行日志
```bash
# 定时任务日志
tail -f /home/admin/.openclaw/cron.log

# 晚间同步日志
tail -f /home/admin/.openclaw/evening-sync.log
```

---

## 🔄 任务执行流程

### 行业监控示例 (二/四/六 9:00 AM)

```
1. Crontab 触发
   └─> python3 delegate_tasks.py industry

2. delegate_tasks.py 委派任务
   ├─> research 部门：搜索行业动态
   └─> content 部门：生成周报

3. 任务记录到 departments.json
   └─> 状态：pending

4. Claw (主代理) 处理任务
   ├─> 读取待处理任务
   ├─> 执行搜索/生成报告
   └─> 更新任务状态为 completed

5. 晚间同步时生成部门报告
   └─> memory/department-report.md
```

---

## 📊 监控与维护

### 每日检查
- [ ] 查看活跃任务 (`departments.py active`)
- [ ] 检查 cron 日志 (`tail cron.log`)

### 每周检查 (周一健康检查)
- [ ] 生成部门报告 (`departments.py report`)
- [ ] 检查 Token 到期情况
- [ ] 清理已完成任务

### 每月维护
- [ ] 审查部门结构是否需要调整
- [ ] 优化任务分配策略
- [ ] 更新模型配置

---

## 🎯 扩展建议

### 可添加的新部门
- **security 部门**: 安全审计/技能审查
- **operations 部门**: 财务/运营/数据分析
- **support 部门**: 用户支持/问题解答

### 可添加的定时任务
- **周报生成**: 每周日 6:00 PM
- **技能学习**: 每天 2:00 AM
- **数据备份**: 每周六 3:00 AM

---

_最后更新：2026-03-07_
