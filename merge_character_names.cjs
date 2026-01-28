#!/usr/bin/env node
const fs = require('fs');

const menu = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));
const chars = JSON.parse(fs.readFileSync('character_names_translated.json', 'utf-8'));

console.log(`📦 Loading...`);
console.log(`   Menu: ${Object.keys(menu).length} keys`);
console.log(`   Character names: ${Object.keys(chars).length} keys`);

let added = 0;
let skipped = 0;

for (const [cn, vi] of Object.entries(chars)) {
    if (!menu[cn]) {
        menu[cn] = vi;
        added++;
    } else {
        skipped++;
    }
}

fs.writeFileSync('locales/vi-VN/menu.json', JSON.stringify(menu, null, 2), 'utf-8');

console.log(`\n✅ Added: ${added} character names`);
console.log(`⏭️  Skipped: ${skipped} (already existed)`);
console.log(`📊 Total keys: ${Object.keys(menu).length}`);
