# 语言服务行业监控

监控语言服务行业动态，基于 Nimdzi 100 榜单覆盖全球顶级语言服务提供商。

## 监控范围

### 1. 行业媒体
| 来源 | URL | 状态 |
|------|-----|------|
| Slator | https://slator.com | ✅ 核心来源 |
| Multilingual | https://multilingual.com | ⚠️ 访问受限 |
| Nimdzi | https://nimdzi.com | ⚠️ 访问受限 |

### 2. Tier 1 LSPs (Nimdzi 100 Top 10)
| 排名 | 公司 | URL | 状态 |
|------|------|-----|------|
| #1 | TransPerfect | https://www.transperfect.com/blog | ✅ |
| #2 | RWS | https://www.rws.com/news | ✅ |
| #3 | Lionbridge | https://www.lionbridge.com/news | ❌ 404 |
| #4 | LanguageLine | https://www.languageline.com/news | ⏳ |
| #5 | Welocalize | https://www.welocalize.com/news | ❌ 404 |
| #6 | Argos Multilingual | https://www.argosmultilingual.com/news | ⏳ |
| #7 | translate plus | https://www.translateplus.com/news | ⏳ |
| #8 | Summa Linguae | https://summalinguae.com/news | ⏳ |
| #9 | Hogarth | https://www.hogarthww.com/news | ⏳ |
| #10 | Acolad | https://www.acolad.com/news | ⏳ |

### 3. Tier 2 LSPs (Nimdzi 100 #11-30)
- Keywords Studios, Pactera EDGE, Amplexor, Semantix
- Straker (CEO变更跟踪), Alconost, Ubiqus, Gengo
- Cloudwords, TextMaster 等

### 4. 技术供应商
| 公司 | URL | 类型 |
|------|-----|------|
| memoQ | https://www.memoq.com/news | TMS/MT |
| Smartling | https://www.smartling.com/blog | TMS |
| Phrase | https://phrase.com/news | TMS |
| XTM | https://xtm.ai/news | TMS |
| POEditor | https://poeditor.com/blog | 本地化平台 |
| Lokalise | https://lokalise.com/blog | 本地化平台 |
| DeepL | https://www.deepl.com/news | MT |
| Google Translate | https://blog.google/products/translate | MT |

### 5. 研究与学术
| 来源 | URL | 类型 |
|------|-----|------|
| Google Research | https://research.google/blog | AI/翻译技术 |
| Microsoft Translator | https://www.microsoft.com/translator/blog | MT技术 |
| OpenAI Blog | https://openai.com/blog | AI/LLM |

## 触发条件
- 定时：每周二、四、六 9:00 AM (Asia/Shanghai)
- 手动：用户说"运行行业监控"或"更新行业报告"

## 输出格式

### 飞书云文档
- **文档名**: 语言服务行业监控
- **文档ID**: IuVJdqS6uoYWOWxEz60cgfWXnh7
- **格式**: 按日期分章节

### 来源URL要求 ⚠️ 必须
**每个新闻/动态条目必须标注来源URL：**

```markdown
#### 1. 标题
- **来源**: https://company.com/news/article-url/
- **公司**: [Tier 1/2 LSP | 技术供应商 | 行业媒体]
- **事件**: ...
```

### 文档结构
```markdown
## YYYY-MM-DD

### 【重点】核心动态
#### 1. 标题
- **来源**: URL (必须)
- **公司**: [类型]
- **事件**: ...

### Tier 1 LSPs 动态
| 日期 | 公司 | 标题 | 来源 |

### Tier 2 LSPs 动态
...

### 技术供应商动态
...

### 行业趋势观察
...

### 监控覆盖说明
...

### 下周关注
...
```

## 执行流程

1. **扫描来源**
   - 遍历所有 enabled=true 的来源
   - 使用 browser/web_fetch 访问
   - 提取最新文章标题和链接

2. **内容提取**
   - 抓取文章正文
   - **记录完整URL**
   - 标注公司类型(Tier 1/2/技术/媒体)

3. **生成报告**
   - 按格式组织内容
   - **确保每个条目有来源URL**
   - 标注【重点】动态

4. **推送飞书**
   - 追加到云文档
   - 发送更新通知

## 质量检查清单

- [ ] 每个新闻条目都有来源URL
- [ ] 标注公司类型(Tier 1/2/技术/媒体)
- [ ] 按日期正确分章节
- [ ] 重点动态用【重点】标记
- [ ] 企业动态表格包含来源列
- [ ] 监控来源表格URL完整

## 参考
- Nimdzi 100 2025: https://www.nimdzi.com/nimdzi-100-2025/
- 飞书文档: https://feishu.cn/docx/IuVJdqS6uoYWOWxEz60cgfWXnh7
