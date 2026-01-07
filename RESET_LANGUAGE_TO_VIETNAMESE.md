# Đặt Lại Ngôn Ngữ Sang Tiếng Việt / Reset Language to Vietnamese

## 🔧 Vấn Đề / Problem

Trình duyệt của bạn đã lưu cấu hình ngôn ngữ cũ (có thể là `en-US` hoặc `zh-CN`), nên game không tự động chuyển sang tiếng Việt mặc định.

Your browser has saved an old language preference (possibly `en-US` or `zh-CN`), so the game doesn't automatically switch to Vietnamese default.

---

## ✅ Giải Pháp / Solution

### Cách 1: Xóa localStorage trong trình duyệt (Khuyến nghị)

**Method 1: Clear localStorage in browser (Recommended)**

1. **Mở game trong trình duyệt:**
   - Chạy: `pnpm run dev`
   - Mở: http://127.0.0.1:8083/

2. **Mở Console (F12):**
   - Nhấn phím **F12** để mở Developer Tools
   - Chuyển sang tab **Console**

3. **Chạy lệnh sau để xóa cấu hình ngôn ngữ cũ:**

```javascript
// Xóa tất cả cấu hình cũ (bao gồm language)
localStorage.clear();

// Hoặc chỉ xóa cấu hình ngôn ngữ:
// localStorage.removeItem('config');

// Sau đó reload lại trang
location.reload();
```

4. **Reload trang:**
   - Game sẽ tự động load lại
   - Lần này sẽ dùng tiếng Việt mặc định ✅

---

### Cách 2: Xóa IndexedDB (Nếu Cách 1 không hiệu quả)

**Method 2: Clear IndexedDB (If Method 1 doesn't work)**

1. **Mở Developer Tools (F12)**

2. **Chuyển sang tab "Application"**

3. **Tìm "IndexedDB" ở sidebar bên trái:**
   - Mở rộng **IndexedDB**
   - Tìm database của game (có thể là `noname` hoặc tương tự)
   - Click phải → **Delete database**

4. **Reload trang:**
   ```javascript
   location.reload();
   ```

---

### Cách 3: Xóa tất cả dữ liệu trình duyệt cho site này

**Method 3: Clear all site data**

1. **Chrome/Edge:**
   - Nhấn **F12** → Tab **Application**
   - Click **"Clear storage"** ở sidebar
   - Tick tất cả các ô
   - Click nút **"Clear site data"**
   - Reload trang

2. **Firefox:**
   - Nhấn **F12** → Tab **Storage**
   - Click phải lên site URL
   - Chọn **"Delete All"**
   - Reload trang

---

## 🧪 Kiểm Tra / Verification

Sau khi xóa dữ liệu cũ, mở Console (F12) và chạy:

```javascript
// Kiểm tra ngôn ngữ hiện tại
console.log('Locale:', lib.i18n.getLocale());
// Kỳ vọng: "vi-VN"

// Kiểm tra bản dịch
console.log('sha:', lib.translate.sha);
// Kỳ vọng: "Trảm" (tiếng Việt)
// Không phải: "杀" (tiếng Trung)

console.log('zhaoyun:', lib.translate.zhaoyun);
// Kỳ vọng: "Triệu Vân" (tiếng Việt)
// Không phải: "赵云" (tiếng Trung)
```

**Nếu thấy output như trên → ✅ Thành công!**

**If you see output like above → ✅ Success!**

---

## 🔄 Nếu Vẫn Bị Tiếng Trung / If Still in Chinese

Có thể do file bản dịch chưa load đúng. Kiểm tra Console (F12) xem có lỗi không:

```
[i18n] Starting initialization...
[i18n] No saved preference, using default: vi-VN
[i18n] Loaded vi-VN/core.json
[i18n] Loaded vi-VN/cards.json
[i18n] Loaded vi-VN/characters.json
[i18n] Loaded vi-VN/modes.json
[i18n] Loaded vi-VN/menu.json
[i18n] Initialized with locale: vi-VN
```

**Nếu thấy lỗi load file JSON:**
- Kiểm tra xem các file trong `locales/vi-VN/` có tồn tại không
- Kiểm tra format JSON có đúng không (không có dấu phẩy thừa ở cuối)

---

## 📝 Lưu Ý / Notes

### Tại sao cần xóa localStorage?

**Why need to clear localStorage?**

Game đã lưu cấu hình ngôn ngữ cũ vào `lib.config.language`. Code hiện tại ưu tiên:

1. ✅ **Saved preference** (nếu có) ← Đây là nguyên nhân
2. ✅ **Default vi-VN** (nếu không có saved preference)

Vì vậy, nếu bạn đã từng chọn ngôn ngữ khác (en-US, zh-CN), nó sẽ được lưu và tiếp tục dùng.

Sau khi xóa localStorage, lần khởi động tiếp theo sẽ dùng mặc định **vi-VN**.

---

## 🎯 Kết Quả Mong Đợi / Expected Result

Sau khi thực hiện các bước trên:

1. ✅ Game khởi động bằng **tiếng Việt**
2. ✅ Tất cả bài, tướng, kỹ năng đều hiển thị **tiếng Việt phong cách kiếm hiệp**
3. ✅ Console hiển thị: `[i18n] Initialized with locale: vi-VN`
4. ✅ `lib.translate.sha` = `"Trảm"` (không phải `"杀"`)
5. ✅ `lib.translate.zhaoyun` = `"Triệu Vân"` (không phải `"赵云"`)

---

## 🚀 Bắt Đầu / Get Started

```bash
# 1. Chạy dev server
pnpm run dev

# 2. Mở trình duyệt
# Open: http://127.0.0.1:8083/

# 3. Nhấn F12, chạy lệnh trong Console:
localStorage.clear();
location.reload();

# 4. Kiểm tra:
console.log('Locale:', lib.i18n.getLocale());
console.log('sha:', lib.translate.sha);
```

---

**Status:** 🟢 **Fix đã sẵn sàng - Chỉ cần xóa localStorage!**

**Status:** 🟢 **Fix is ready - Just clear localStorage!**

---

**Ngày:** 2026-01-07
**Phiên bản:** 1.11.0 + i18n (Vietnamese default)
