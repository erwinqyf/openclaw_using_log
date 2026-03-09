# Lessons - 踩坑记录

## [2026-03-06] QQ Bot 无法用于定时任务
- **问题**: QQ Bot 官方限制主动消息数量，没有用户输入就无法输出
- **影响**: 无法实现定时提醒/日报等功能
- **解决**: 迁移至飞书
- **参考**: https://bot.q.qq.com/wiki/develop/api-v2/server-inter/message/send-receive/send.html
- **标签**: #QQBot #限制 #飞书迁移

## [2026-03-06] 部分行业网站抓取受限
- **问题**: Multilingual.com, Nimdzi, Lionbridge 等因 Cloudflare 或 URL 变更无法直接抓取
- **影响**: 行业监控覆盖不全
- **解决**: 后续配置 Brave Search API 增强覆盖
- **标签**: #爬虫 #Cloudflare #监控

---
_最后更新：2026-03-07_
