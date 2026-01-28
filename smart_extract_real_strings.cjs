#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Combine all
const innerHTML = missing.innerHTML || [];
const other = missing.other || [];
const all = [...innerHTML, ...other];

console.log(`📦 Total remaining: ${all.length}`);

// Smart filter - only real user-facing strings
const realStrings = all
    .filter(s => typeof s === 'string')
    .filter(s => /[\u4e00-\u9fff]/.test(s))  // Has Chinese
    .filter(s => s.length >= 1 && s.length <= 100)  // Reasonable length for UI strings
    // Filter out code comments
    .filter(s => !s.includes('/**'))
    .filter(s => !s.includes('*/'))
    .filter(s => !s.includes('@param'))
    .filter(s => !s.includes('@type'))
    .filter(s => !s.includes('@returns'))
    .filter(s => !s.includes('@example'))
    .filter(s => !s.includes('@see'))
    .filter(s => !s.includes('// '))
    .filter(s => !s.startsWith('//'))
    .filter(s => !s.includes('\r\n'))  // Multi-line code snippets
    .filter(s => !s.includes('\\r\\n'))
    .filter(s => !s.includes('\t'))  // Code with tabs
    // Filter out code patterns
    .filter(s => !s.includes('function('))
    .filter(s => !s.includes('function '))
    .filter(s => !s.includes('=>'))
    .filter(s => !s.includes('const '))
    .filter(s => !s.includes('let '))
    .filter(s => !s.includes('var '))
    .filter(s => !s.includes('return '))
    .filter(s => !s.includes('if ('))
    .filter(s => !s.includes('else '))
    .filter(s => !s.includes('for ('))
    .filter(s => !s.includes('while ('))
    .filter(s => !s.includes('switch ('))
    .filter(s => !s.includes('.forEach'))
    .filter(s => !s.includes('.map'))
    .filter(s => !s.includes('.filter'))
    .filter(s => !s.includes('new Error'))
    .filter(s => !s.includes('throw '))
    .filter(s => !s.includes('console.'))
    .filter(s => !s.includes('window.'))
    .filter(s => !s.includes('document.'))
    .filter(s => !s.includes('this.'))
    .filter(s => !s.includes('game.'))
    .filter(s => !s.includes('lib.'))
    .filter(s => !s.includes('get.'))
    .filter(s => !s.includes('ui.'))
    .filter(s => !s.includes('.classList'))
    .filter(s => !s.includes('.querySelector'))
    .filter(s => !s.includes('.innerHTML'))
    .filter(s => !s.includes('.startsWith'))
    .filter(s => !s.includes('.includes'))
    .filter(s => !s.includes('typeof '))
    .filter(s => !s.includes('instanceof '))
    .filter(s => !s.includes(' = '))
    .filter(s => !s.includes(' == '))
    .filter(s => !s.includes(' === '))
    .filter(s => !s.includes('${'))  // Template literals
    .filter(s => !s.includes('class='))  // HTML class attributes
    .filter(s => !s.includes('</div>'))
    .filter(s => !s.includes('</span>'))
    .filter(s => !s.includes('<div'))
    .filter(s => !s.includes('<span'))
    // Only keep strings that look like UI text
    .filter(s => {
        // Single Chinese characters are likely UI
        if (s.length === 1) return true;
        // Pure Chinese strings are likely UI
        if (/^[\u4e00-\u9fff]+$/.test(s)) return true;
        // Chinese with simple punctuation
        if (/^[\u4e00-\u9fff，。：；！？、]+$/.test(s)) return true;
        // Character/skill names with brackets
        if (/^[\u4e00-\u9fff]+:\s*\[$/.test(s)) return true;
        // Simple mixed strings
        if (s.length <= 20 && !s.includes('(') && !s.includes('{')) return true;
        return false;
    })
    // Remove duplicates
    .filter((s, i, arr) => arr.indexOf(s) === i)
    // Sort by length
    .sort((a, b) => a.length - b.length);

console.log(`📋 Real user-facing strings: ${realStrings.length}`);

// Save
fs.writeFileSync('real_user_facing.txt', realStrings.join('\n'), 'utf-8');
console.log(`💾 Saved to real_user_facing.txt`);

// Show samples
console.log(`\n📝 Sample (first 100):`);
realStrings.slice(0, 100).forEach(s => console.log(`  ${s}`));

// Stats
console.log(`\n📊 Statistics:`);
console.log(`   Total remaining in missing.json: ${all.length}`);
console.log(`   Filtered to real UI strings: ${realStrings.length}`);
console.log(`   Filtered out (code/comments): ${all.length - realStrings.length}`);
console.log(`   Percentage of real UI: ${(realStrings.length / all.length * 100).toFixed(1)}%`);
