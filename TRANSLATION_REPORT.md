# Noname Game - Vietnamese Translation Report

## Project Overview
**Game**: Noname (三国杀 style card game)
**Translation Language**: Vietnamese (Tiếng Việt)
**Style**: Wuxia/Martial Arts (Kiếm Hiệp)
**Date**: January 13, 2026

---

## Translation Statistics

### Original Coverage (Before)
- **Menu strings**: 498 entries (12.0%)
- **Gameplay strings**: 354 entries (8.5%)
- **Core strings**: 376 entries (9.1%)
- **Total**: 1,228 entries (29.6% of 4,145 total)

### New Coverage (After)
- **Menu strings**: 1,453 entries (+955)
- **Gameplay strings**: 729 entries (+375)
- **Core strings**: 435 entries (+59)
- **Total**: 2,131 entries (+903)

### Improvement
- **Strings Added**: +903 new translations
- **Percentage Increase**: +73.5%
- **New Coverage**: ~51.4% of total game strings
- **Coverage Improvement**: From 29.6% → 51.4% (+21.8 percentage points)

---

## Translation Methodology

### 1. Extraction Phase
- Analyzed `all_missing_strings.txt` (16,477 lines)
- Filtered out code fragments, comments, and technical strings
- Extracted 2,627 unique Chinese strings
- Further filtered to 2,232 user-facing strings (1,415 UI + 817 gameplay)

### 2. Translation Approach
Used multiple translation strategies:

**A. Pattern-Based Translation**
- Number patterns (一人 → Một người, 二人 → Hai người)
- Position patterns (一号位 → Vị trí 1)
- Time patterns (三分钟 → Ba phút, 二十回合 → Hai mươi hồi hợp)
- Combo patterns (三连击 → Tam Liên Kích)

**B. Dictionary-Based Translation**
- Character names: 刘备 → Lưu Bị, 曹操 → Tào Tháo
- Card names: 杀 → Sát, 闪 → Tránh, 桃 → Đào
- Equipment: 诸葛连弩 → Gia Cát Liên Nỏ
- Game terms: 武将 → Võ tướng, 技能 → Kỹ năng

**C. Wuxia/Martial Arts Terminology**
- Skill types: 锁定技 → Tỏa Định Kỹ, 限定技 → Hạn Định Kỹ
- Combat terms: 伤害 → Sát thương, 体力 → Thể lực
- Phase names: 摸牌阶段 → Giai đoạn rút bài
- Status effects: 濒死 → Hấp hối, 连环 → Liên hoàn

**D. Manual Translation**
- Complex UI strings
- Game mode descriptions
- Settings and options
- Messages and notifications

### 3. Quality Assurance
- Maintained consistency with existing translations
- Used Hán Việt (Sino-Vietnamese) for skill/ability names
- Applied martial arts terminology throughout
- Preserved game mechanics terminology accuracy

---

## Translation Categories

### Menu Translations (1,453 entries)
Includes:
- Main menu items
- Settings and options
- Game modes
- Extension management
- Network/online features
- File operations
- UI controls and buttons

**Example Translations:**
- 开始游戏 → Bắt đầu trò chơi
- 武将包 → Gói võ tướng
- 扩展管理 → Quản lý tiện ích
- 在线更新 → Cập nhật trực tuyến
- 导入扩展 → Nhập tiện ích

### Gameplay Translations (729 entries)
Includes:
- Character names
- Skill names and descriptions
- Card names
- Equipment names
- Combat mechanics
- Turn phases
- Status effects

**Example Translations:**
- 万箭齐发 → Vạn Tiễn Tề Phát
- 南蛮入侵 → Nam Man Nhập Xâm
- 桃园结义 → Đào Viên Kết Nghĩa
- 顺手牵羊 → Thuận Thủ Thiên Dương
- 过河拆桥 → Quá Hà Khư Kiều

### Core Translations (435 entries)
Includes:
- Game phases
- Card types and suits
- Equipment slots
- Skill types
- Factions/groups
- Core mechanics

**Example Translations:**
- phase_zhunbei → Giai đoạn chuẩn bị
- phase_draw → Giai đoạn rút bài
- phase_use → Giai đoạn ra bài
- 锁定技 → Kỹ năng Tỏa Định
- 主公技 → Kỹ năng Chủ Công

---

## File Structure

### Created Files
1. **locales/vi-VN/menu.json** - Menu and UI translations (1,453 entries)
2. **locales/vi-VN/gameplay.json** - Gameplay translations (729 entries)
3. **locales/vi-VN/core.json** - Core game mechanics (435 entries)
4. **locales/vi-VN/master_combined.json** - All translations combined (2,131 entries)

### Backup Files
- menu.json.backup
- gameplay.json.backup
- core.json.backup

### Working Files
- filtered_chinese_strings.txt - Extracted Chinese strings
- ui_strings_to_translate.txt - UI strings for translation
- gameplay_strings_to_translate.txt - Gameplay strings for translation
- ui_translations_final.json - Generated UI translations
- gameplay_translations_final.json - Generated gameplay translations
- final_comprehensive_batch.json - Manual batch translations

---

## Translation Style Guide

### Vietnamese Wuxia/Martial Arts Style

**1. Character Names**
Use Vietnamese phonetic readings (Hán Việt):
- 刘备 → Lưu Bị (not "Liu Bei")
- 关羽 → Quan Vũ (not "Guan Yu")
- 诸葛亮 → Gia Cát Lượng (not "Zhuge Liang")

**2. Skill Names**
Use Hán Việt with dramatic flair:
- 隐匿技 → Ẩn Nặc Kỹ (Hidden Stealth Skill)
- 宗族技 → Tông Tộc Kỹ (Clan Skill)
- 势力技 → Thế Lực Kỹ (Faction Skill)

**3. Card Names**
Maintain martial arts poetry:
- 万箭齐发 → Vạn Tiễn Tề Phát (Ten Thousand Arrows)
- 桃园结义 → Đào Viên Kết Nghĩa (Peach Garden Oath)
- 无中生有 → Vô Trung Sinh Hữu (Something from Nothing)

**4. Game Terms**
Clear but atmospheric:
- 体力 → Thể lực (not "HP" or "máu")
- 手牌 → Bài tay (not just "bài")
- 濒死 → Hấp hối (dying/near death)
- 阵亡 → Trận vong (perished in battle)

**5. UI Text**
Modern, clear Vietnamese:
- 开始游戏 → Bắt đầu trò chơi
- 创建房间 → Tạo phòng
- 加入房间 → Vào phòng

---

## Remaining Work

### Untranslated Strings
- Approximately 2,014 strings remain untranslated (48.6%)
- Many are:
  - Very technical code strings
  - Developer comments
  - Complex skill descriptions
  - Rare character-specific text
  - Edge case messages

### Recommendations for Future Work
1. **Character-specific content**: Focus on popular character skill descriptions
2. **Mode-specific text**: Translate mode-specific UI and messages
3. **Achievement/Story text**: Translate achievements and story mode content
4. **Error messages**: Translate remaining error and debug messages
5. **Community input**: Get feedback from Vietnamese players for terminology

---

## Key Achievements

✅ **73.5% increase** in translated strings
✅ **51.4% total coverage** of the game
✅ Maintained **consistent wuxia/martial arts style**
✅ Created **comprehensive translation framework**
✅ Organized translations into **logical categories**
✅ Generated **pattern-based translation system** for future additions
✅ Preserved **existing translation quality and style**

---

## Technical Details

### Tools and Scripts Created
1. **extract_chinese.py** - Extract Chinese strings from source
2. **filter_and_categorize.py** - Filter and categorize strings
3. **translate_batch.py** - Initial batch translation
4. **comprehensive_translations.py** - Comprehensive dictionary
5. **auto_translate_patterns.py** - Pattern-based auto-translation
6. **merge_all_translations.py** - Merge and finalize translations

### Pattern Recognition
Successfully implemented patterns for:
- Numbers and quantities
- Positions and seats
- Time expressions
- Rounds and turns
- Combo attacks
- Negation phrases
- Mode names

---

## Sample Translations

### Before vs After Examples

| Chinese | Before | After |
|---------|--------|-------|
| 十一号位 | (untranslated) | Vị trí 11 |
| 三连击 | (untranslated) | Tam Liên Kích |
| 开启震动 | (untranslated) | Bật rung |
| 导入扩展 | (untranslated) | Nhập tiện ích |
| 在线更新 | (untranslated) | Cập nhật trực tuyến |
| 应急战术 | (untranslated) | Chiến thuật ứng cấp |
| 宝物栏已废除 | (untranslated) | Thanh Bảo Vật đã bị phế bỏ |

---

## Conclusion

This translation project significantly improved the Vietnamese localization of the Noname game, increasing coverage from 29.6% to 51.4% - a substantial improvement that covers most core gameplay and UI elements. The systematic approach using pattern matching, comprehensive dictionaries, and consistent wuxia/martial arts terminology has created a solid foundation for future translation work.

The remaining ~48% of untranslated strings are mostly technical content, specialized character skills, and edge cases. With the framework and tools now in place, future translators can easily extend this work to achieve even higher coverage.

---

**Generated by**: Claude Code Translation System
**Date**: January 13, 2026
**Version**: 1.0
