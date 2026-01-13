const fs = require('fs');
const path = require('path');

// Function to extract Chinese strings from JS files
function extractChineseStrings(content, filePath) {
    const strings = new Set();

    // Match strings in quotes containing Chinese characters
    const patterns = [
        /"([^"]*[\u4e00-\u9fff][^"]*)"/g,  // Double quoted strings
        /'([^']*[\u4e00-\u9fff][^']*)'/g,  // Single quoted strings
        /`([^`]*[\u4e00-\u9fff][^`]*)`/g,  // Template literals
    ];

    patterns.forEach(pattern => {
        let match;
        while ((match = pattern.exec(content)) !== null) {
            const str = match[1].trim();
            if (str && str.length > 0 && /[\u4e00-\u9fff]/.test(str)) {
                // Filter out comments and code-like patterns
                if (!str.startsWith('//') &&
                    !str.startsWith('/*') &&
                    !str.includes('function') &&
                    !str.includes('return ') &&
                    !str.includes('import ') &&
                    !str.startsWith('.') &&
                    !str.startsWith('#')) {
                    strings.add(str);
                }
            }
        }
    });

    return Array.from(strings);
}

// Recursively scan directory
function scanDirectory(dir, results = {}, baseDir = dir) {
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            // Skip node_modules, .git, etc.
            if (!file.startsWith('.') && file !== 'node_modules' && file !== 'dist' && file !== 'locales') {
                scanDirectory(filePath, results, baseDir);
            }
        } else if (file.endsWith('.js') || file.endsWith('.ts') || file.endsWith('.cts')) {
            try {
                const content = fs.readFileSync(filePath, 'utf-8');
                const strings = extractChineseStrings(content, filePath);
                if (strings.length > 0) {
                    const relPath = path.relative(baseDir, filePath).replace(/\\/g, '/');
                    results[relPath] = strings;
                }
            } catch (err) {
                console.error(`Error reading ${filePath}: ${err.message}`);
            }
        }
    });

    return results;
}

console.log('🔍 Scanning noname/ directory for hardcoded Chinese strings...\n');
const results = scanDirectory('noname');

// Count total strings
let totalStrings = 0;
let totalFiles = 0;
const allStrings = new Set();

Object.values(results).forEach(strings => {
    totalStrings += strings.length;
    totalFiles++;
    strings.forEach(s => allStrings.add(s));
});

console.log(`📊 Found ${totalStrings} Chinese string occurrences in ${totalFiles} files`);
console.log(`📊 Unique Chinese strings: ${allStrings.size}\n`);

// Show top 15 files with most Chinese strings
const sorted = Object.entries(results).sort((a, b) => b[1].length - a[1].length).slice(0, 15);

console.log('📁 Top 15 files with most Chinese strings:\n');
sorted.forEach(([file, strings], i) => {
    console.log(`${i+1}. ${file} (${strings.length} strings)`);
});

// Save full results to file
const outputPath = 'chinese_strings_scan.json';
fs.writeFileSync(outputPath, JSON.stringify(results, null, 2), 'utf-8');
console.log(`\n✅ Full results saved to ${outputPath}`);

// Save unique strings list
const uniqueStringsPath = 'chinese_strings_unique.txt';
const sortedUniqueStrings = Array.from(allStrings).sort();
fs.writeFileSync(uniqueStringsPath, sortedUniqueStrings.join('\n'), 'utf-8');
console.log(`✅ Unique strings saved to ${uniqueStringsPath}`);

// Group by category (alert, confirm, prompt, game.log, etc.)
const categorized = {
    alerts: [],
    confirms: [],
    prompts: [],
    gameLogs: [],
    innerHTML: [],
    other: []
};

Object.entries(results).forEach(([file, strings]) => {
    const content = fs.readFileSync(path.join('noname', file), 'utf-8');
    strings.forEach(str => {
        if (content.includes(`alert("${str}")`)) {
            categorized.alerts.push(str);
        } else if (content.includes(`confirm("${str}")`)) {
            categorized.confirms.push(str);
        } else if (content.includes(`prompt("${str}")`)) {
            categorized.prompts.push(str);
        } else if (content.includes(`game.log("${str}")`)) {
            categorized.gameLogs.push(str);
        } else if (content.includes(`innerHTML`) && content.includes(`"${str}"`)) {
            categorized.innerHTML.push(str);
        } else {
            categorized.other.push(str);
        }
    });
});

console.log('\n📂 Strings by category:');
console.log(`   alerts: ${new Set(categorized.alerts).size} unique`);
console.log(`   confirms: ${new Set(categorized.confirms).size} unique`);
console.log(`   prompts: ${new Set(categorized.prompts).size} unique`);
console.log(`   game.log: ${new Set(categorized.gameLogs).size} unique`);
console.log(`   innerHTML: ${new Set(categorized.innerHTML).size} unique`);
console.log(`   other: ${new Set(categorized.other).size} unique`);

// Save categorized results
fs.writeFileSync('chinese_strings_categorized.json', JSON.stringify({
    alerts: Array.from(new Set(categorized.alerts)),
    confirms: Array.from(new Set(categorized.confirms)),
    prompts: Array.from(new Set(categorized.prompts)),
    gameLogs: Array.from(new Set(categorized.gameLogs)),
    innerHTML: Array.from(new Set(categorized.innerHTML)),
    other: Array.from(new Set(categorized.other))
}, null, 2), 'utf-8');
console.log('✅ Categorized strings saved to chinese_strings_categorized.json');
