/**
 * Script to find missing translations in Vietnamese locale
 * Extracts all lib.translate keys from codebase and compares with vi-VN translations
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

// Find all lib.translate references in source files
const findTranslateKeys = (dir, keys = new Set()) => {
    const files = fs.readdirSync(dir);

    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
            // Skip node_modules, .git, etc.
            if (!['node_modules', '.git', 'dist', 'locales'].includes(file)) {
                findTranslateKeys(fullPath, keys);
            }
        } else if (file.endsWith('.js') || file.endsWith('.ts')) {
            const content = fs.readFileSync(fullPath, 'utf-8');

            // Pattern 1: lib.translate.key or lib.translate['key']
            const pattern1 = /lib\.translate\.([a-zA-Z0-9_]+)/g;
            const pattern2 = /lib\.translate\[['"]([^'"]+)['"]\]/g;

            let match;
            while ((match = pattern1.exec(content)) !== null) {
                keys.add(match[1]);
            }
            while ((match = pattern2.exec(content)) !== null) {
                keys.add(match[1]);
            }
        }
    }

    return keys;
};

// Main execution
console.log('🔍 Scanning codebase for translation keys...\n');

const projectRoot = path.join(__dirname, '..');
const allKeys = findTranslateKeys(path.join(projectRoot, 'noname'));

console.log(`📊 Found ${allKeys.size} translation keys in codebase\n`);

const viTranslations = loadVietnameseTranslations();
console.log(`✅ Existing Vietnamese translations: ${Object.keys(viTranslations).length}\n`);

// Find missing translations
const missing = Array.from(allKeys).filter(key => !(key in viTranslations));
missing.sort();

console.log(`❌ Missing translations: ${missing.length}\n`);

if (missing.length > 0) {
    console.log('Missing keys (first 100):');
    console.log('='.repeat(60));

    // Group by prefix for easier categorization
    const grouped = {};
    for (const key of missing.slice(0, 100)) {
        const prefix = key.split('_')[0];
        if (!grouped[prefix]) grouped[prefix] = [];
        grouped[prefix].push(key);
    }

    for (const prefix in grouped) {
        console.log(`\n[${prefix}] (${grouped[prefix].length} keys):`);
        for (const key of grouped[prefix].slice(0, 20)) {
            console.log(`  - ${key}`);
        }
        if (grouped[prefix].length > 20) {
            console.log(`  ... and ${grouped[prefix].length - 20} more`);
        }
    }

    // Export to file
    const outputPath = path.join(projectRoot, 'missing_translations.txt');
    fs.writeFileSync(outputPath, missing.join('\n'));
    console.log(`\n📝 Full list exported to: missing_translations.txt`);
}

// Statistics
console.log('\n' + '='.repeat(60));
console.log('📊 Coverage Statistics:');
console.log('='.repeat(60));
console.log(`Total keys found:          ${allKeys.size}`);
console.log(`Translated (vi-VN):        ${Object.keys(viTranslations).length}`);
console.log(`Missing:                   ${missing.length}`);
console.log(`Coverage:                  ${((Object.keys(viTranslations).length / allKeys.size) * 100).toFixed(1)}%`);
console.log('='.repeat(60));
