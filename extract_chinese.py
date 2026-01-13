import re
import json

# Read the file
with open('all_missing_strings.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match Chinese characters
chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')

# Split by lines
lines = content.split('\n')

chinese_strings = set()
for line in lines:
    # Skip code lines
    if any(x in line for x in ['function', 'const', 'let', 'var', 'return', 'if (', ') {', '} else', '//', '/*', '*/', '@param', '@returns', 'class ', '.forEach', '.map', '.filter', 'new Map', 'import ', 'export ', 'throw new', '===', '!==', '=>', '&&', '||']):
        continue

    # Skip lines with excessive punctuation (likely code)
    if line.count('(') > 2 or line.count(')') > 2 or line.count('{') > 1 or line.count('}') > 1:
        continue

    # Skip very short lines
    if len(line.strip()) < 2:
        continue

    # Find Chinese text
    matches = chinese_pattern.findall(line)
    if matches:
        # Join consecutive Chinese segments
        chinese_text = ''.join(matches)
        # Only add if substantial (more than 1 char) and not too long (< 100 chars)
        if 1 < len(chinese_text) < 100:
            chinese_strings.add(chinese_text)

# Sort and save
chinese_list = sorted(list(chinese_strings))

print(f"Found {len(chinese_list)} unique Chinese strings")

# Save to file
with open('filtered_chinese_strings.txt', 'w', encoding='utf-8') as f:
    for s in chinese_list:
        f.write(s + '\n')

print("Saved to filtered_chinese_strings.txt")
