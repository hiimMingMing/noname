# Ngôn Ngữ Mặc Định: Tiếng Việt / Default Language: Vietnamese

## Tóm Tắt / Summary

Trò chơi hiện đã được cấu hình để **mặc định sử dụng Tiếng Việt (phong cách kiếm hiệp)**.

The game is now configured to **default to Vietnamese (martial arts style)**.

---

## Những Thay Đổi / Changes Made

### ✅ 1. Core i18n System / Hệ Thống i18n Cốt Lõi

**File: `noname/i18n/index.js`**

```javascript
// Trước (Before):
this.currentLocale = 'zh-CN';
this.availableLocales = ['zh-CN', 'en-US', 'vi-VN'];
// Default to Chinese
return 'zh-CN';

// Sau (After):
this.currentLocale = 'vi-VN';
this.availableLocales = ['vi-VN', 'zh-CN', 'en-US'];
// Default to Vietnamese
return 'vi-VN';
```

**Thay đổi:**
- ✅ Ngôn ngữ mặc định: `zh-CN` → `vi-VN`
- ✅ Thứ tự ưu tiên: Tiếng Việt đứng đầu
- ✅ Fallback: Chuyển sang tiếng Việt thay vì tiếng Trung khi có lỗi

### ✅ 2. Settings Menu / Menu Cài Đặt

**File: `noname/library/index.js`**

```javascript
// Trước (Before):
language: {
    name: '语言 / Language / Ngôn ngữ',
    init: 'zh-CN',
    intro: '选择游戏语言 / Select game language / Chọn ngôn ngữ trò chơi',
    item: {
        'zh-CN': '简体中文',
        'en-US': 'English',
        'vi-VN': 'Tiếng Việt (Kiếm hiệp)'
    }
}

// Sau (After):
language: {
    name: 'Ngôn ngữ / 语言 / Language',
    init: 'vi-VN',
    intro: 'Chọn ngôn ngữ trò chơi / 选择游戏语言 / Select game language',
    item: {
        'vi-VN': 'Tiếng Việt (Kiếm hiệp)',
        'zh-CN': '简体中文',
        'en-US': 'English'
    }
}
```

**Thay đổi:**
- ✅ Tên cài đặt: Tiếng Việt đứng đầu
- ✅ Giá trị mặc định: `zh-CN` → `vi-VN`
- ✅ Giới thiệu: Tiếng Việt đứng đầu
- ✅ Thứ tự lựa chọn: Tiếng Việt → Trung → Anh
- ✅ Thông báo mặc định: Tiếng Việt

### ✅ 3. Locale Configuration / Cấu Hình Ngôn Ngữ

**File: `locales/config.json`**

```json
// Trước (Before):
{
  "locales": {
    "zh-CN": { "isDefault": true },
    "en-US": { "isDefault": false },
    "vi-VN": { "isDefault": false }
  },
  "fallbackLocale": "zh-CN"
}

// Sau (After):
{
  "locales": {
    "vi-VN": { "isDefault": true },
    "zh-CN": { "isDefault": false },
    "en-US": { "isDefault": false }
  },
  "fallbackLocale": "vi-VN"
}
```

**Thay đổi:**
- ✅ Ngôn ngữ mặc định: `vi-VN`
- ✅ Fallback locale: `vi-VN`
- ✅ Thứ tự: Tiếng Việt đầu tiên

---

## Hành Vi Mới / New Behavior

### Khi Khởi Động Lần Đầu / First Launch

1. **Người dùng chưa có cài đặt ngôn ngữ:**
   - ✅ Game sẽ mặc định hiển thị **Tiếng Việt (phong cách kiếm hiệp)**
   - ✅ Tất cả bài, tướng, kỹ năng đều bằng tiếng Việt
   - ✅ Menu và UI bằng tiếng Việt

2. **Phát hiện ngôn ngữ trình duyệt:**
   - Trình duyệt tiếng Việt (vi, vi-VN) → Tiếng Việt ✅
   - Trình duyệt tiếng Trung (zh, zh-CN) → Tiếng Trung
   - Trình duyệt tiếng Anh (en, en-US) → Tiếng Anh
   - Trình duyệt khác → **Tiếng Việt** (mặc định mới) ✅

### Đổi Ngôn Ngữ / Language Switching

Người chơi vẫn có thể đổi sang ngôn ngữ khác:

1. Vào **Tùy chọn** (Options)
2. Chọn **通用** (General)
3. Tìm **Ngôn ngữ / 语言 / Language** (đầu tiên)
4. Chọn:
   - 🇻🇳 **Tiếng Việt (Kiếm hiệp)** - Mặc định
   - 🇨🇳 简体中文
   - 🇺🇸 English
5. Khởi động lại game

---

## Ví Dụ Hiển Thị / Display Examples

### Menu Chính / Main Menu
```
Bắt đầu          (Trước: 开始)
Tùy chọn         (Trước: 选项)
Võ tướng         (Trước: 武将)
Bài phép         (Trước: 卡牌)
Mở rộng          (Trước: 扩展)
```

### Trong Game / In-Game
```
Bài:
- 杀 → Trảm
- 闪 → Tránh
- 桃 → Đào
- 青龙偃月刀 → Thanh Long Đao

Tướng:
- 赵云 → Triệu Vân
- 诸葛亮 → Gia Cát Lượng
- 关羽 → Quan Vũ

Kỹ năng:
- 龙胆 → Long Đảm
- 观星 → Quan Tinh
- 武圣 → Vũ Thánh

Giai đoạn:
- 准备阶段 → Giai đoạn chuẩn bị
- 出牌阶段 → Giai đoạn ra bài
- 弃牌阶段 → Giai đoạn bỏ bài
```

---

## Kiểm Tra / Testing

### Test 1: Khởi Động Mới / Fresh Start

```bash
# Xóa cấu hình cũ
# Clear localStorage in browser console:
localStorage.clear();

# Khởi động lại game
pnpm dev

# Kỳ vọng: Game hiển thị Tiếng Việt
# Expected: Game shows Vietnamese
```

### Test 2: Kiểm Tra Console / Console Check

```javascript
// Mở browser console (F12)

// Kiểm tra ngôn ngữ hiện tại
console.log('Current locale:', lib.i18n.getLocale());
// Output: "vi-VN"

// Kiểm tra bản dịch
console.log('sha:', lib.translate.sha);
// Output: "Trảm"

console.log('zhaoyun:', lib.translate.zhaoyun);
// Output: "Triệu Vân"

// Kiểm tra danh sách ngôn ngữ
console.log('Available:', lib.i18n.getAvailableLocales());
// Output: [
//   { code: 'vi-VN', name: 'Tiếng Việt' },
//   { code: 'zh-CN', name: '简体中文' },
//   { code: 'en-US', name: 'English' }
// ]
```

### Test 3: Đổi Ngôn Ngữ / Language Switch

1. Vào Settings → General → Language
2. Chọn "简体中文"
3. Khởi động lại
4. ✅ Game hiển thị tiếng Trung
5. Quay lại chọn "Tiếng Việt (Kiếm hiệp)"
6. Khởi động lại
7. ✅ Game hiển thị tiếng Việt

---

## Lợi Ích / Benefits

### 🎯 Cho Người Chơi Việt Nam / For Vietnamese Players

1. **Trải nghiệm ngay lập tức** - Không cần cấu hình, mở là chơi
2. **Phong cách kiếm hiệp** - Thuật ngữ chuẩn văn võ hiệp
3. **Dễ hiểu** - Ngôn ngữ mẹ đẻ, không rào cản
4. **Immersion** - Đắm chìm trong thế giới Tam Quốc

### 🌍 Cho Người Chơi Quốc Tế / For International Players

1. **Vẫn có thể đổi** - Dễ dàng chuyển sang Trung hoặc Anh
2. **Không mất dữ liệu** - Cấu hình được lưu
3. **Hỗ trợ đa ngôn ngữ** - 3 ngôn ngữ sẵn có

### 💻 Cho Developers / For Developers

1. **Không breaking change** - Code cũ vẫn hoạt động
2. **Dễ bảo trì** - Cấu trúc rõ ràng
3. **Mở rộng dễ** - Thêm ngôn ngữ mới đơn giản

---

## Rollback / Khôi Phục

Nếu cần quay lại tiếng Trung làm mặc định:

### Cách 1: Qua Settings (Khuyến nghị)
1. Options → General → Language
2. Chọn "简体中文"
3. Restart

### Cách 2: Code (Developers)

**File: `noname/i18n/index.js`**
```javascript
// Dòng 13:
this.currentLocale = 'zh-CN';  // Đổi lại từ 'vi-VN'

// Dòng 25:
this.availableLocales = ['zh-CN', 'en-US', 'vi-VN'];  // Đổi thứ tự

// Dòng 105:
return 'zh-CN';  // Đổi lại từ 'vi-VN'

// Dòng 116:
locale = 'zh-CN';  // Đổi lại từ 'vi-VN'

// Dòng 57:
this.currentLocale = 'zh-CN';  // Đổi lại từ 'vi-VN'
```

**File: `noname/library/index.js`**
```javascript
// Dòng 948:
init: 'zh-CN',  // Đổi lại từ 'vi-VN'
```

**File: `locales/config.json`**
```json
{
  "fallbackLocale": "zh-CN"  // Đổi lại từ "vi-VN"
}
```

---

## Tổng Kết / Conclusion

🎉 **Hoàn thành!** Game Vô Danh Sát giờ đây mặc định hiển thị **Tiếng Việt phong cách kiếm hiệp**!

✅ **3 files đã được cập nhật:**
1. `noname/i18n/index.js` - Core i18n defaults
2. `noname/library/index.js` - Settings menu defaults
3. `locales/config.json` - Locale configuration

✅ **Tất cả hệ thống hoạt động:**
- Phát hiện ngôn ngữ tự động
- Đổi ngôn ngữ trong game
- Fallback an toàn
- Lưu cấu hình người dùng

🇻🇳 **Chào mừng đến với Vô Danh Sát - Phiên bản Tiếng Việt!**

---

**Date:** 2026-01-07
**Version:** 1.11.0 + i18n
**Default Language:** Vietnamese (vi-VN)
**Translation Style:** Martial Arts / Wuxia (Kiếm hiệp)
