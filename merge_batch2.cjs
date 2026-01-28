#!/usr/bin/env node
const fs = require('fs');

const menu = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));
const batch2 = JSON.parse(fs.readFileSync('batch2_translated.json', 'utf-8'));

console.log(`📦 Loading...`);
console.log(`   Menu: ${Object.keys(menu).length} keys`);
console.log(`   Batch 2: ${Object.keys(batch2).length} translations`);

let added = 0;
let skipped = 0;

for (const [cn, vi] of Object.entries(batch2)) {
    if (!menu[cn]) {
        menu[cn] = vi;
        added++;
    } else {
        skipped++;
    }
}

fs.writeFileSync('locales/vi-VN/menu.json', JSON.stringify(menu, null, 2), 'utf-8');

console.log(`\n✅ Added: ${added} new translations`);
console.log(`⏭️  Skipped: ${skipped} (already existed)`);
console.log(`📊 Total keys in menu.json: ${Object.keys(menu).length}`);
