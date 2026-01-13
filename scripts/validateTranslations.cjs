const fs = require('fs');

// Validate all JSON files
const files = ['menu.json', 'gameplay.json', 'core.json'];
const results = {};

files.forEach(file => {
  try {
    const content = JSON.parse(fs.readFileSync(`locales/vi-VN/${file}`, 'utf-8'));
    const keys = Object.keys(content).filter(k => !k.startsWith('_comment'));
    results[file] = {
      valid: true,
      keys: keys.length,
      size: (fs.statSync(`locales/vi-VN/${file}`).size / 1024).toFixed(2) + ' KB'
    };
  } catch (err) {
    results[file] = {
      valid: false,
      error: err.message
    };
  }
});

console.log('📊 Translation Files Validation:\n');
Object.entries(results).forEach(([file, data]) => {
  if (data.valid) {
    console.log(`✅ ${file}`);
    console.log(`   Keys: ${data.keys}`);
    console.log(`   Size: ${data.size}`);
  } else {
    console.log(`❌ ${file}: ${data.error}`);
  }
});

// Calculate total
const total = Object.values(results).reduce((sum, data) => sum + (data.keys || 0), 0);
console.log(`\n📈 Total Translation Keys: ${total}`);
