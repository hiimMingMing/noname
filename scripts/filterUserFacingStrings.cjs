const fs = require('fs');

// Load missing strings
const missing = JSON.parse(fs.readFileSync('missing_translations.json', 'utf-8'));

// Filter function to identify real user-facing strings
function isUserFacingString(str) {
    // Exclude code/technical patterns
    const excludePatterns = [
        /^\/\//,                    // Comments starting with //
        /^\/\*/,                    // Comments starting with /*
        /^\*/,                      // Comments starting with *
        /@param/i,                  // JSDoc parameters
        /@returns/i,                // JSDoc returns
        /@example/i,                // JSDoc examples
        /function\s*\(/,            // Function declarations
        /return\s+/,                // Return statements
        /const\s+/,                 // Const declarations
        /let\s+/,                   // Let declarations
        /var\s+/,                   // Var declarations
        /import\s+/,                // Import statements
        /export\s+/,                // Export statements
        /=>/,                       // Arrow functions
        /console\./,                // Console logs
        /^\s*\{/,                   // Object literals
        /^\s*\}/,                   // Closing braces
        /^\s*\[/,                   // Array literals
        /^\s*\]/,                   // Closing brackets
        /^\s*\(/,                   // Opening parenthesis
        /^\s*\)/,                   // Closing parenthesis
        /^\s*;/,                    // Semicolons
        /^\s*,/,                    // Commas
        /http:\/\//i,               // URLs
        /https:\/\//i,              // Secure URLs
        /\.js$/i,                   // JS file references
        /\.ts$/i,                   // TS file references
        /\.css$/i,                  // CSS file references
        /\.json$/i,                 // JSON file references
        /\.md$/i,                   // Markdown file references
        /^[\s\t\n\r]*$/,           // Empty or whitespace only
        /^[a-zA-Z_$][a-zA-Z0-9_$]*$/, // Variable names (English only)
        /^\d+$/,                    // Numbers only
        /^[\.,:;!\?]+$/,           // Punctuation only
        /game\./,                   // Game object references
        /lib\./,                    // Lib object references
        /ui\./,                     // UI object references
        /get\./,                    // Get object references
        /_status\./,                // Status object references
        /Element$/,                 // DOM element references
        /element\./i,               // Element references
        /style\./,                  // Style references
        /classList\./,              // ClassList references
        /innerHTML/,                // innerHTML references
        /setAttribute/,             // setAttribute calls
        /getAttribute/,             // getAttribute calls
        /addEventListener/,         // Event listener calls
        /removeEventListener/,      // Event listener removal
        /querySelector/,            // Query selector calls
        /getElementById/,           // GetElementById calls
        /createElement/,            // Create element calls
        /appendChild/,              // AppendChild calls
        /removeChild/,              // RemoveChild calls
        /^[\u4e00-\u9fff][\u4e00-\u9fff]*[的了吗呢啊]$/,  // Single character + particle
        /^\s*\*\s+/,               // Bullet points in comments
        /^\s*-\s+/,                // Dash bullet points
        /^@/,                       // JSDoc tags
        /typeof\s+/,                // Typeof operator
        /instanceof\s+/,            // Instanceof operator
        /new\s+/,                   // New operator
        /this\./,                   // This references
        /prototype\./,              // Prototype references
        /^Error:/i,                 // Error messages (technical)
        /^Warning:/i,               // Warning messages (technical)
        /^Debug:/i,                 // Debug messages
        /^\[.*\]$/,                // Bracketed technical strings
        /^undefined$/,              // Undefined keyword
        /^null$/,                   // Null keyword
        /^true$/,                   // True keyword
        /^false$/,                  // False keyword
        /^\d+px$/,                  // CSS pixel values
        /^#[0-9a-fA-F]{3,8}$/,     // Color codes
        /^rgb\(/,                   // RGB colors
        /^rgba\(/,                  // RGBA colors
        /^\./,                      // Class selectors
        /^#/,                       // ID selectors
        /^<[^>]+>$/,               // HTML tags
        /喵$/,                      // Debug/cute messages (already translated)
    ];

    // Check if string matches any exclude pattern
    if (excludePatterns.some(pattern => pattern.test(str))) {
        return false;
    }

    // Exclude very short strings that are likely fragments
    if (str.length < 2) {
        return false;
    }

    // Exclude strings with only one Chinese character (likely fragments)
    const chineseChars = str.match(/[\u4e00-\u9fff]/g);
    if (chineseChars && chineseChars.length === 1 && str.length < 5) {
        return false;
    }

    return true;
}

// Filter innerHTML strings
console.log('🔍 Filtering innerHTML strings...');
const innerHTMLUserFacing = missing.innerHTML.filter(isUserFacingString);
console.log(`   Found ${innerHTMLUserFacing.length} user-facing strings (from ${missing.innerHTML.length} total)`);

// Filter other strings
console.log('🔍 Filtering other strings...');
const otherUserFacing = missing.other.filter(isUserFacingString);
console.log(`   Found ${otherUserFacing.length} user-facing strings (from ${missing.other.length} total)`);

// Combine and deduplicate
const allUserFacing = [...new Set([...innerHTMLUserFacing, ...otherUserFacing])];
console.log(`\n📊 Total unique user-facing strings: ${allUserFacing.length}`);

// Sort by length (shorter strings first - usually more common)
allUserFacing.sort((a, b) => a.length - b.length);

// Save filtered strings
fs.writeFileSync('user_facing_strings.txt', allUserFacing.join('\n'), 'utf-8');
console.log(`✅ Saved to user_facing_strings.txt`);

// Show samples
console.log('\n📝 Sample strings (first 50):');
allUserFacing.slice(0, 50).forEach((str, i) => {
    console.log(`  ${i+1}. ${str}`);
});

console.log(`\n... and ${allUserFacing.length - 50} more strings`);

// Split into batches for translation
const batchSize = 500;
const batches = [];
for (let i = 0; i < allUserFacing.length; i += batchSize) {
    batches.push(allUserFacing.slice(i, i + batchSize));
}

console.log(`\n📦 Split into ${batches.length} batches of ${batchSize} strings each`);

// Save batch files
batches.forEach((batch, i) => {
    fs.writeFileSync(`user_facing_batch_${i+1}.txt`, batch.join('\n'), 'utf-8');
});
console.log(`✅ Saved ${batches.length} batch files (user_facing_batch_1.txt, etc.)`);
