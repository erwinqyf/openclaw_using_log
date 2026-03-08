# Memory 目录结构

> 清晰的文件组织，方便快速查找

```
memory/
├── README.md                    # 本文件（结构说明）
├── MEMORY.md                    # 核心索引（全局偏好）
├── lessons.md                   # 踩坑记录（全局）
├── projects.md                  # 项目总览（聚合）
│
├── 2026-03-06.md               # 每日日志（AGENTS.md 格式）
├── 2026-03-07.md               # 每日日志
├── 2026-03-08.md               # 每日日志
│
├── learning/                    # 学习相关
│   ├── README.md               # 学习系统说明
│   ├── learning-opportunities.md  # 技能学习追踪
│   ├── plans/                  # 学习计划
│   │   └── learning-plan.md
│   ├── logs/                   # 学习日志
│   │   ├── learning-log.md
│   │   └── learning-log-2026-03-07-afternoon.md
│   └── summaries/              # 学习总结
│       └── learning-log-summary.md
│
├── system/                      # 系统配置
│   ├── README.md               # 系统说明
│   ├── INDEX.md                # 关键词索引
│   ├── cron-department-integration.md  # 定时任务配置
│   ├── department-report.md    # 部门报告
│   └── subagent-skills.md      # 子代理技能
│
├── projects/                    # 项目状态
│   └── {project-name}/
│       └── status.md
│
└── archives/                    # 归档（旧文件）
```

---

## 快速查找

| 找什么 | 去哪里 |
|--------|--------|
| 今天发生了什么 | `memory/YYYY-MM-DD.md` |
| 我掌握了什么技能 | `learning/learning-opportunities.md` |
| 踩过什么坑 | `lessons.md` |
| 项目进展 | `projects.md` 或 `projects/{name}/status.md` |
| 定时任务配置 | `system/cron-department-integration.md` |
| 关键词索引 | `system/INDEX.md` |

---

## 维护规则

1. **每日日志** - 直接放 memory/ 根目录（AGENTS.md 要求）
2. **学习相关** - 统一放 learning/ 目录
3. **系统配置** - 统一放 system/ 目录
4. **项目状态** - 放 projects/{name}/status.md
5. **旧文件** - 超过 3 个月移入 archives/

---

_最后整理：2026-03-08_
