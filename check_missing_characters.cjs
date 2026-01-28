#!/usr/bin/env node
const fs = require('fs');

const menu = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));
const all = fs.readFileSync('all_character_strings.txt', 'utf-8').split('\n').filter(s => s.trim());
const missing = all.filter(s => !menu[s.trim()]);

console.log('📊 Character Strings Analysis:');
console.log(`   Total character strings: ${all.length}`);
console.log(`   Already translated: ${all.length - missing.length}`);
console.log(`   Still missing: ${missing.length}`);
console.log(`   Coverage: ${((all.length - missing.length) / all.length * 100).toFixed(1)}%`);

fs.writeFileSync('missing_character_strings.txt', missing.join('\n'), 'utf-8');
console.log(`\n💾 Saved missing strings to missing_character_strings.txt`);

// Show samples
console.log(`\n📝 Sample missing strings (first 100):`);
missing.slice(0, 100).forEach(s => console.log(`  ${s}`));
