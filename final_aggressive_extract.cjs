#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Combine all
const innerHTML = missing.innerHTML || [];
const other = missing.other || [];
const all = [...innerHTML, ...other];

console.log(`📦 Total remaining: ${all.length}`);

// Ultra aggressive - anything with 2+ Chinese chars
const strings = all
    .filter(s => typeof s === 'string')
    .filter(s => s.length >= 2 && s.length <= 60)  // Short strings most likely to be UI
    .filter(s => /[\u4e00-\u9fff]{2,}/.test(s))  // Has 2+ Chinese characters
    .filter(s => !s.includes('function('))
    .filter(s => !s.includes('return '))
    .filter(s => !s.includes(' = '))
    .filter(s => !s.includes('=>'))
    .filter(s => !s.includes('new '))
    .filter(s => !s.includes('class '))
    .filter(s => !s.includes('const '))
    .filter(s => !s.includes('let '))
    .filter(s => !s.includes('var '))
    // Remove duplicates
    .filter((s, i, arr) => arr.indexOf(s) === i)
    // Sort by length
    .sort((a, b) => a.length - b.length);

console.log(`📋 Ultra filtered: ${strings.length} strings`);

// Save
fs.writeFileSync('final_aggressive.txt', strings.join('\n'), 'utf-8');
console.log(`💾 Saved to final_aggressive.txt`);

// Show samples
console.log(`\n📝 Sample (first 60):`);
strings.slice(0, 60).forEach(s => console.log(`  ${s}`));
