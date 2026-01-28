#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add curly quote version of alert message
"""

import json

# Load menu.json
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    menu = json.load(f)

# Add the curly quote version (Python handles Unicode properly)
curly_quote_key = '您可以在"设置→通用→获取扩展地址"中，修改下载扩展时所采用的地址。'
translation = "Bạn có thể sửa địa chỉ tải tiện ích tại Cài đặt → Chung → Địa chỉ lấy tiện ích."

menu[curly_quote_key] = translation

print(f"✅ Added curly quote version")
print(f"   Key: {curly_quote_key}")
print(f"   Total keys: {len(menu)}")

# Save
with open('locales/vi-VN/menu.json', 'w', encoding='utf-8') as f:
    json.dump(menu, f, ensure_ascii=False, indent=2)

print(f"💾 Saved to locales/vi-VN/menu.json")
