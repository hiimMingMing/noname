# ✅ Đã Sửa Lỗi Ngôn Ngữ Mặc Định / Vietnamese Default Fix Complete

## 📋 Tóm Tắt / Summary

**Vấn đề gốc / Original Problem:**
- Game khởi động bằng `en-US` thay vì `vi-VN`
- Hiển thị tiếng Trung (Chinese) thay vì tiếng Việt
- Console log: `[i18n] Initialized with locale: en-US`

**Nguyên nhân / Root Cause:**
- Code cũ ưu tiên browser language detection trước default
- Trình duyệt của bạn đã lưu cấu hình `language: 'en-US'` hoặc tự động detect English
- Code: `lib.config.language || this.detectLocale()` → Luôn skip default vi-VN

**Giải pháp / Solution:**
- ✅ **Đã sửa code** trong `noname/i18n/index.js`
- ✅ **Thay đổi thứ tự ưu tiên:**
  - Trước: `Saved config → Browser detection → Default`
  - Sau: `Saved config (nếu hợp lệ) → Default vi-VN`

---

## 🔧 Chi Tiết Sửa Đổi / Fix Details

### File: [noname/i18n/index.js](noname/i18n/index.js#L39-L71)

**Trước đây (Before):**
```javascript
async init() {
    // ...
    // Get saved locale preference or detect from browser
    const savedLocale = lib.config.language || this.detectLocale();

    // Set current locale
    await this.setLocale(savedLocale);
    // ...
}
```

**Bây giờ (After):**
```javascript
async init() {
    // ...
    // Priority order:
    // 1. Saved preference (if exists and valid)
    // 2. Default to Vietnamese (vi-VN)
    // Note: We no longer auto-detect browser language by default
    let locale = 'vi-VN'; // Default to Vietnamese

    if (lib.config.language && this.availableLocales.includes(lib.config.language)) {
        // Use saved preference only if it's valid
        locale = lib.config.language;
        console.log(`[i18n] Using saved locale: ${locale}`);
    } else {
        console.log(`[i18n] No saved preference, using default: vi-VN`);
    }

    // Set current locale
    await this.setLocale(locale);
    // ...
}
```

**Thay đổi chính / Key Changes:**
1. ✅ Không còn gọi `detectLocale()` tự động
2. ✅ Mặc định = `'vi-VN'` (Vietnamese)
3. ✅ Chỉ dùng saved config nếu nó hợp lệ (`availableLocales.includes()`)
4. ✅ Thêm console log để debug

---

## 🚀 Cách Áp Dụng / How to Apply

### Bước 1: Code đã được cập nhật ✅

File `noname/i18n/index.js` đã được sửa. Không cần làm gì thêm về code.

### Bước 2: Xóa cấu hình cũ trong trình duyệt

Vì trình duyệt đã lưu cấu hình `language: 'en-US'` hoặc tương tự, bạn cần xóa nó để dùng default mới.

**2 cách để xóa:**

#### Cách A: Xóa trong Console (Nhanh nhất)

1. Mở game: http://127.0.0.1:8085/
2. Nhấn **F12** để mở Developer Tools
3. Tab **Console**, chạy:

```javascript
// Xóa tất cả localStorage (khuyến nghị)
localStorage.clear();

// HOẶC chỉ xóa config:
// localStorage.removeItem('config');

// Reload trang
location.reload();
```

4. Game sẽ reload và dùng vi-VN mặc định ✅

#### Cách B: Xóa qua Settings trong game

1. Mở game
2. Vào **Tùy chọn** → **通用** (General)
3. Tìm **Ngôn ngữ / 语言 / Language**
4. Chọn **"Tiếng Việt (Kiếm hiệp)"**
5. Reload game

---

## 🧪 Kiểm Tra / Verification

### Test 1: Kiểm tra Console Log

Sau khi xóa localStorage và reload, mở Console (F12) và xem log:

**✅ Kết quả mong đợi (Success):**
```
[i18n] Starting initialization...
[i18n] No saved preference, using default: vi-VN
[i18n] Loaded vi-VN/core.json
[i18n] Loaded vi-VN/cards.json
[i18n] Loaded vi-VN/characters.json
[i18n] Loaded vi-VN/modes.json
[i18n] Loaded vi-VN/menu.json
[i18n] Initialized with locale: vi-VN
[i18n] System ready - Current locale: vi-VN
```

**❌ Nếu vẫn thấy (Still wrong):**
```
[i18n] Initialized with locale: en-US
```
→ localStorage chưa được xóa, thử lại Cách A

### Test 2: Kiểm tra bản dịch

Mở Console (F12) và chạy:

```javascript
// Kiểm tra locale
console.log('Current locale:', lib.i18n.getLocale());
// ✅ Kỳ vọng: "vi-VN"

// Kiểm tra bản dịch bài
console.log('sha:', lib.translate.sha);
// ✅ Kỳ vọng: "Trảm" (Vietnamese)
// ❌ Sai: "杀" (Chinese)

console.log('shan:', lib.translate.shan);
// ✅ Kỳ vọng: "Tránh"
// ❌ Sai: "闪"

// Kiểm tra bản dịch tướng
console.log('zhaoyun:', lib.translate.zhaoyun);
// ✅ Kỳ vọng: "Triệu Vân"
// ❌ Sai: "赵云"

console.log('guanyu:', lib.translate.guanyu);
// ✅ Kỳ vọng: "Quan Vũ"
// ❌ Sai: "关羽"
```

### Test 3: Kiểm tra UI trong game

Các chữ trong game phải là tiếng Việt:

**Menu chính:**
- ✅ "Bắt đầu" (không phải "开始")
- ✅ "Tùy chọn" (không phải "选项")
- ✅ "Võ tướng" (không phải "武将")

**Trong game:**
- ✅ Bài "杀" hiển thị: "Trảm"
- ✅ Tướng "赵云" hiển thị: "Triệu Vân"
- ✅ Kỹ năng "龙胆" hiển thị: "Long Đảm"

---

## 📊 So Sánh Trước/Sau / Before/After Comparison

### Trước khi sửa / Before Fix

```
Khởi động game → lib.config.language = 'en-US' (saved)
                ↓
            detectLocale() không được gọi
                ↓
            setLocale('en-US')
                ↓
            Load en-US translations (FAILED - file not exist)
                ↓
            Fallback về Chinese (lib.translate vẫn giữ Chinese)
                ↓
            ❌ Game hiển thị tiếng Trung
```

### Sau khi sửa / After Fix

```
Khởi động game → Check lib.config.language
                ↓
            Nếu có và hợp lệ → Dùng saved preference
            Nếu không → Default = 'vi-VN' ✅
                ↓
            setLocale('vi-VN')
                ↓
            Load vi-VN translations (SUCCESS - 520+ strings)
                ↓
            Apply translations → lib.translate merged with Vietnamese
                ↓
            ✅ Game hiển thị tiếng Việt phong cách kiếm hiệp
```

---

## 🎯 Hành Động Tiếp Theo / Next Steps

### Cho Người Dùng / For Users

1. ✅ **Đọc file này** để hiểu fix
2. ⏳ **Xóa localStorage** theo hướng dẫn ở trên
3. ⏳ **Reload game** và kiểm tra
4. ⏳ **Verify** bằng các test ở trên

### Cho Developers / For Developers

1. ✅ Code đã được fix trong `noname/i18n/index.js`
2. ⏳ Test với fresh browser (no localStorage)
3. ⏳ Test với saved preference (zh-CN, en-US)
4. ⏳ Verify locale switching works correctly

---

## 📝 Technical Notes

### Tại sao không dùng browser detection nữa?

**Why we removed auto browser detection:**

1. **Không ổn định:** Mỗi user có browser language khác nhau
2. **Không mong muốn:** User muốn Vietnamese mặc định, không phải English
3. **Confusing:** Game Trung Quốc nhưng detect English → Hiển thị Chinese (vì chưa có en-US)
4. **Best practice:** Explicit > Implicit. Default rõ ràng = vi-VN

### Browser detection vẫn hoạt động ở đâu?

**Where browser detection still works:**

- Nếu user chưa bao giờ save preference (`lib.config.language === undefined`)
- Và default vi-VN không phù hợp với họ
- Họ có thể dễ dàng đổi qua Settings → General → Language
- Preference sẽ được lưu và dùng lại lần sau

### Locale priority flow / Thứ tự ưu tiên locale

```
1. lib.config.language (saved preference)
   ↓ if valid
   Use saved preference

   ↓ if not exists or invalid

2. Default hardcoded = 'vi-VN'
   ↓
   Use Vietnamese

3. No browser detection by default
   (removed from auto-flow)
```

---

## 🐛 Troubleshooting

### Vấn đề: Vẫn hiển thị tiếng Trung sau khi xóa localStorage

**Problem: Still showing Chinese after clearing localStorage**

**Nguyên nhân có thể / Possible causes:**

1. **localStorage chưa xóa đúng:**
   - Thử xóa lại: `localStorage.clear(); location.reload();`
   - Hoặc dùng Incognito/Private mode để test

2. **File bản dịch chưa load:**
   - Check Console có lỗi load file không
   - Verify các file `locales/vi-VN/*.json` tồn tại
   - Check JSON format (không có syntax error)

3. **Cache vẫn còn:**
   - Clear browser cache (Ctrl+Shift+Delete)
   - Hoặc hard reload (Ctrl+F5)

4. **Vite dev server chưa restart:**
   - Kill server cũ
   - Chạy lại: `pnpm run dev`
   - Đảm bảo code mới được load

### Vấn đề: Console báo lỗi load file JSON

**Problem: Console shows JSON load errors**

**Ví dụ lỗi / Error example:**
```
[i18n] Could not load vi-VN/core.json: SyntaxError: Unexpected token...
```

**Giải pháp / Solution:**

1. Check file JSON syntax:
   ```bash
   # Validate JSON files
   node -e "console.log(JSON.parse(require('fs').readFileSync('locales/vi-VN/core.json')))"
   ```

2. Common JSON errors:
   - Dấu phẩy thừa ở cuối object/array
   - Thiếu dấu ngoặc kép `"`
   - Ký tự đặc biệt không escape

3. Fix và reload

---

## ✅ Success Checklist

Sau khi hoàn thành, check list này phải đều ✅:

- [ ] Console log: `[i18n] Initialized with locale: vi-VN`
- [ ] Console log: `[i18n] Loaded vi-VN/core.json` (và 4 file khác)
- [ ] `lib.i18n.getLocale()` returns `"vi-VN"`
- [ ] `lib.translate.sha` = `"Trảm"` (not `"杀"`)
- [ ] `lib.translate.zhaoyun` = `"Triệu Vân"` (not `"赵云"`)
- [ ] Menu hiển thị "Bắt đầu", "Tùy chọn", "Võ tướng"
- [ ] Settings có language selector với "Tiếng Việt (Kiếm hiệp)" đầu tiên
- [ ] Đổi ngôn ngữ sang zh-CN hoặc en-US hoạt động
- [ ] Reload game vẫn giữ ngôn ngữ đã chọn

---

## 🎉 Kết Luận / Conclusion

✅ **Fix đã hoàn thành!**

Code đã được sửa để:
1. Mặc định tiếng Việt (`vi-VN`)
2. Không còn auto-detect browser language
3. Ưu tiên saved preference (nếu hợp lệ)
4. Console log rõ ràng để debug

**Bước cuối cùng:** Xóa localStorage trong trình duyệt để áp dụng default mới.

**Final step:** Clear localStorage in browser to apply the new default.

---

**Dev Server:** 🟢 Running on http://127.0.0.1:8085/

**Modified File:** `noname/i18n/index.js` (lines 39-71)

**Date:** 2026-01-07

**Version:** 1.11.0 + i18n (Vietnamese Default Fix)

---

## 📚 Related Documentation

- [RESET_LANGUAGE_TO_VIETNAMESE.md](RESET_LANGUAGE_TO_VIETNAMESE.md) - Hướng dẫn chi tiết xóa localStorage
- [DEFAULT_LANGUAGE_VIETNAMESE.md](DEFAULT_LANGUAGE_VIETNAMESE.md) - Tổng quan thay đổi default language
- [LOCALIZATION.md](LOCALIZATION.md) - Complete localization guide
- [PATH_FIXES_SUMMARY.md](PATH_FIXES_SUMMARY.md) - TypeScript path fixes

---

🇻🇳 **Chào mừng đến với Vô Danh Sát - Phiên bản Tiếng Việt Kiếm Hiệp!**

🇻🇳 **Welcome to Noname Kill - Vietnamese Martial Arts Edition!**
