# 主题：记忆系统

## 当前架构: Elite Longterm Memory v3

### 6层架构

| 层级 | 名称 | 存储位置 | 用途 |
|------|------|----------|------|
| 1 | HOT RAM | SESSION-STATE.md | 跨 session 热内存 |
| 2 | WARM STORE | .elite-memory/vectors/ | LanceDB 语义搜索 |
| 3 | COLD STORE | .elite-memory/git-notes/ | Git-Notes 永久决策 |
| 4 | CURATED | memory/ | 人工可读档案 |
| 5 | CLOUD | (可选) | SuperMemory 跨设备同步 |
| 6 | AUTO-EXTRACTION | .elite-memory/mem0/ | Mem0 自动事实提取 |

### 文件夹结构

```
workspace/
├── SESSION-STATE.md              # HOT RAM
├── .elite-memory/
│   ├── vectors/                  # WARM STORE (LanceDB)
│   ├── git-notes/                # COLD STORE
│   ├── mem0/                     # AUTO-EXTRACTION
│   ├── config.json               # 系统配置
│   ├── recall.sh                 # 检索脚本
│   └── extract.sh                # 提取脚本
└── memory/
    ├── daily/                    # 每日日志
    ├── projects/                 # 项目状态
    ├── people/                   # 人员档案
    ├── decisions/                # 决策记录
    ├── lessons/                  # 经验教训
    └── topics/                   # 主题文件
```

### WAL 协议
- **Write BEFORE responding**
- 用户表达偏好 → 立即写入 SESSION-STATE.md
- 做出重要决策 → 立即写入 Git-Notes
- 用户纠正错误 → 立即更新并记录原因

### 维护周期
- **每天**: 更新 SESSION-STATE.md
- **每周**: 归档已完成任务，清理旧向量
- **每月**: 整合日志到 MEMORY.md

---

*主题文档: 记忆系统架构与维护*
