#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

// Extract all character names from translate.js files
const characterDir = 'character';
const allNames = new Map();

function extractFromFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const match = content.match(/const translates = \{([\s\S]*?)\n\}/);

    if (!match) return;

    const lines = match[1].split('\n');
    for (const line of lines) {
        const lineMatch = line.match(/^\s*([a-zA-Z0-9_]+):\s*"([^"]+)",?\s*$/);
        if (lineMatch) {
            const [, key, value] = lineMatch;
            // Skip skill descriptions (containing _info)
            if (!key.includes('_info') && /[\u4e00-\u9fff]/.test(value)) {
                // Character names and skills only
                allNames.set(value, value); // Will translate later
            }
        }
    }
}

// Scan all character folders
function scanDir(dir) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
            const translatePath = path.join(fullPath, 'translate.js');
            if (fs.existsSync(translatePath)) {
                console.log(`📖 Reading: ${translatePath}`);
                extractFromFile(translatePath);
            }
        }
    }
}

scanDir(characterDir);

console.log(`\n📊 Extracted ${allNames.size} unique character/skill names from translate.js files`);

// Save all names
const namesList = Array.from(allNames.keys()).sort();
fs.writeFileSync('all_character_skill_names.txt', namesList.join('\n'), 'utf-8');

console.log(`💾 Saved to all_character_skill_names.txt`);
console.log(`\n📝 Sample (first 30):`);
namesList.slice(0, 30).forEach(name => console.log(`   ${name}`));
