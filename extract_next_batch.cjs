#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Combine innerHTML and other
const innerHTML = missing.innerHTML || [];
const other = missing.other || [];
const all = [...innerHTML, ...other];

console.log(`📦 Total remaining strings: ${all.length}`);
console.log(`   innerHTML: ${innerHTML.length}`);
console.log(`   other: ${other.length}`);

// More aggressive filtering - focus on short, likely user-facing strings
const strings = all
    .filter(s => typeof s === 'string')
    .filter(s => s.length >= 2 && s.length <= 80)  // Short to medium
    .filter(s => /[\u4e00-\u9fff]{2,}/.test(s))  // Has Chinese characters
    .filter(s => !s.includes('function'))
    .filter(s => !s.includes('return'))
    .filter(s => !s.includes('console'))
    .filter(s => !s.includes('window.'))
    .filter(s => !s.includes('document.'))
    .filter(s => !s.includes(' = '))
    .filter(s => !s.includes('=>'))
    .filter(s => !s.includes('typeof'))
    .filter(s => !s.includes('instanceof'))
    .filter(s => !s.includes('extends'))
    .filter(s => !s.includes('this.'))
    .filter(s => !s.includes('super.'))
    .filter(s => !s.startsWith('//'))
    .filter(s => !s.startsWith('/*'))
    .filter(s => !s.startsWith('*'))
    .filter(s => !s.startsWith('@'))
    .filter(s => !s.startsWith('#'))
    // Remove duplicates
    .filter((s, i, arr) => arr.indexOf(s) === i)
    .sort((a, b) => a.length - b.length);

console.log(`📋 Filtered to: ${strings.length} translatable strings`);

// Save
fs.writeFileSync('next_batch_to_translate.txt', strings.join('\n'), 'utf-8');
console.log(`💾 Saved to next_batch_to_translate.txt`);

// Show samples
console.log(`\n📝 Sample (first 50):`);
strings.slice(0, 50).forEach(s => console.log(`  ${s}`));
