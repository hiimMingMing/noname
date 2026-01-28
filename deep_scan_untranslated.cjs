#!/usr/bin/env node
const fs = require('fs');

// Load missing translations
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));
const existing = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));

// Combine all
const innerHTML = missing.innerHTML || [];
const other = missing.other || [];
const all = [...innerHTML, ...other];

console.log(`📦 Total remaining: ${all.length}`);

// Less aggressive filter - catch character names, skills, UI strings
const untranslated = all
    .filter(s => typeof s === 'string')
    .filter(s => /[\u4e00-\u9fff]/.test(s))  // Has Chinese
    .filter(s => s.length >= 1 && s.length <= 50)  // Focus on shorter strings (names, skills, UI)
    // Only filter out obvious code patterns
    .filter(s => !s.includes('\r\n'))  // Multi-line code
    .filter(s => !s.includes('\t\t'))  // Heavy indentation
    .filter(s => !s.includes('/**'))
    .filter(s => !s.includes('*/'))
    .filter(s => !s.includes('@param'))
    .filter(s => !s.includes('@type'))
    .filter(s => !s.includes('@returns'))
    .filter(s => !s.includes('function('))
    .filter(s => !s.includes('=>'))
    .filter(s => !s.includes('const '))
    .filter(s => !s.includes('return '))
    .filter(s => !s.match(/^(if|else|for|while|switch|case)\s/))
    // Keep character names and skills
    .filter(s => {
        // Already translated
        if (existing[s]) return false;

        // Single Chinese chars are likely UI
        if (s.length === 1) return true;

        // 2-4 char Chinese strings are likely names/skills
        if (s.length <= 4 && /^[\u4e00-\u9fff]+$/.test(s)) return true;

        // Character name patterns like "孙资刘放"
        if (s.length <= 8 && /^[\u4e00-\u9fff]+$/.test(s)) return true;

        // Skill names with brackets
        if (/^[\u4e00-\u9fff]+:\s*\[$/.test(s)) return true;

        // UI strings with Chinese
        if (s.length <= 20 && /[\u4e00-\u9fff]{2,}/.test(s) && !s.includes('(') && !s.includes('{')) return true;

        return false;
    })
    // Remove duplicates
    .filter((s, i, arr) => arr.indexOf(s) === i)
    // Sort by length
    .sort((a, b) => a.length - b.length);

console.log(`📋 Untranslated strings found: ${untranslated.length}`);

// Categorize
const characterNames = untranslated.filter(s => s.length <= 4 && /^[\u4e00-\u9fff]+$/.test(s));
const skillNames = untranslated.filter(s => /^[\u4e00-\u9fff]+:\s*\[$/.test(s));
const uiStrings = untranslated.filter(s => !characterNames.includes(s) && !skillNames.includes(s));

console.log(`\n📊 Breakdown:`);
console.log(`   Character names (2-4 chars): ${characterNames.length}`);
console.log(`   Skill names (with :[): ${skillNames.length}`);
console.log(`   UI strings: ${uiStrings.length}`);

// Save
fs.writeFileSync('untranslated_character_names.txt', characterNames.join('\n'), 'utf-8');
fs.writeFileSync('untranslated_skill_names.txt', skillNames.join('\n'), 'utf-8');
fs.writeFileSync('untranslated_ui_strings.txt', uiStrings.join('\n'), 'utf-8');
fs.writeFileSync('all_untranslated.txt', untranslated.join('\n'), 'utf-8');

console.log(`\n💾 Saved to files:`);
console.log(`   untranslated_character_names.txt`);
console.log(`   untranslated_skill_names.txt`);
console.log(`   untranslated_ui_strings.txt`);
console.log(`   all_untranslated.txt`);

// Show samples
console.log(`\n📝 Sample character names (first 50):`);
characterNames.slice(0, 50).forEach(s => console.log(`  ${s}`));

console.log(`\n📝 Sample skill names (first 30):`);
skillNames.slice(0, 30).forEach(s => console.log(`  ${s}`));

console.log(`\n📝 Sample UI strings (first 30):`);
uiStrings.slice(0, 30).forEach(s => console.log(`  ${s}`));
