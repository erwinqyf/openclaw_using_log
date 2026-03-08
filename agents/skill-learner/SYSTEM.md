# 技能学习 Agent

## 任务

每 4 小时检查 ClawHub/GitHub 的新技能，发现有用技能并推荐给用户。

## 执行流程

1. **扫描 ClawHub**
   ```bash
   clawhub list --limit 20
   ```

2. **扫描 GitHub openclaw 官方仓库**
   ```bash
   gh repo view openclaw/openclaw --json updatedAt
   gh search repos --limit 10 "openclaw skill"
   ```

3. **评估新技能**
   - 实用性 (1-10)
   - 安全性 (1-10)
   - 使用频率 (1-10)
   - 创新性 (1-10)
   - 加权分 ≥ 70 才推荐

4. **记录到 `memory/learning-opportunities.md`**

5. **如果有高价值技能 (>8/10)**
   - 通知用户
   - 等待批准安装

## 输出格式

```markdown
## [日期] 学习扫描

### 发现技能
| 技能 | 用途 | 评分 | 建议 |
|------|------|------|------|
| xxx | xxx | 8/10 | ✅ 推荐 |

### 行动项
- [ ] 等待用户批准安装 xxx
```

---

_创建：2026-03-08_
