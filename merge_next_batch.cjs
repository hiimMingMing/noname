#!/usr/bin/env node
const fs = require('fs');

// Load files
const menuPath = 'locales/vi-VN/menu.json';
const nextPath = 'next_batch_translated.json';

const menu = JSON.parse(fs.readFileSync(menuPath, 'utf-8'));
const next = JSON.parse(fs.readFileSync(nextPath, 'utf-8'));

console.log(`📦 Loading translations...`);
console.log(`   Menu: ${Object.keys(menu).length} keys`);
console.log(`   Next batch: ${Object.keys(next).length} keys`);

// Merge
let added = 0;
let skipped = 0;

for (const [cn, vi] of Object.entries(next)) {
    if (!menu[cn]) {
        menu[cn] = vi;
        added++;
    } else {
        skipped++;
    }
}

console.log(`\n✅ Added: ${added} new translations`);
console.log(`⏭️  Skipped: ${skipped} existing translations`);

// Save
fs.writeFileSync(menuPath, JSON.stringify(menu, null, 2), 'utf-8');
console.log(`\n💾 Saved to ${menuPath}`);
console.log(`📊 Total keys: ${Object.keys(menu).length}`);
