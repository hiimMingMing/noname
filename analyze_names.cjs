const fs = require('fs');

const all = fs.readFileSync('all_character_skill_names.txt', 'utf-8')
    .split('\n')
    .filter(x => {
        x = x.trim();
        if (!x) return false;
        if (x.length > 40) return false;
        if (x.includes('①') || x.includes('②') || x.includes('③')) return false;
        if (x.includes('。') || x.includes('，')) return false;
        if (x.includes('<') || x.includes('>')) return false;
        if (x.includes('=') || x.includes('{') || x.includes('}')) return false;
        if (x.includes('⒈') || x.includes('⒉')) return false;
        return /[\u4e00-\u9fff]/.test(x);
    });

console.log('Total clean character/skill names:', all.length);

// Save next 500 for batch 4
const batch4 = all.slice(300, 800);
fs.writeFileSync('remaining_names_batch4.txt', batch4.join('\n'), 'utf-8');

console.log(`\n💾 Saved ${batch4.length} names to remaining_names_batch4.txt`);
console.log('\n📝 Sample:');
batch4.slice(0, 30).forEach(x => console.log(`   ${x}`));
