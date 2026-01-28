const fs = require('fs');

const missing = fs.readFileSync('missing_character_strings.txt', 'utf-8').split('\n');
const menu = JSON.parse(fs.readFileSync('locales/vi-VN/menu.json', 'utf-8'));

// Filter for short names only
const names = missing.filter(str => {
    str = str.trim();
    if (!str) return false;
    if (menu[str]) return false;
    if (str.length > 15) return false; // Very short only - likely names
    if (str.includes('<') || str.includes('>')) return false;
    if (str.includes('=') || str.includes('{') || str.includes('}')) return false;
    if (str.includes('①') || str.includes('②') || str.includes('③')) return false;
    if (str.includes('⒈') || str.includes('⒉')) return false;
    if (str.includes('。') || str.includes('，')) return false;
    if (str.includes('【') && str.length > 6) return false;
    return /[\u4e00-\u9fff]/.test(str);
});

console.log(`📊 Found ${names.length} very short names (<=15 chars)`);

// Save next 1000 for batch 5-14 (100 each)
for (let i = 0; i < 10; i++) {
    const start = i * 100;
    const end = start + 100;
    const batch = names.slice(start, end);

    if (batch.length > 0) {
        fs.writeFileSync(`batch_${i+5}_names.txt`, batch.join('\n'), 'utf-8');
        console.log(`💾 Batch ${i+5}: ${batch.length} names`);
    }
}

console.log(`\n📝 Sample from Batch 5:`);
names.slice(0, 30).forEach(x => console.log(`   ${x}`));
