# Hướng Dẫn Debug i18n / i18n Debugging Guide

## 🔧 Các Fix Đã Áp Dụng / Fixes Applied

### Fix #1: Uncomment `setLocale()` call
**File:** `noname/i18n/index.js:61`
```javascript
// Trước: // await this.setLocale(locale);
// Sau:
await this.setLocale(locale);
```
**Lý do:** setLocale() bị comment out nên translations không được load.

### Fix #2: Setup Translation Interceptor
**File:** `noname/i18n/init.js:35`
```javascript
// Thêm:
setupTranslationInterceptor();
```
**Lý do:** Interceptor không được gọi nên Proxy không hoạt động.

### Fix #3: Add Detailed Logging
**Files:**
- `noname/i18n/index.js` - loadTranslations()
- `noname/i18n/index.js` - applyTranslations()

**Lý do:** Cần logging để debug runtime behavior.

---

## 🧪 Kiểm Tra Trong Browser / Browser Testing

### Bước 1: Mở Game và Console

1. **Chạy dev server:**
   ```bash
   pnpm run dev
   ```

2. **Mở browser:** http://127.0.0.1:8085/

3. **Mở Console:** Nhấn **F12** → Tab **Console**

### Bước 2: Kiểm Tra Console Log

**✅ Log mong đợi (Success):**

```
[i18n] Starting initialization...
[i18n] No saved preference, using default: vi-VN
[i18n] Loading translations for vi-VN...
[i18n] Asset URL: ""
[i18n] Fetching: locales/vi-VN/core.json
[i18n] ✅ Loaded vi-VN/core.json (139 keys)
[i18n] Fetching: locales/vi-VN/cards.json
[i18n] ✅ Loaded vi-VN/cards.json (126 keys)
[i18n] Fetching: locales/vi-VN/characters.json
[i18n] ✅ Loaded vi-VN/characters.json (162 keys)
[i18n] Fetching: locales/vi-VN/modes.json
[i18n] ✅ Loaded vi-VN/modes.json (55 keys)
[i18n] Fetching: locales/vi-VN/menu.json
[i18n] ✅ Loaded vi-VN/menu.json (156 keys)
[i18n] Total translations loaded for vi-VN: 638 keys across 5 categories
[i18n] applyTranslations() called - currentLocale: vi-VN
[i18n] Applying translations from vi-VN...
[i18n] ✅ Applied 139 translations from category: core
[i18n] ✅ Applied 126 translations from category: cards
[i18n] ✅ Applied 162 translations from category: characters
[i18n] ✅ Applied 55 translations from category: modes
[i18n] ✅ Applied 156 translations from category: menu
[i18n] 🎉 Total 638 translations applied to lib.translate
[i18n] Test translations: {sha: "Trảm", shan: "Tránh", tao: "Đào", zhaoyun: "Triệu Vân", hp: "Thể lực"}
[i18n] Initialized with locale: vi-VN
[i18n] Translation interceptor installed
[i18n] System ready - Current locale: vi-VN
```

**❌ Nếu thấy lỗi (Errors):**

```
[i18n] ❌ Failed to load vi-VN/core.json - Status: 404
```
→ File không tồn tại hoặc URL sai

```
[i18n] ❌ Error loading vi-VN/core.json: SyntaxError...
```
→ JSON syntax error

```
[i18n] No translations found for vi-VN
```
→ loadTranslations() failed to populate

### Bước 3: Test Translations Trong Console

Chạy các lệnh sau trong Console:

```javascript
// Test 1: Check locale
console.log('Current locale:', lib.i18n.getLocale());
// Kỳ vọng: "vi-VN"

// Test 2: Check lib.translate có Vietnamese không
console.log('sha:', lib.translate.sha);
// Kỳ vọng: "Trảm"
// Sai: "杀" hoặc undefined

console.log('shan:', lib.translate.shan);
// Kỳ vọng: "Tránh"

console.log('tao:', lib.translate.tao);
// Kỳ vọng: "Đào"

// Test 3: Check tướng
console.log('zhaoyun:', lib.translate.zhaoyun);
// Kỳ vọng: "Triệu Vân"

console.log('guanyu:', lib.translate.guanyu);
// Kỳ vọng: "Quan Vũ"

// Test 4: Check interceptor
console.log('Has interceptor:', lib.translate.__isI18nProxy);
// Kỳ vọng: true

// Test 5: Check translations object
console.log('Translation keys:', Object.keys(lib.i18n.translations['vi-VN']).length);
// Kỳ vọng: 5 (core, cards, characters, modes, menu)

console.log('Total translations:',
  Object.keys(lib.i18n.translations['vi-VN']).reduce((sum, cat) =>
    sum + Object.keys(lib.i18n.translations['vi-VN'][cat]).length, 0)
);
// Kỳ vọng: ~638 keys

// Test 6: Check một số UI strings
console.log('hp:', lib.translate.hp);
// Kỳ vọng: "Thể lực"

console.log('phase_zhunbei:', lib.translate.phase_zhunbei);
// Kỳ vọng: "Giai đoạn chuẩn bị"
```

---

## 🐛 Troubleshooting

### Vấn Đề 1: Tất cả vẫn hiển thị tiếng Trung

**Nguyên nhân có thể:**

1. **Translations không load được (404):**
   - Check Console có lỗi `404 Not Found` không
   - Verify files tồn tại trong `locales/vi-VN/`
   - Check `lib.assetURL` value (nên là `""` trong dev mode)

2. **JSON syntax error:**
   - Check Console có `SyntaxError` không
   - Validate JSON files:
     ```bash
     node -e "JSON.parse(require('fs').readFileSync('locales/vi-VN/core.json'))"
     ```

3. **applyTranslations() không được gọi:**
   - Check Console có log `applyTranslations() called` không
   - Nếu không → `setLocale()` bị skip

4. **Interceptor không hoạt động:**
   - Check Console có log `Translation interceptor installed` không
   - Test: `lib.translate.__isI18nProxy` should be `true`

### Vấn Đề 2: Chỉ một số chữ được dịch

**Nguyên nhân:**
- Một số file không load được (partial load)
- Check Console xem file nào failed

### Vấn Đề 3: lib.translate.sha = undefined

**Nguyên nhân:**
- File `cards.json` chưa load
- Or `sha` key không tồn tại trong file
- Verify: `lib.i18n.translations['vi-VN']['cards']['sha']`

---

## 📊 Expected Console Output

### Giai đoạn 1: Initialization
```
[i18n] Starting initialization...
[i18n] No saved preference, using default: vi-VN
```

### Giai đoạn 2: Loading Translations
```
[i18n] Loading translations for vi-VN...
[i18n] Asset URL: ""
[i18n] Fetching: locales/vi-VN/core.json
[i18n] Fetching: locales/vi-VN/cards.json
...
[i18n] ✅ Loaded vi-VN/core.json (139 keys)
[i18n] ✅ Loaded vi-VN/cards.json (126 keys)
...
[i18n] Total translations loaded for vi-VN: 638 keys across 5 categories
```

### Giai đoạn 3: Applying Translations
```
[i18n] applyTranslations() called - currentLocale: vi-VN
[i18n] Applying translations from vi-VN...
[i18n] ✅ Applied 139 translations from category: core
...
[i18n] 🎉 Total 638 translations applied to lib.translate
[i18n] Test translations: {sha: "Trảm", ...}
```

### Giai đoạn 4: Setup Interceptor
```
[i18n] Translation interceptor installed
[i18n] System ready - Current locale: vi-VN
```

---

## ✅ Success Criteria

Sau khi reload game (với localStorage.clear()), check:

- [ ] Console log shows `vi-VN` as current locale
- [ ] All 5 translation files loaded successfully
- [ ] Total 638 translations applied
- [ ] Test translations show Vietnamese strings
- [ ] `lib.translate.sha` = `"Trảm"`
- [ ] `lib.translate.zhaoyun` = `"Triệu Vân"`
- [ ] `lib.translate.__isI18nProxy` = `true`
- [ ] Game UI displays Vietnamese text

---

## 🚀 Next Steps

1. ✅ Code đã được fix
2. ⏳ Restart dev server: `pnpm run dev`
3. ⏳ Open browser và clear localStorage
4. ⏳ Check Console logs
5. ⏳ Run test commands
6. ⏳ Verify game UI

---

**Dev Server:** http://127.0.0.1:8085/

**Files Modified:**
- `noname/i18n/index.js` - Uncomment setLocale(), add logging
- `noname/i18n/init.js` - Add setupTranslationInterceptor()

**Date:** 2026-01-07
