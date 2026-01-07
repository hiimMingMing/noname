# Locales Directory / 语言目录

This directory contains translation files for Noname's internationalization system.

本目录包含无名杀国际化系统的翻译文件。

## Structure / 结构

```
locales/
├── config.json          # Locale configuration
├── en-US/              # English translations
│   ├── core.json
│   ├── cards.json
│   ├── characters.json
│   ├── modes.json
│   └── menu.json
├── vi-VN/              # Vietnamese translations (Wuxia style)
│   ├── core.json
│   ├── cards.json
│   ├── characters.json
│   ├── modes.json
│   └── menu.json
└── zh-CN/              # Chinese (source language, no files needed)
```

## Supported Languages / 支持的语言

| Code | Language | Native Name | Status | Style |
|------|----------|-------------|--------|-------|
| zh-CN | Simplified Chinese | 简体中文 | ✅ Default | - |
| en-US | English | English | ✅ Complete | Modern |
| vi-VN | Vietnamese | Tiếng Việt | ✅ Complete | Martial Arts |

## Adding a New Language / 添加新语言

1. Create a directory with the language code (e.g., `ja-JP`)
2. Create the 5 required JSON files:
   - `core.json` - Core UI translations
   - `menu.json` - Menu and settings
   - `cards.json` - Card translations
   - `characters.json` - Character and skill translations
   - `modes.json` - Game mode translations
3. Update `config.json` to include the new language
4. Test in-game
5. Submit a pull request

## File Descriptions / 文件说明

### core.json
Core game UI elements, phases, statuses, and common terms.
核心游戏UI元素、阶段、状态和常用术语。

Example keys: `phase_draw`, `damage`, `recover`, `handcard`

### menu.json
Menu items, settings, buttons, and navigation.
菜单项、设置、按钮和导航。

Example keys: `开始`, `选项`, `武将`, `设置`

### cards.json
Card names, descriptions, and effects.
卡牌名称、描述和效果。

Example keys: `sha`, `shan`, `tao`, `sha_info`

### characters.json
Character names, skill names, and skill descriptions.
武将名称、技能名称和技能描述。

Example keys: `zhaoyun`, `longdan`, `longdan_info`

### modes.json
Game mode names, identity names, and mode-specific terms.
游戏模式名称、身份名称和模式特定术语。

Example keys: `zhu`, `zhong`, `nei`, `fan`

## Translation Guidelines / 翻译指南

### General Rules / 通用规则

1. **Accuracy**: Translations must accurately convey the original meaning
   翻译必须准确传达原意

2. **Consistency**: Use consistent terminology throughout
   全文使用一致的术语

3. **Context**: Consider the game context (Three Kingdoms theme)
   考虑游戏背景（三国主题）

4. **Format**: Maintain JSON structure and special symbols
   保持JSON结构和特殊符号

### Special Symbols / 特殊符号

Keep these symbols in translations:
翻译中保留这些符号：

- `【】` - For card names (e.g., `【杀】` → `【Strike】`)
- `〖〗` - For skill names (e.g., `〖龙胆〗` → `〖Dragon Heart〗`)
- `♠♥♣♦` - Card suits (keep as-is)
- `①②③` - Numbered lists (keep as-is)

### Vietnamese Wuxia Style / 越南语武侠风格

The Vietnamese translation uses classical/wuxia terminology:

- Use "ngươi" (汝) instead of "bạn" (you)
- Use Sino-Vietnamese words for martial arts terms
- Maintain poetic and classical style
- Example: "Kỹ năng Tỏa Định" for "锁定技" (Compulsory skill)

## Translation Status / 翻译状态

### en-US (English)
- [ ] core.json (0% - Template ready)
- [ ] menu.json (0% - Template ready)
- [ ] cards.json (0% - Template ready)
- [ ] characters.json (0% - Template ready)
- [ ] modes.json (0% - Template ready)

### vi-VN (Tiếng Việt)
- [x] core.json (100% - Complete)
- [x] menu.json (100% - Complete)
- [x] cards.json (100% - Complete, Wuxia style)
- [x] characters.json (100% - Complete, Wuxia style)
- [x] modes.json (100% - Complete)

## Contributing / 贡献

We welcome translation contributions! / 欢迎贡献翻译！

### How to Contribute / 如何贡献

1. Fork the repository
2. Add or improve translations
3. Test your changes
4. Submit a pull request

See [LOCALIZATION.md](../LOCALIZATION.md) for detailed instructions.
详细说明请参见 [LOCALIZATION.md](../LOCALIZATION.md)。

### Translation Priorities / 翻译优先级

1. 🔴 **High Priority**: core.json, menu.json
2. 🟡 **Medium Priority**: cards.json, characters.json
3. 🟢 **Low Priority**: modes.json

## Testing / 测试

To test your translations:

1. Place files in the appropriate `locales/{language}/` directory
2. Update `config.json` if adding a new language
3. Start the game
4. Go to Settings > Language
5. Select your language
6. Restart the game
7. Check translations in-game

## Resources / 资源

- Full Documentation: [LOCALIZATION.md](../LOCALIZATION.md)
- Quick Start Guide: [LOCALIZATION_QUICKSTART.md](../LOCALIZATION_QUICKSTART.md)
- GitHub Issues: Report translation problems
- GitHub Discussions: Ask questions

## License / 许可证

All translation files are licensed under GPL-3.0, same as the main project.
所有翻译文件采用GPL-3.0许可证，与主项目相同。

---

**Thanks to all translators! / 感谢所有翻译者！**

Maintainers / 维护者:
- Vietnamese (vi-VN): Noname Community
- English (en-US): Looking for volunteers!

Last updated: 2026-01-07
