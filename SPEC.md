# SPEC: The Blood of Dawnwalker Guide Website

## 1. Problem Statement（问题陈述）

The Blood of Dawnwalker 于 2026 年 9 月 2 日发布，是一款由前 Witcher 3 开发团队打造的开放世界黑暗幻想 ARPG。游戏 IGN 评分 9/10，48 小时销量突破 100 万份。玩家对游戏攻略、系统解析、Boss 打法有强烈搜索需求，但目前网上攻略信息分散且不完整。目标是尽快上线抢占搜索流量。

---

## 2. Proposed Solution（方案描述）

### 页面结构

| 页面 | 内容 |
|------|------|
| **首页** | 游戏简介 + Quick Facts + 核心导航 |
| **Boss 攻略** | 各章节 Boss 打法、攻略技巧 |
| **任务攻略** | 主线/支线任务流程攻略 |
| **系统攻略** | 形态切换、战斗系统、技能树、灵魂吸收 |
| **收集攻略** | 物品收集、成就完成 |

### 首页布局结构

```
┌─────────────────────────────────────┐
│  Header (Logo + Navigation)         │
├─────────────────────────────────────┤
│  Hero: Game Banner + Quick Facts   │
├─────────────────────────────────────┤
│  Quick Navigation Cards             │
│  (Boss/Quests/Systems/Collectibles)│
├─────────────────────────────────────┤
│  Featured Bosses                    │
├─────────────────────────────────────┤
│  Core Systems Overview             │
├─────────────────────────────────────┤
│  Footer                             │
└─────────────────────────────────────┘
```

### 设计风格

| 元素 | 选择 |
|------|------|
| **主题** | 深色主题（契合黑暗幻想风格） |
| **强调色** | 暗红色 #8B0000 + 金色 #D4AF37 |
| **风格** | 黑暗幻想、吸血鬼、哥特风格 |

### 参考网站结构（借鉴）

| 参考网站 | 借鉴内容 |
|----------|----------|
| [farevergame.wiki](https://farevergame.wiki/) | Quick Facts 区块 + Adventurer's Codex 导航 |
| [shindolifewiki.wiki](https://shindolifewiki.wiki/) | 卡片网格型布局 |
| [legacy-piece-wiki.wiki](https://legacy-piece-wiki.wiki/en/) | 代码/奖励突出展示风格 |

### 内容来源
- 官方公开信息（游戏官网、预告片）
- AI 辅助整理和验证

### 目标语言
- 仅英文

---

## 3. Technical Constraints（技术约束）

| 项目 | 选择 |
|------|------|
| **域名** | dawnwalker-wiki.com |
| **部署平台** | Cloudflare Pages |
| **代码托管** | GitHub |
| **前端技术** | HTML5 + Tailwind CSS |
| **上线时间** | 尽快 |

---

## 4. Non-goals（明确不做的事）

- **不提供游戏下载**
- **不提供盗版/破解内容**
- **不接入广告变现**（现阶段专注流量）
- **不支持用户评论/UGC**
- **不开发多语言版本**
- **不开发移动端 App**
- **不复制参考网站的内容**（只借鉴结构，不抄内容）

---

## 5. Success Criteria（成功标准）

| 指标 | 目标 |
|------|------|
| **上线时间** | 尽快（尽快抢占流量） |
| **页面收录** | Google Search Console 收录 > 90% 的页面 |
| **搜索排名** | 核心关键词进入 Google 前3页 |
| **自然流量** | 上线3个月内实现日均100+访问 |

---

## 6. 页面规划

### 6.1 首页 (index.html)
- Hero 区域：游戏 Banner + Quick Facts
- Quick Navigation Cards：4个导航卡片（Boss/Quests/Systems/Collectibles）
- Featured Bosses：精选 Boss 攻略
- Core Systems Overview：核心系统介绍
- Footer

### 6.2 Boss 攻略 (bosses.html)
- Boss 列表（按章节分类）
- Boss 卡片网格
- Boss 详情页/弹窗（弱点、打法技巧、掉落物品）

### 6.3 任务攻略 (quests.html)
- 主线任务列表
- 支线任务列表
- 任务流程详解

### 6.4 系统攻略 (systems.html)
- 形态切换系统（人类 vs 吸血鬼）
- 战斗系统
- 技能树/天赋系统
- 灵魂吸收系统

### 6.5 收集攻略 (collectibles.html)
- 物品收集
- 成就完成

### 6.6 Sitemap
- sitemap.xml
