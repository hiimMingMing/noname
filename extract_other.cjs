#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Get "other" array
const other = missing.other || [];

console.log(`📦 Total "other" strings: ${other.length}`);

// Filter translatable strings
const strings = other
    .filter(s => s.length >= 2 && s.length <= 100)  // Reasonable length
    .filter(s => !/^[a-zA-Z0-9_\-\.\/]+$/.test(s))  // Not just code/path
    .filter(s => !s.includes('function'))
    .filter(s => !s.includes('return'))
    .filter(s => !s.includes('console'))
    .filter(s => !s.startsWith('lib.'))
    .filter(s => !s.startsWith('game.'))
    .filter(s => !s.includes('window.'))
    .filter(s => !s.includes('document.'))
    .filter(s => !s.includes('typeof'))
    .filter(s => !s.includes(' = '))
    .filter(s => !s.includes('const '))
    .filter(s => !s.includes('let '))
    .filter(s => !s.includes('var '))
    .filter(s => !s.includes('=>'))
    .filter(s => !s.includes('extends'))
    .filter(s => !/^[\/\*#]/.test(s))  // Not comments
    .sort((a, b) => a.length - b.length);

console.log(`📋 Filtered to: ${strings.length} translatable strings`);

// Save
fs.writeFileSync('other_to_translate.txt', strings.join('\n'), 'utf-8');
console.log(`💾 Saved to other_to_translate.txt`);

// Show samples
console.log(`\n📝 Sample (first 40):`);
strings.slice(0, 40).forEach(s => console.log(`  ${s}`));
