#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Get innerHTML array
const innerHTML = missing.innerHTML || [];

console.log(`📦 Total innerHTML strings: ${innerHTML.length}`);

// Extract just the strings (they're already strings, not objects), sort by length (shorter first)
const strings = innerHTML
    .filter(s => s.length >= 2 && s.length <= 100)  // Reasonable length
    .filter(s => !/^[a-zA-Z0-9_\-\.\/]+$/.test(s))  // Not just code/path
    .filter(s => !s.includes('function'))
    .filter(s => !s.includes('return'))
    .filter(s => !s.includes('console'))
    .filter(s => !s.startsWith('lib.'))
    .filter(s => !s.startsWith('game.'))
    .sort((a, b) => a.length - b.length);

console.log(`📋 Filtered to: ${strings.length} translatable strings`);

// Save
fs.writeFileSync('innerHTML_to_translate.txt', strings.join('\n'), 'utf-8');
console.log(`💾 Saved to innerHTML_to_translate.txt`);

// Show samples
console.log(`\n📝 Sample (first 30):`);
strings.slice(0, 30).forEach(s => console.log(`  ${s}`));
