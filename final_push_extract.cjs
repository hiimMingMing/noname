#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Combine all
const innerHTML = missing.innerHTML || [];
const other = missing.other || [];
const all = [...innerHTML, ...other];

console.log(`📦 Remaining strings: ${all.length}`);

// Get everything that looks translateable
const strings = all
    .filter(s => typeof s === 'string')
    .filter(s => /[\u4e00-\u9fff]/.test(s))  // Has Chinese
    .filter(s => s.length >= 1 && s.length <= 150)  // Reasonable length
    // Only exclude very obvious code
    .filter(s => !s.match(/^(const|let|var|if|for|while|switch|case|try|catch)\s/))
    .filter(s => !s.includes('function('))
    .filter(s => !s.includes('class extends'))
    .filter(s => !s.includes('new Error'))
    // Remove duplicates
    .filter((s, i, arr) => arr.indexOf(s) === i)
    // Sort by length
    .sort((a, b) => a.length - b.length);

console.log(`📋 Extracted: ${strings.length} strings`);

// Save
fs.writeFileSync('final_push.txt', strings.join('\n'), 'utf-8');
console.log(`💾 Saved to final_push.txt`);

// Show samples
console.log(`\n📝 Sample (first 80):`);
strings.slice(0, 80).forEach(s => console.log(`  ${s}`));
