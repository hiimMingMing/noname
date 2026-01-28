#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

// Find all translate.js files in character folders
const translateFiles = [
    'character/standard/translate.js',
    'character/yijiang/translate.js',
    'character/refresh/translate.js',
    'character/sp/translate.js',
    'character/sp2/translate.js',
    'character/tw/translate.js',
    'character/mobile/translate.js',
    'character/offline/translate.js',
    'character/clan/translate.js',
    'character/extra/translate.js',
    'character/diy/translate.js',
    'character/key/translate.js',
    'character/jsrg/translate.js',
    'character/sb/translate.js',
    'character/huicui/translate.js',
    'character/onlyOL/translate.js',
    'character/bingshi/translate.js',
    'character/collab/translate.js',
    'character/shenhua/translate.js',
    'character/shiji/translate.js',
    'character/sixiang/translate.js',
    'character/sxrm/translate.js',
    'character/xianding/translate.js',
    'character/old/translate.js',
    'character/yingbian/translate.js',
    'character/newjiang/translate.js',
];

console.log(`📦 Extracting from ${translateFiles.length} character files...`);

const allTranslations = {};
let totalKeys = 0;
let filesProcessed = 0;

for (const file of translateFiles) {
    try {
        const content = fs.readFileSync(file, 'utf-8');

        // Extract the translates object
        const match = content.match(/const translates = \{([\s\S]*?)\n\}/);
        if (!match) {
            console.log(`⚠️  No translates found in ${file}`);
            continue;
        }

        const translatesContent = match[1];

        // Parse key-value pairs
        const lines = translatesContent.split('\n');
        for (const line of lines) {
            // Match pattern: key: "value",
            const lineMatch = line.match(/^\s*([a-zA-Z0-9_]+):\s*"([^"]+)",?\s*$/);
            if (lineMatch) {
                const [, key, value] = lineMatch;
                // Only store Chinese character names and skills
                if (/[\u4e00-\u9fff]/.test(value)) {
                    allTranslations[value] = value; // Will translate later
                    totalKeys++;
                }
            }
        }

        filesProcessed++;
    } catch (e) {
        console.log(`❌ Error reading ${file}: ${e.message}`);
    }
}

console.log(`\n✅ Processed ${filesProcessed} files`);
console.log(`📊 Found ${totalKeys} unique Chinese strings`);

// Get unique strings
const uniqueStrings = [...new Set(Object.keys(allTranslations))];
console.log(`📋 Unique strings: ${uniqueStrings.length}`);

// Categorize
const characterNames = uniqueStrings.filter(s => s.length <= 6 && !/[：，。！？、]/.test(s) && !s.includes('技'));
const skillNames = uniqueStrings.filter(s => s.length <= 6 && !/[：，。！？、]/.test(s) && !characterNames.includes(s));
const skillDescriptions = uniqueStrings.filter(s => s.length > 6 || /[：，。！？、]/.test(s));

console.log(`\n📊 Categories:`);
console.log(`   Character names: ${characterNames.length}`);
console.log(`   Skill names: ${skillNames.length}`);
console.log(`   Skill descriptions: ${skillDescriptions.length}`);

// Save
fs.writeFileSync('all_character_names.txt', characterNames.sort().join('\n'), 'utf-8');
fs.writeFileSync('all_skill_names.txt', skillNames.sort().join('\n'), 'utf-8');
fs.writeFileSync('all_skill_descriptions.txt', skillDescriptions.join('\n'), 'utf-8');
fs.writeFileSync('all_character_strings.txt', uniqueStrings.sort().join('\n'), 'utf-8');

console.log(`\n💾 Saved to:`);
console.log(`   all_character_names.txt (${characterNames.length} names)`);
console.log(`   all_skill_names.txt (${skillNames.length} skills)`);
console.log(`   all_skill_descriptions.txt (${skillDescriptions.length} descriptions)`);
console.log(`   all_character_strings.txt (${uniqueStrings.length} total)`);

// Show samples
console.log(`\n📝 Sample character names (first 50):`);
characterNames.slice(0, 50).forEach(s => console.log(`  ${s}`));

console.log(`\n📝 Sample skill names (first 30):`);
skillNames.slice(0, 30).forEach(s => console.log(`  ${s}`));
