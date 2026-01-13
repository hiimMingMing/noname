const fs = require('fs');

console.log('🔍 Comparing found Chinese strings with existing translations...\n');

// Load scanned Chinese strings
const categorized = JSON.parse(fs.readFileSync('chinese_strings_categorized.json', 'utf-8'));

// Load existing translations
const menuVi = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));
const gameplayVi = JSON.parse(fs.readFileSync('locales/vi-VN/gameplay.json', 'utf-8'));
const coreVi = JSON.parse(fs.readFileSync('locales/vi-VN/core.json', 'utf-8'));

// Combine all existing translations
const allTranslations = { ...menuVi, ...gameplayVi, ...coreVi };

// Find missing translations
const missing = {
    alerts: [],
    confirms: [],
    prompts: [],
    innerHTML: [],
    other: []
};

console.log('📊 Translation Coverage:\n');

// Check each category
Object.keys(categorized).forEach(category => {
    const strings = categorized[category];
    const missingStrings = strings.filter(str => !allTranslations[str]);

    if (category !== 'gameLogs') {
        missing[category] = missingStrings;
        const coverage = ((strings.length - missingStrings.length) / strings.length * 100).toFixed(1);
        console.log(`   ${category}: ${strings.length - missingStrings.length}/${strings.length} translated (${coverage}%)`);
        console.log(`      Missing: ${missingStrings.length} strings`);
    }
});

// Total statistics
const totalStrings = Object.values(categorized).flat().length;
const totalMissing = Object.values(missing).flat().length;
const totalTranslated = totalStrings - totalMissing;
const coverage = (totalTranslated / totalStrings * 100).toFixed(1);

console.log(`\n📈 Total Coverage: ${totalTranslated}/${totalStrings} (${coverage}%)`);
console.log(`❌ Missing Translations: ${totalMissing}\n`);

// Save missing translations
fs.writeFileSync('missing_translations.json', JSON.stringify(missing, null, 2), 'utf-8');
console.log('✅ Missing translations saved to missing_translations.json');

// Create priority list (alerts, confirms, prompts first)
const highPriority = [
    ...missing.alerts.map(s => ({ type: 'alert', string: s })),
    ...missing.confirms.map(s => ({ type: 'confirm', string: s })),
    ...missing.prompts.map(s => ({ type: 'prompt', string: s }))
];

console.log(`\n🔴 High Priority (alerts/confirms/prompts): ${highPriority.length} strings\n`);

// Show sample of high priority missing strings
if (highPriority.length > 0) {
    console.log('Sample high priority missing strings:');
    highPriority.slice(0, 20).forEach((item, i) => {
        console.log(`   ${i+1}. [${item.type}] ${item.string}`);
    });
    if (highPriority.length > 20) {
        console.log(`   ... and ${highPriority.length - 20} more`);
    }
}

// Save high priority list
fs.writeFileSync('missing_high_priority.json', JSON.stringify(highPriority, null, 2), 'utf-8');
console.log('\n✅ High priority missing strings saved to missing_high_priority.json');
