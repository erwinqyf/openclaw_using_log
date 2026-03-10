# Project: 语言服务行业监控

## 状态
- **当前状态**: 🔄 运行中
- **启动日期**: 2026-03-06
- **报告频率**: 周二/四/六 9:00 AM
- **最后报告**: 2026-03-10 (扩展监控范围)
- **飞书文档**: https://feishu.cn/docx/IuVJdqS6uoYWOWxEz60cgfWXnh7
- **参考**: Nimdzi 100 2025 https://www.nimdzi.com/nimdzi-100-2025/

---

## 监控范围 (基于 Nimdzi 100 2025)

### 行业媒体 (3个)
| 来源 | URL | 状态 | 备注 |
|------|-----|------|------|
| Slator | https://slator.com | ✅ | 核心来源，市场情报 |
| Multilingual | https://multilingual.com | ⚠️ | Cloudflare受限 |
| Nimdzi | https://nimdzi.com | ⚠️ | Cloudflare受限 |

### Tier 1 LSPs (Nimdzi 100 Top 10)
| 排名 | 公司 | URL | 状态 |
|------|------|-----|------|
| #1 | TransPerfect | https://www.transperfect.com/blog | ✅ |
| #2 | RWS | https://www.rws.com/news | ✅ |
| #3 | Lionbridge | https://www.lionbridge.com/news | ❌ 404 |
| #4 | LanguageLine | https://www.languageline.com/news | ⏳ 待添加 |
| #5 | Welocalize | https://www.welocalize.com/news | ❌ 404 |
| #6 | Argos Multilingual | https://www.argosmultilingual.com/news | ⏳ 待添加 |
| #7 | translate plus | https://www.translateplus.com/news | ⏳ 待添加 |
| #8 | Summa Linguae | https://summalinguae.com/news | ⏳ 待添加 |
| #9 | Hogarth | https://www.hogarthww.com/news | ⏳ 待添加 |
| #10 | Acolad | https://www.acolad.com/news | ⏳ 待添加 |

### Tier 2 LSPs (Nimdzi 100 #11-30) - 部分
| 排名 | 公司 | URL | 状态 |
|------|------|-----|------|
| #15 | Straker | https://strakertranslations.com/news | ✅ CEO变更跟踪 |
| - | Keywords Studios | https://www.keywordsstudios.com/news | ⏳ |
| - | Pactera EDGE | https://www.pacteraedge.com/news | ⏳ |
| - | Amplexor | https://www.amplexor.com/news | ⏳ |
| - | Semantix | https://www.semantix.com/news | ⏳ |
| - | Alconost | https://alconost.com/news | ⏳ |
| - | Gengo | https://gengo.com/news | ⏳ |

### 技术供应商 (9个)
| 公司 | URL | 类型 | 状态 |
|------|-----|------|------|
| memoQ | https://www.memoq.com/news | TMS/MT | ✅ |
| POEditor | https://poeditor.com/blog | 本地化平台 | ✅ 新增 |
| Google Translate | https://blog.google/products/translate | MT | ✅ 新增 |
| Google Research | https://research.google/blog | AI研究 | ✅ 新增 |
| Smartling | https://www.smartling.com/blog | TMS | ❌ 404 |
| Phrase | https://phrase.com/news | TMS | ❌ 403 |
| XTM | https://xtm.ai/news | TMS | ⏳ |
| Lokalise | https://lokalise.com/blog | 本地化 | ⏳ |
| DeepL | https://www.deepl.com/news | MT | ⏳ |

---

## 近期核心动态

### 1. 2026年AI翻译六大趋势 (2026-03-10)
- **来源**: https://poeditor.com/blog/ai-translation-trends-2026/
- POEditor发布AI翻译趋势报告
- 行业从NMT向LLM转型
- 本地化团队将变为AI运营团队

### 2. Google端到端语音翻译突破 (2026-03-10)
- **来源**: https://research.google/blog/real-time-speech-to-speech-translation/
- 亚3秒延迟实时语音翻译
- 保留原声特征
- 应用场景：会议、客服、消费设备

### 3. Straker 领导层变更 (2026-03-04)
- **来源**: https://slator.com
- Grant Straker 卸任 CEO (26 年后)
- 新架构：双 CEO (David Sowerby + Indiver Nagpal)
- 战略：AI 优先增长

### 4. SlatorCon 2026
- **Remote**: 2026-03-24 (线上)
- **London**: 2026-05-22 (Nobu Hotel)

---

## 待办事项
- [x] 创建飞书云文档 (2026-03-10)
- [x] 配置来源URL要求 (2026-03-10)
- [x] 运行今日行业监控 (2026-03-10)
- [x] 扩展监控范围至Nimdzi 100 (2026-03-10)
- [ ] 添加Tier 1 LSPs (#4-10)
- [ ] 添加Tier 2 LSPs (#11-30)
- [ ] 添加更多技术供应商
- [ ] 3/24 跟踪 SlatorCon Remote 内容
- [ ] 持续监控 Straker 双 CEO 过渡
- [ ] 配置 Brave Search API 增强覆盖
- [ ] 关注Google S2ST技术商业落地

---

## 输出规范
1. **飞书云文档**: https://feishu.cn/docx/IuVJdqS6uoYWOWxEz60cgfWXnh7
2. **格式**: 按日期分章节 (`## YYYY-MM-DD`)
3. **来源URL**: 每个条目必须标注完整URL
4. **公司类型**: 标注[Tier 1/2 LSP | 技术供应商 | 行业媒体]
5. **重点标记**: 核心动态用【重点】标注

---

## 相关文件
- 配置: `../../skills/industry-monitor/config.json`
- SKILL: `../../skills/industry-monitor/SKILL.md`
- 教训记录: `../lessons.md`

---

## 关键词
#行业监控 #语言服务 #Slator #Nimdzi100 #本地化 #AI翻译

---
_最后更新：2026-03-10_
