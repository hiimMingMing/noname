/**
 * Extract all keys from lib.translate in noname/library/index.js
 * Compare with existing Vietnamese translations
 */

const fs = require('fs');
const path = require('path');

// Load existing Vietnamese translations
const loadVietnameseTranslations = () => {
    const categories = ['core', 'cards', 'characters', 'modes', 'menu'];
    const translations = {};

    for (const category of categories) {
        const filePath = path.join(__dirname, '..', 'locales', 'vi-VN', `${category}.json`);
        if (fs.existsSync(filePath)) {
            const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
            // Filter out comments
            for (const key in data) {
                if (!key.startsWith('_')) {
                    translations[key] = data[key];
                }
            }
        }
    }

    return translations;
};

// Extract all keys from lib.translate object
const extractLibTranslateKeys = () => {
    const content = fs.readFileSync(path.join(__dirname, '..', 'noname', 'library', 'index.js'), 'utf-8');

    // Find the translate Proxy object
    const match = content.match(/translate\s*=\s*new Proxy\(\s*\{([\s\S]*?)\n\t\},/);

    if (!match) {
        console.error('Could not find lib.translate object');
        return [];
    }

    const objContent = match[1];
    const keys = [];

    // Extract all property keys
    const propertyRegex = /^\s*(?:["'])?([a-zA-Z0-9_]+)(?:["'])?\s*:/gm;
    let propMatch;

    while ((propMatch = propertyRegex.exec(objContent)) !== null) {
        keys.push(propMatch[1]);
    }

    return keys;
};

// Main
console.log('🔍 Extracting lib.translate keys...\n');

const libKeys = extractLibTranslateKeys();
console.log(`📊 Found ${libKeys.length} keys in lib.translate\n`);

const viTranslations = loadVietnameseTranslations();
console.log(`✅ Existing Vietnamese translations: ${Object.keys(viTranslations).length}\n`);

// Find missing
const missing = libKeys.filter(key => !(key in viTranslations));
missing.sort();

console.log(`❌ Missing translations: ${missing.length}\n`);

if (missing.length > 0) {
    console.log('Missing keys:');
    console.log('='.repeat(60));

    // Group by prefix
    const grouped = {};
    for (const key of missing) {
        const prefix = key.includes('_') ? key.split('_')[0] : 'other';
        if (!grouped[prefix]) grouped[prefix] = [];
        grouped[prefix].push(key);
    }

    for (const prefix in grouped) {
        console.log(`\n[${prefix}] (${grouped[prefix].length} keys):`);
        for (const key of grouped[prefix]) {
            console.log(`  - ${key}`);
        }
    }

    // Export to JSON
    const outputPath = path.join(__dirname, '..', 'missing_translations.json');
    fs.writeFileSync(outputPath, JSON.stringify(missing, null, 2));
    console.log(`\n📝 Full list exported to: missing_translations.json`);
}

// Statistics
console.log('\n' + '='.repeat(60));
console.log('📊 Coverage Statistics:');
console.log('='.repeat(60));
console.log(`Total lib.translate keys:  ${libKeys.length}`);
console.log(`Translated (vi-VN):        ${Object.keys(viTranslations).length}`);
console.log(`Missing:                   ${missing.length}`);
console.log(`Coverage:                  ${((Object.keys(viTranslations).length / libKeys.length) * 100).toFixed(1)}%`);
console.log('='.repeat(60));
