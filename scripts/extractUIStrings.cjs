const fs = require('fs');
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Filter innerHTML strings to get only actual UI text (not code/comments)
const shortStrings = missing.innerHTML.filter(s => {
    // Filter out code-like patterns
    return s.length > 1 &&
           s.length <= 50 &&
           !s.includes('*') &&
           !s.includes('@') &&
           !s.includes('game.') &&
           !s.includes('lib.') &&
           !s.includes('function') &&
           !s.includes('return') &&
           !s.includes('const ') &&
           !s.includes('let ') &&
           !s.includes('var ') &&
           !s.includes('=>') &&
           !s.includes('import') &&
           !s.includes('export') &&
           !s.startsWith('/') &&
           !s.startsWith('.') &&
           !s.includes('http') &&
           !s.includes('github') &&
           !s.includes('Element') &&
           s.trim().length > 0;
});

console.log(`📊 Filtered UI strings: ${shortStrings.length}`);

// Common UI terms that should be translated
const commonUI = shortStrings.filter(s =>
    s.length <= 20 &&
    !s.includes('(') &&
    !s.includes(')') &&
    !s.includes('<') &&
    !s.includes('>')
);

console.log(`\n📊 Clean UI strings (<=20 chars, no HTML): ${commonUI.length}\n`);

// Sample
console.log('Top 100 common UI strings:\n');
commonUI.slice(0, 100).forEach((str, i) => {
  console.log(`  ${str}`);
});

fs.writeFileSync('innerHTML_ui_clean.txt', commonUI.join('\n'), 'utf-8');
console.log(`\n✅ Saved ${commonUI.length} clean UI strings to innerHTML_ui_clean.txt`);
