# 语言服务行业监控

监控语言服务行业动态，生成结构化报告并推送至飞书云文档。

## 触发条件
- 定时：每周二、四、六 9:00 AM (Asia/Shanghai)
- 手动：用户说"运行行业监控"或"更新行业报告"

## 输出格式要求

### 1. 飞书云文档
- **文档名**: 语言服务行业监控 (固定)
- **文档ID**: IuVJdqS6uoYWOWxEz60cgfWXnh7
- **格式**: 按日期分章节，每天追加 `## YYYY-MM-DD`

### 2. 来源URL要求 ⚠️ 必须
**每个新闻/动态条目必须标注来源URL，放在条目开头：**

```markdown
#### 1. Straker 重大领导层变更 (3月4日)
- **来源**: https://slator.com/straker-ceo-change/
- **事件**: ...
```

### 3. 文档结构
```markdown
# 语言服务行业监控

## 监控来源
| 来源 | URL | 状态 |

## YYYY-MM-DD

### 【重点】核心动态
#### 1. 标题
- **来源**: URL (必须)
- **事件**: ...

### 企业动态
| 日期 | 类型 | 标题 | 来源 |

### 行业趋势观察
...

### 监控覆盖说明
...

### 下周关注
...
```

## 监控来源

### 主要来源 (Primary)
1. **Slator** - https://slator.com
   - 语言行业市场情报
   - 核心动态、会议信息

2. **TransPerfect Blog** - https://www.transperfect.com/blog
   - 企业博客
   - 行业洞察、案例研究

3. **memoQ News** - https://www.memoq.com/news
   - MT供应商动态
   - 产品更新、奖项

### 次要来源 (Secondary)
4. **RWS News** - https://www.rws.com/news
5. **Multilingual** - https://multilingual.com (受限)
6. **Nimdzi** - https://nimdzi.com (受限)

## 执行流程

1. **扫描来源**
   - 使用 browser/web_fetch 访问各来源
   - 提取最新文章标题和链接

2. **内容提取**
   - 抓取文章正文
   - **记录完整URL**
   - 提取关键信息

3. **生成报告**
   - 按格式组织内容
   - **确保每个条目有来源URL**
   - 标注【重点】动态

4. **推送飞书**
   - 追加到云文档
   - 发送更新通知

## 质量检查清单

- [ ] 每个新闻条目都有来源URL
- [ ] 按日期正确分章节
- [ ] 重点动态用【重点】标记
- [ ] 企业动态表格包含来源列
- [ ] 监控来源表格URL完整

## 示例条目

✅ **正确示例**:
```markdown
#### 1. Straker 重大领导层变更 (3月4日)
- **来源**: https://slator.com/straker-ceo-change/
- **事件**: Straker Limited 创始人兼 CEO Grant Straker 卸任
- **影响**: 双CEO架构，AI优先战略
```

❌ **错误示例** (缺少来源URL):
```markdown
#### 1. Straker 重大领导层变更 (3月4日)
- **事件**: Straker Limited 创始人兼 CEO Grant Straker 卸任
```

## 相关文件
- 配置: `config.json`
- 项目状态: `memory/projects/industry-monitoring/status.md`
- 飞书文档: https://feishu.cn/docx/IuVJdqS6uoYWOWxEz60cgfWXnh7
