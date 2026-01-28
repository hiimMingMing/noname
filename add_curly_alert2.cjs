#!/usr/bin/env node
const fs = require('fs');

// Load menu.json
const menu = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));

// Load the exact string from missing_high_priority.json
const missing = JSON.parse(fs.readFileSync('missing_high_priority.json', 'utf-8'));
const curlyKey = missing[0].string;
const translation = 'Bạn có thể sửa địa chỉ tải tiện ích tại Cài đặt → Chung → Địa chỉ lấy tiện ích.';

console.log(`Adding curly quote version...`);
console.log(`Key: ${curlyKey}`);
console.log(`Quote chars: ${curlyKey.charCodeAt(4).toString(16)} and ${curlyKey.charCodeAt(16).toString(16)}`);

menu[curlyKey] = translation;

console.log(`✅ Added translation`);
console.log(`📊 Total keys: ${Object.keys(menu).length}`);

// Save
fs.writeFileSync('locales/vi-VN/menu.json', JSON.stringify(menu, null, 2), 'utf-8');
console.log(`💾 Saved to locales/vi-VN/menu.json`);
