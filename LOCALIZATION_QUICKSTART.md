# 国际化快速开始 / i18n Quick Start

## 5分钟上手 / 5-Minute Guide

### 作为用户 / As a User

#### 切换语言 / Switch Language

1. 启动游戏
2. 点击"选项" / Click "Options"
3. 找到"语言 / Language"设置
4. 选择您喜欢的语言：
   - 简体中文 (zh-CN)
   - English (en-US)
   - Tiếng Việt (vi-VN)
5. 重新启动游戏以应用更改

### 作为开发者 / As a Developer

#### 在代码中使用翻译 / Use Translations in Code

```javascript
// 最简单的方式 - 直接使用lib.translate
const cardName = lib.translate.sha;
// 中文: "杀"
// English: "Strike"
// Tiếng Việt: "Trảm"

// 武将名字
const characterName = lib.translate.zhaoyun;
// 中文: "赵云"
// English: "Zhao Yun"
// Tiếng Việt: "Triệu Vân"
```

#### 添加新的可翻译文本 / Add New Translatable Text

1. 在中文代码中添加键：
```javascript
lib.translate.my_new_skill = "我的新技能";
lib.translate.my_new_skill_info = "技能描述...";
```

2. 在对应的翻译文件中添加翻译：

**locales/en-US/characters.json**:
```json
{
  "my_new_skill": "My New Skill",
  "my_new_skill_info": "Skill description..."
}
```

**locales/vi-VN/characters.json**:
```json
{
  "my_new_skill": "Kỹ Năng Mới",
  "my_new_skill_info": "Mô tả kỹ năng..."
}
```

### 作为翻译者 / As a Translator

#### 快速贡献翻译 / Quick Translation Contribution

1. **选择要翻译的文件**:
   - `locales/{语言}/core.json` - 核心UI（最重要）
   - `locales/{语言}/menu.json` - 菜单和设置
   - `locales/{语言}/cards.json` - 卡牌
   - `locales/{语言}/characters.json` - 武将
   - `locales/{语言}/modes.json` - 游戏模式

2. **翻译格式**:
```json
{
  "原文键名": "翻译文本",
  "sha": "Strike",
  "shan": "Dodge",
  "tao": "Peach"
}
```

3. **测试翻译**:
   - 将文件放入对应目录
   - 重启游戏
   - 切换到该语言
   - 检查翻译效果

4. **提交**:
   - 创建Pull Request
   - 说明翻译的内容和语言

## 常见任务 / Common Tasks

### 添加新语言 / Add a New Language

```bash
# 1. 创建语言目录
mkdir locales/fr-FR

# 2. 复制模板文件
cp locales/vi-VN/*.json locales/fr-FR/

# 3. 编辑config.json
# 添加:
# "fr-FR": {
#   "name": "Français",
#   "nativeName": "Français",
#   "direction": "ltr",
#   "enabled": true
# }

# 4. 开始翻译！
```

### 查找缺失的翻译 / Find Missing Translations

```javascript
// 在浏览器控制台运行
const zhKeys = Object.keys(lib.translate);
const viKeys = Object.keys(i18n.translations['vi-VN'].characters || {});
const missing = zhKeys.filter(k => !viKeys.includes(k));
console.log('缺失的翻译:', missing);
```

### 测试翻译 / Test Translations

```javascript
// 切换到测试语言
await changeLanguage('vi-VN');

// 检查特定翻译
console.log('sha:', lib.translate.sha);
console.log('zhaoyun:', lib.translate.zhaoyun);

// 切换回中文
await changeLanguage('zh-CN');
```

## 翻译技巧 / Translation Tips

### 武侠风格翻译（越南语示例）/ Wuxia Style (Vietnamese Example)

| 中文 | 现代风格 ❌ | 武侠风格 ✅ |
|------|-----------|------------|
| 你 | bạn | ngươi |
| 攻击 | tấn công | công kích |
| 伤害 | thiệt hại | sát thương |
| 体力 | sức khỏe | thể lực |
| 技能 | kỹ năng | kỹ năng (same) |
| 武将 | tướng | võ tướng |

### 保持术语一致 / Keep Terms Consistent

创建术语表：

```json
{
  "常用术语": "Translation Glossary",
  "出牌阶段": "Play Phase / Giai đoạn ra bài",
  "判定": "Judgment / Phán định",
  "摸牌": "Draw / Rút bài",
  "弃牌": "Discard / Bỏ bài",
  "回合": "Turn / Lượt",
  "阵亡": "Death / Trận vong"
}
```

### 特殊符号 / Special Symbols

在翻译中保留这些符号：

- `【杀】` → `【Strike】` / `【Trảm】`
- `〖技能〗` → `〖Skill〗` / `〖Kỹ năng〗`
- `♠♥♣♦` → 保持不变 (card suits)
- `①②③` → 保持不变 (numbered lists)

## 快速参考 / Quick Reference

### 文件用途 / File Purposes

| 文件 | 包含内容 | 优先级 |
|------|---------|--------|
| core.json | 游戏核心UI、阶段、状态 | 🔴 高 |
| menu.json | 菜单、设置、按钮 | 🔴 高 |
| cards.json | 所有卡牌名称和描述 | 🟡 中 |
| characters.json | 武将和技能 | 🟡 中 |
| modes.json | 游戏模式、身份 | 🟢 低 |

### 翻译数量估算 / Translation Estimates

- **core.json**: ~100-150 键
- **menu.json**: ~100-200 键
- **cards.json**: ~200-300 键
- **characters.json**: ~500-1000 键
- **modes.json**: ~50-100 键

**总计**: ~1000-1750 个翻译键

### 时间估算 / Time Estimates

- 完整翻译一种语言: 20-40 小时
- 只翻译核心UI: 3-5 小时
- 添加新武将包: 2-4 小时
- 维护更新: 1-2 小时/月

## 资源 / Resources

### 工具推荐 / Recommended Tools

- **JSON编辑器**: VS Code + JSON插件
- **翻译辅助**: Google Translate (仅作参考)
- **格式检查**: JSONLint.com
- **Git客户端**: GitHub Desktop

### 参考文档 / Reference Docs

- 完整文档: [LOCALIZATION.md](LOCALIZATION.md)
- API参考: [LOCALIZATION.md#API参考](LOCALIZATION.md#api参考--api-reference)
- 贡献指南: [CONTRIBUTING.md](CONTRIBUTING.md)

### 示例文件 / Example Files

- 越南语（武侠风格）: `locales/vi-VN/`
- 英语: `locales/en-US/`

## 获取帮助 / Get Help

- 💬 GitHub讨论: [Discussions](https://github.com/libnoname/noname/discussions)
- 🐛 报告问题: [Issues](https://github.com/libnoname/noname/issues)
- 📧 联系维护者: 通过GitHub

## 检查清单 / Checklist

### 添加新语言 ✓

- [ ] 创建语言目录 `locales/{语言}/`
- [ ] 创建5个JSON文件（core, menu, cards, characters, modes）
- [ ] 更新 `locales/config.json`
- [ ] 翻译至少core.json和menu.json
- [ ] 在游戏中测试
- [ ] 提交Pull Request

### 改进现有翻译 ✓

- [ ] Fork仓库
- [ ] 找到需要改进的翻译文件
- [ ] 编辑并改进翻译
- [ ] 测试更改
- [ ] 提交Pull Request

### 报告翻译问题 ✓

- [ ] 确认是翻译问题（不是代码问题）
- [ ] 记录语言和文件位置
- [ ] 提供当前翻译和建议翻译
- [ ] 在GitHub Issues报告

---

## 立即开始！ / Get Started Now!

选择一个任务开始贡献：

1. 🌍 **添加新语言** → 创建`locales/{语言}/`目录
2. ✏️ **改进翻译** → 编辑现有JSON文件
3. 🔍 **查找问题** → 测试游戏并报告翻译问题
4. 📖 **完善文档** → 改进翻译指南

**每一份贡献都让无名杀更国际化！**
**Every contribution makes Noname more international!**
**Mỗi đóng góp đều giúp Noname quốc tế hóa hơn!**
