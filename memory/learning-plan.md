# 夜间技能学习计划

**启动日期**: 2026-03-07  
**理念**: Live and Learn! 🪞  
**执行时间**: 每天零点（crontab 自动）  
**汇报时间**: 次日早上

---

## 📚 学习来源

### 主要来源
| 来源 | 说明 | 链接 |
|------|------|------|
| **ClawHub** | 官方技能注册表（13,729+ 技能） | https://clawhub.ai/ |
| **awesome-openclaw-skills** | 社区精选 5,494 技能 | https://github.com/VoltAgent/awesome-openclaw-skills |
| **openclaw-hub.org** | 3,286+ 精选技能 | https://openclaw-hub.org/ |

### 安全审查
- ✅ **skill-vetter** - 本地安全审查（已安装）
- ✅ **VirusTotal** - ClawHub 集成扫描
- ⚠️ **Snyk Skill Scanner** - 可选深度扫描

---

## 🎯 学习优先级

### P0 - 核心增强（本周）
| 技能类别 | 数量 | 用途 |
|---------|------|------|
| Productivity & Tasks | 206 | 生产力提升 |
| Search & Research | 350 | 搜索增强 |
| AI & LLMs | 197 | 模型集成 |

### P1 - 自动化扩展（下周）
| 技能类别 | 数量 | 用途 |
|---------|------|------|
| Browser & Automation | 335 | 网页自动化 |
| DevOps & Cloud | 408 | 部署运维 |
| Self-Hosted & Automation | 32 | 本地自动化 |

### P2 - 专项能力（按需）
| 技能类别 | 数量 | 用途 |
|---------|------|------|
| Coding Agents & IDEs | 1222 | 编码辅助 |
| Web & Frontend | 938 | 前端开发 |
| PDF & Documents | 111 | 文档处理 |
| Notes & PKM | 71 | 知识管理 |

---

## 📋 学习流程

### 零点自动执行
```bash
1. 搜索 ClawHub 热门技能（按类别）
2. 用 skill-vetter 审查安全性
3. 阅读 SKILL.md 了解功能
4. 记录到 learning-log.md
5. 选择性安装测试
```

### 早上汇报内容
```markdown
## 🌅 昨夜学习进展 (YYYY-MM-DD)

### 探索的技能
- 技能名 1: 功能简介，是否安装
- 技能名 2: 功能简介，跳过原因

### 新安装的技能
- 技能名：用途，测试计划

### 发现的问题
- 技能冲突/依赖问题
- 安全警告

### 今日建议
- 推荐尝试的技能
- 需要用户决策的事项
```

---

## 📝 学习日志

### 2026-03-07 (今晚)
- [ ] 搜索 Productivity & Tasks 类别热门技能
- [ ] 搜索 Search & Research 类别热门技能
- [ ] 用 skill-vetter 审查前 10 个技能
- [ ] 记录到 learning-log.md

---

## 🔧 相关工具

```bash
# 搜索技能
uv run skills/searxng/scripts/searxng.py search "ClawHub productivity skills"

# 审查技能
cd skills/skill-vetter && python3 scripts/vet.py <skill-path>

# 安装技能
npx clawhub@latest install <skill-slug>
```

---

_最后更新：2026-03-07_
