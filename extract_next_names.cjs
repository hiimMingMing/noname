#!/usr/bin/env node
const fs = require('fs');

const missing = fs.readFileSync('missing_character_strings.txt', 'utf-8').split('\n');
const menu = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));

// Filter for character/skill names only (not long descriptions)
const names = missing.filter(str => {
    str = str.trim();
    if (!str) return false;
    if (menu[str]) return false; // Already translated

    // Skip long descriptions (>40 chars usually means it's a description)
    if (str.length > 40) return false;

    // Skip HTML tags
    if (str.includes('<') || str.includes('>')) return false;

    // Skip JavaScript code and special chars
    if (str.includes('=') || str.includes('{') || str.includes('}')) return false;
    if (str.includes('①') || str.includes('②') || str.includes('③')) return false;
    if (str.includes('⒈') || str.includes('⒉') || str.includes('⒊')) return false;
    if (str.includes('【') && str.length > 10) return false; // Long card names

    // Skip sentences (contains periods or commas in middle)
    if (str.includes('。') || str.includes('，')) return false;

    return true;
});

console.log(`📊 Found ${names.length} short character/skill names`);

// Take next 300 for batch 3
const batch3 = names.slice(0, 300);

fs.writeFileSync('remaining_names_batch3.txt', batch3.join('\n'), 'utf-8');

console.log(`💾 Saved ${batch3.length} names to remaining_names_batch3.txt`);
console.log(`\n📝 Sample:`);
batch3.slice(0, 20).forEach(name => console.log(`   ${name}`));
