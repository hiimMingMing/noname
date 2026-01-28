const fs = require('fs');
const menu = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));
const b3 = JSON.parse(fs.readFileSync('batch3_translated.json', 'utf-8'));

let added = 0;
for (const [k, v] of Object.entries(b3)) {
    if (!menu[k]) {
        menu[k] = v;
        added++;
    }
}

fs.writeFileSync('locales/vi-VN/menu.json', JSON.stringify(menu, null, 2), 'utf-8');
console.log(`✅ Added: ${added} new translations`);
console.log(`📊 Total keys: ${Object.keys(menu).length}`);
