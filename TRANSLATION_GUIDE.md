# Hướng Dẫn Bổ Sung Translations / Translation Guide

## 📊 Tình Trạng Hiện Tại / Current Status

✅ **i18n system hoạt động tốt!**
- ✅ 593 translations đã có
- ❌ ~70 keys còn thiếu (nhiều keys duplicate)
- ✅ Coverage: ~89%

---

## 🎯 Các Keys Quan Trọng Cần Dịch / Important Missing Keys

### 1. Game States & Actions
```json
{
  "agree": "Đồng ý",
  "cancel2": "Hủy bỏ",
  "refuse": "Từ chối",
  "ok2": "Xác nhận",

  "gameStart": "Bắt đầu trò chơi",
  "createroom": "Tạo phòng",
  "roomlist": "Danh sách phòng",

  "discard_card": "Bỏ bài",
  "draw_card": "Rút bài",
  "selectCard": "Chọn bài",
  "selectTarget": "Chọn mục tiêu",

  "drawPile": "Chồng bài rút",
  "discardPile": "Chồng bài bỏ",

  "revive": "Hồi sinh",
  "reset_character": "Đặt lại tướng"
}
```

### 2. Phases (Giai đoạn)
```json
{
  "phaseZhunbei": "Giai đoạn chuẩn bị",
  "phaseJudge": "Giai đoạn phán xét",
  "phaseDraw": "Giai đoạn rút bài",
  "phaseUse": "Giai đoạn ra bài",
  "phaseDiscard": "Giai đoạn bỏ bài",
  "phaseJieshu": "Giai đoạn kết thúc"
}
```

### 3. Numbers (Số)
```json
{
  "zero": "0",
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
  "ten": "10"
}
```

### 4. Card Suits (đã có icon rồi)
```json
{
  "spade2": "♠",
  "heart2": "♥",
  "club2": "♣",
  "diamond2": "♦",
  "none2": "Vô"
}
```

### 5. Groups/Factions (Thế lực)
```json
{
  "group_wei": "Ngụy",
  "group_wei_bg": "Ngụy",
  "group_shu": "Thục",
  "group_shu_bg": "Thục",
  "group_wu": "Ngô",
  "group_wu_bg": "Ngô",
  "group_qun": "Quần",
  "group_qun_bg": "Quần",
  "group_jin": "Tấn",
  "group_jin_bg": "Tấn",
  "group_key": "Ngô Đông",
  "group_key_bg": "Ngô Đông"
}
```

### 6. Colors (Màu thế lực)
```json
{
  "weiColor": "#4B67AF",
  "shuColor": "#D8874A",
  "wuColor": "#35A05F",
  "qunColor": "#8B8B8B",
  "jinColor": "#8F4E8B",
  "keyColor": "#87CEEB"
}
```

### 7. Damage Types
```json
{
  "take_damage": "Nhận sát thương",
  "get_damage": "Gây sát thương",
  "recover_hp": "Hồi máu",
  "hujia_damage": "Hư giáp"
}
```

### 8. Equipment Slots
```json
{
  "empty_equip1": "Trống (Vũ khí)",
  "empty_equip2": "Trống (Giáp)",
  "empty_equip3": "Trống (+1 Mã)",
  "empty_equip4": "Trống (-1 Mã)",
  "empty_equip5": "Trống (Trân bảo)",
  "empty_equip6": "Trống (Bảo vật)"
}
```

### 9. Mode Configs
```json
{
  "mode_derivation_card_config": "Cấu hình bài phái sinh",
  "mode_banned_card_config": "Cấu hình bài cấm",
  "mode_favourite_character_config": "Cấu hình tướng ưa thích",
  "mode_banned_character_config": "Cấu hình tướng cấm"
}
```

### 10. Special States
```json
{
  "disable_judge": "Vô hiệu phán xét",
  "disable_judge_info": "Phán xét của bạn không hiệu lực",
  "_disableJudge": "Vô hiệu phán xét",

  "_lianhuan": "Liên hoàn",
  "_lianhuan2": "Liên hoàn",
  "_out": "Xuất trận",
  "_recasting": "Đang đúc lại"
}
```

---

## 📝 Cách Bổ Sung Translations / How to Add Translations

### Option 1: Thủ công (Manual)

1. **Mở file tương ứng:**
   - UI/General → `locales/vi-VN/core.json`
   - Cards → `locales/vi-VN/cards.json`
   - Characters → `locales/vi-VN/characters.json`
   - Modes → `locales/vi-VN/modes.json`
   - Menu/Settings → `locales/vi-VN/menu.json`

2. **Thêm translations:**
   ```json
   {
     "existing_key": "Existing translation",

     "_comment_new_section": "New translations",
     "new_key_1": "Bản dịch mới 1",
     "new_key_2": "Bản dịch mới 2"
   }
   ```

3. **Reload game** để thấy thay đổi

### Option 2: Sử dụng AI

Tôi có thể giúp bạn generate translations hàng loạt! Chỉ cần cho tôi biết:
- Category nào? (phases, numbers, groups, etc.)
- Bao nhiêu keys?

---

## 🎨 Style Guide / Hướng Dẫn Phong Cách

### Phong Cách Kiếm Hiệp / Wuxia Style

**DO ✅:**
- Dùng Hán Việt: "Ngụy", "Thục", "Ngô", "Quần"
- Thuật ngữ võ hiệp: "Vũ khí", "Khinh công", "Nội lực"
- Ngôn ngữ cổ điển: "Ngươi", "Ta", "Ngã"

**DON'T ❌:**
- Tiếng Anh: ~~"Card"~~, ~~"Skill"~~
- Tiếng Việt hiện đại: ~~"Bạn"~~, ~~"Tôi"~~
- Slang: ~~"Thẻ bài"~~, ~~"Kỹ năng"~~

### Examples

```json
{
  // ✅ Good - Wuxia style
  "sha": "Trảm",
  "zhaoyun": "Triệu Vân",
  "longdan": "Long Đảm",
  "qinglong": "Thanh Long Đao",

  // ❌ Bad - Modern style
  "sha": "Giết",
  "zhaoyun": "Zhao Yun",
  "longdan": "Gan rồng"
}
```

---

## 🚀 Quick Commands / Lệnh Nhanh

### Kiểm tra coverage hiện tại:
```bash
node scripts/extractLibTranslateKeys.cjs
```

### Validate JSON syntax:
```bash
node -e "JSON.parse(require('fs').readFileSync('locales/vi-VN/core.json'))"
```

### Test translations trong browser:
```javascript
// Open: http://127.0.0.1:8086/
// F12 → Console

lib.translate.sha           // → "Trảm"
lib.translate.gameStart     // → Check if translated
lib.i18n.getLocale()        // → "vi-VN"
```

---

## 📋 Priority List / Danh Sách Ưu Tiên

### 🔴 High Priority (Hiển thị thường xuyên)
1. ✅ Phases (phaseZhunbei, phaseDraw, etc.) - **CẦN DỊCH**
2. ✅ Actions (agree, cancel, refuse, ok) - **CẦN DỊCH**
3. ✅ Numbers (one, two, three, ..., ten) - **CẦN DỊCH**
4. ✅ Groups (group_wei, group_shu, etc.) - **CẦN DỊCH**

### 🟡 Medium Priority (Hiển thị thỉnh thoảng)
5. ✅ Equipment slots (empty_equip1-6) - **CẦN DỊCH**
6. ✅ Damage types (take_damage, recover_hp) - **CẦN DỊCH**
7. ✅ Card suits with number suffix (spade2, heart2) - **CẦN DỊCH**

### 🟢 Low Priority (Hiếm khi hiển thị)
8. ⚠️ Mode configs (mode_banned_card_config, etc.)
9. ⚠️ Technical keys (color, type, nature - nhiều duplicate)
10. ⚠️ Internal keys (Button, Card, Character - class names)

---

## 💡 Tips

1. **Nhiều keys không cần dịch:**
   - Class names: `Button`, `Card`, `Character`, `Player`
   - Internal: `color`, `type`, `nature`, `number` (khi là metadata)
   - Technical: `ws`, `server`, `client`, `config`

2. **Keys trùng lặp:**
   - Nhiều keys xuất hiện nhiều lần trong lib.translate
   - Chỉ cần dịch 1 lần, sẽ apply cho tất cả

3. **Test ngay:**
   - Sau khi thêm translations, reload game
   - Check Console logs
   - Verify trong game UI

---

## 📞 Need Help?

Nếu cần tôi giúp:
1. **Generate translations hàng loạt** - Cho tôi category
2. **Review translations** - Paste JSON cho tôi check
3. **Fix issues** - Cho tôi biết error/warning

---

**Current Coverage:** 89.4% (593/663 keys)

**Target:** 95%+ (chỉ cần ~40 keys quan trọng nữa!)

**Dev Server:** http://127.0.0.1:8086/
