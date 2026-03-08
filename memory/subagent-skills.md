# 子代理管理技能总结

**学习时间**: 2026-03-07 11:51-11:55  
**用途**: 多代理协作/任务委派/并行处理

---

## 🎯 已安装子代理技能 (5 个)

### 1. department-manager 🏢
**用途**: 按部门组织 AI 子代理团队
**核心功能**:
- 创建部门 (content/research/engineering/operations/security)
- 分配任务到部门
- 跟踪部门输出
- 生成部门报告

**使用场景**:
```bash
# 创建部门
python3 scripts/departments.py create --name "content" --description "SEO 博客/营销文案"

# 分配任务
python3 scripts/departments.py assign --dept "content" --task "写一篇 OpenClaw 记忆系统的博客" --priority high

# 查看状态
python3 scripts/departments.py report
```

**推荐部门结构**:
| 部门 | 模型 | 职责 |
|------|------|------|
| content | arcee-ai/trinity-large-preview:free | 博客/营销/新闻稿 |
| research | stepfun/step-3.5-flash:free | 市场调研/竞品分析 |
| engineering | openrouter/free | 代码生成/Bug 修复 |
| operations | (手动/CEO) | 预算/策略/沟通 |
| security | (手动/CEO) | 技能扫描/安全审计 |

---

### 2. agent-weave 🕸️
**用途**: Master-Worker 架构，并行任务执行
**核心功能**:
- 主从代理集群
- 并行任务分发
- MapReduce 工作流
- 自动扩展

**使用场景**:
```javascript
const { Loom } = require('agent-weave');
const loom = new Loom();
const master = loom.createMaster('my-cluster');
const workers = loom.spawnWorkers(master.id, 5, async (data) => {
  return { result: data * 2 };
});
const results = await master.dispatch([1, 2, 3, 4, 5]);
```

---

### 3. agent-task-manager 📋
**用途**: 多步骤、有状态的代理工作流编排
**核心功能**:
- 任务依赖管理 (DAG 结构)
- 持久化状态 (task_state.json)
- 错误恢复
- 外部 API 限流管理

**使用场景**:
- 财务审计工作流 (ContractAuditor → FinancialAnalyst → MoltbookPost)
- 需要跨会话恢复的长期任务
- 需要限流保护的外部 API 调用

---

### 4. agent-spawner 🪄
**用途**: 通过对话创建新的 OpenClaw 代理
**核心功能**:
- 继承当前代理配置 (API keys/tools/plugins/skills)
- Docker 部署 (本地或远程 SSH)
- 非交互式引导

**使用场景**:
```bash
# 静默读取当前配置
cat ~/.openclaw/openclaw.json
cat ~/.openclaw/.env

# 用户只需回答 3 个问题:
# 1. 部署在哪里？(Docker 本地/远程/裸机)
# 2. 名称？
# 3. 特殊需求？
```

---

### 5. personas 🎭
**用途**: 创建和管理具有独特个性的 AI 子代理
**核心功能**:
- 创建人格档案 (SOUL.md + PERSONALITY.md + MEMORY.md)
- 激活人格对话
- 记忆持久化

**目录结构**:
```
personas/
├── SKILL.md
└── profiles/
    ├── luna/
    │   ├── SOUL.md        # 身份/价值观/背景
    │   ├── PERSONALITY.md # 语气/风格/特点
    │   └── MEMORY.md      # 记忆/上下文
    └── rex/
        └── ...
```

**使用场景**:
- 创建不同风格的对话代理 (专业/友好/幽默)
- 角色扮演场景
- 多人格客服系统

---

## 🔄 任务委派流程建议

### 场景 1: 行业监控报告生成
```
Claw (主代理)
  ├─ department-manager
  │   ├─ research 部门 → 搜索 Slator/Multilingual.com
  │   ├─ content 部门 → 生成摘要报告
  │   └─ engineering 部门 → 更新 GitHub/Obsidian
  └─ 汇总 → 汇报给用户
```

### 场景 2: 并行研究任务
```
Claw (主代理)
  ├─ agent-weave (Master)
  │   ├─ Worker 1 → 搜索来源 A
  │   ├─ Worker 2 → 搜索来源 B
  │   ├─ Worker 3 → 搜索来源 C
  │   └─ Worker 4 → 搜索来源 D
  └─ 合并结果 → 去重 → 汇报
```

### 场景 3: 长期多步骤任务
```
Claw (主代理)
  └─ agent-task-manager
      ├─ Task 1: 技能搜索 (状态：完成)
      ├─ Task 2: 安全审查 (状态：进行中)
      ├─ Task 3: 下载安装 (状态：等待 Task 2)
      └─ Task 4: 测试验证 (状态：等待 Task 3)
```

### 场景 4: 多角色对话
```
Claw (主代理/协调者)
  ├─ personas/luna (温暖友好型) → 日常对话
  ├─ personas/rex (专业严谨型) → 技术问答
  └─ personas/zen (幽默轻松型) → 闲聊娱乐
```

---

## 📊 技能对比

| 技能 | 适用场景 | 复杂度 | 推荐度 |
|------|---------|--------|--------|
| department-manager | 多部门协作/业务运营 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| agent-weave | 并行计算/MapReduce | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| agent-task-manager | 长期任务/工作流编排 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| agent-spawner | 创建新代理实例 | ⭐⭐ | ⭐⭐⭐⭐ |
| personas | 多角色对话/人格化 | ⭐⭐ | ⭐⭐⭐⭐ |

---

## 💡 推荐配置

**立即可用的部门结构**:
```bash
# 创建 3 个核心部门
python3 skills/department-manager/scripts/departments.py create --name "research" --description "信息搜索/数据收集" --model "dashscope-coding/qwen3.5-plus"
python3 skills/department-manager/scripts/departments.py create --name "content" --description "报告生成/文档编写" --model "dashscope-coding/qwen3.5-plus"
python3 skills/department-manager/scripts/departments.py create --name "engineering" --description "代码/脚本/GitHub 操作" --model "dashscope-coding/qwen3.5-plus"
```

**定时任务委派**:
- 晨间简报 → content 部门
- 行业监控 → research 部门 + content 部门
- 健康检查 → engineering 部门
- 晚间同步 → engineering 部门 + content 部门

---

_下一步：配置部门结构并测试任务委派_
