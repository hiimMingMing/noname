#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Combine all
const innerHTML = missing.innerHTML || [];
const other = missing.other || [];
const all = [...innerHTML, ...other];

console.log(`📦 Total remaining: ${all.length}`);

// Ultra aggressive - get EVERYTHING with Chinese
const strings = all
    .filter(s => typeof s === 'string')
    .filter(s => /[\u4e00-\u9fff]/.test(s))  // Has ANY Chinese character
    .filter(s => s.length >= 1 && s.length <= 200)  // Very permissive length
    // Only exclude obvious code patterns
    .filter(s => !s.includes('function('))
    .filter(s => !s.includes('class extends'))
    .filter(s => !s.match(/^(const|let|var|if|for|while|switch|case)\s/))
    .filter(s => !s.startsWith('//'))
    .filter(s => !s.startsWith('/*'))
    .filter(s => !s.startsWith('*'))
    // Remove duplicates
    .filter((s, i, arr) => arr.indexOf(s) === i)
    // Sort by length (shorter first - more likely to be simple terms)
    .sort((a, b) => a.length - b.length);

console.log(`📋 Ultra aggressive filtered: ${strings.length} strings`);

// Split into manageable batches
const batch1 = strings.slice(0, 400);
const batch2 = strings.slice(400, 800);
const batch3 = strings.slice(800, 1200);
const batch4 = strings.slice(1200);

// Save batches
fs.writeFileSync('ultra_batch_1.txt', batch1.join('\n'), 'utf-8');
fs.writeFileSync('ultra_batch_2.txt', batch2.join('\n'), 'utf-8');
fs.writeFileSync('ultra_batch_3.txt', batch3.join('\n'), 'utf-8');
fs.writeFileSync('ultra_batch_4.txt', batch4.join('\n'), 'utf-8');

console.log(`\n💾 Saved to 4 batch files:`);
console.log(`   ultra_batch_1.txt: ${batch1.length} strings`);
console.log(`   ultra_batch_2.txt: ${batch2.length} strings`);
console.log(`   ultra_batch_3.txt: ${batch3.length} strings`);
console.log(`   ultra_batch_4.txt: ${batch4.length} strings`);

// Show samples from batch 1
console.log(`\n📝 Sample from batch 1 (first 50):`);
batch1.slice(0, 50).forEach(s => console.log(`  ${s}`));
