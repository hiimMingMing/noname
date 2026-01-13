#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge all translations into final Vietnamese locale files
"""

import json
import os

def load_json(filename):
    """Load JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_json(filename, data):
    """Save JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent='\t')

# Load all translation sources
print("Loading translations...")

# 1. Load existing translations
existing_menu = load_json('locales/vi-VN/menu.json')
existing_gameplay = load_json('locales/vi-VN/gameplay.json')
existing_core = load_json('locales/vi-VN/core.json')

print(f"Existing menu.json: {len(existing_menu)} entries")
print(f"Existing gameplay.json: {len(existing_gameplay)} entries")
print(f"Existing core.json: {len(existing_core)} entries")

# 2. Load our generated translations
ui_translations = load_json('ui_translations_final.json')
gameplay_translations = load_json('gameplay_translations_final.json')
final_batch = load_json('final_comprehensive_batch.json')

print(f"\nOur translations:")
print(f"UI translations: {len(ui_translations)} entries")
print(f"Gameplay translations: {len(gameplay_translations)} entries")
print(f"Final batch: {len(final_batch)} entries")

# 3. Merge all translations
all_translations = {}

# Start with existing
all_translations.update(existing_menu)
all_translations.update(existing_gameplay)
all_translations.update(existing_core)

# Add our new translations
all_translations.update(ui_translations)
all_translations.update(gameplay_translations)
all_translations.update(final_batch)

print(f"\nTotal merged translations: {len(all_translations)} entries")

# 4. Split into categories for better organization

# Menu-related (UI, settings, options)
menu_keywords = [
    '设置', '选项', '模式', '启用', '开启', '关闭', '显示', '隐藏',
    '菜单', '按钮', '主题', '音效', '背景', '皮肤', '字体', '颜色',
    '导入', '导出', '下载', '删除', '创建', '编辑', '保存', '加载',
    '房间', '扩展', '素材', '录像', '回放', '拖拽', '点击', '右键',
    '人数', '人', '局', '位', '页', '文件', '图片', '音频'
]

# Gameplay-related (cards, skills, combat)
gameplay_keywords = [
    '武将', '技能', '主公', '忠臣', '反贼', '内奸', '体力', '手牌',
    '装备', '判定', '伤害', '回合', '阶段', '摸牌', '弃牌', '出牌',
    '杀', '闪', '桃', '锦囊', '拼点', '距离', '濒死', '阵亡',
    '复活', '连环', '翻面', '目标', '触发', '发动', '使用', '打出',
    '获得', '失去', '弃置', '展示', '亮出'
]

# Core-related (phases, states, actions)
core_keywords = [
    '准备', '判定', '摸牌', '出牌', '弃牌', '结束', '阶段',
    '锁定技', '限定技', '觉醒技', '主公技', '主将技', '副将技',
    '转换技', '阵法技', '隐匿技', '使命技', '君主技', '宗族技',
    'phase', '_', '势力', '身份'
]

menu_dict = {}
gameplay_dict = {}
core_dict = {}
other_dict = {}

for chinese, vietnamese in all_translations.items():
    # Skip comments and metadata
    if chinese.startswith('_'):
        if 'menu' in chinese.lower():
            menu_dict[chinese] = vietnamese
        elif 'gameplay' in chinese.lower():
            gameplay_dict[chinese] = vietnamese
        else:
            core_dict[chinese] = vietnamese
        continue

    # Categorize by keywords
    is_menu = any(kw in chinese for kw in menu_keywords)
    is_gameplay = any(kw in chinese for kw in gameplay_keywords)
    is_core = any(kw in chinese for kw in core_keywords)

    if is_menu:
        menu_dict[chinese] = vietnamese
    elif is_gameplay:
        gameplay_dict[chinese] = vietnamese
    elif is_core:
        core_dict[chinese] = vietnamese
    else:
        # Default to menu for short strings
        if len(chinese) < 10:
            menu_dict[chinese] = vietnamese
        else:
            other_dict[chinese] = vietnamese

# Merge other_dict into menu_dict
menu_dict.update(other_dict)

print(f"\nCategorized:")
print(f"Menu: {len(menu_dict)} entries")
print(f"Gameplay: {len(gameplay_dict)} entries")
print(f"Core: {len(core_dict)} entries")

# 5. Keep existing metadata and structure
final_menu = dict(existing_menu)
final_menu.update(menu_dict)

final_gameplay = dict(existing_gameplay)
final_gameplay.update(gameplay_dict)

final_core = dict(existing_core)
final_core.update(core_dict)

# 6. Save final files
print("\nSaving final files...")

# Backup originals first
if os.path.exists('locales/vi-VN/menu.json'):
    os.rename('locales/vi-VN/menu.json', 'locales/vi-VN/menu.json.backup')
if os.path.exists('locales/vi-VN/gameplay.json'):
    os.rename('locales/vi-VN/gameplay.json', 'locales/vi-VN/gameplay.json.backup')
if os.path.exists('locales/vi-VN/core.json'):
    os.rename('locales/vi-VN/core.json', 'locales/vi-VN/core.json.backup')

# Save new files
save_json('locales/vi-VN/menu.json', final_menu)
save_json('locales/vi-VN/gameplay.json', final_gameplay)
save_json('locales/vi-VN/core.json', final_core)

# Also create a master combined file
master_dict = {}
master_dict.update(final_menu)
master_dict.update(final_gameplay)
master_dict.update(final_core)
save_json('locales/vi-VN/master_combined.json', master_dict)

print(f"\nFinal file sizes:")
print(f"menu.json: {len(final_menu)} entries")
print(f"gameplay.json: {len(final_gameplay)} entries")
print(f"core.json: {len(final_core)} entries")
print(f"master_combined.json: {len(master_dict)} entries (all in one)")

# 7. Generate statistics report
print("\n" + "="*60)
print("TRANSLATION STATISTICS REPORT")
print("="*60)

original_total = len(existing_menu) + len(existing_gameplay) + len(existing_core)
new_total = len(master_dict)
added = new_total - original_total

print(f"\nOriginal coverage:")
print(f"  Menu: {len(existing_menu)} strings")
print(f"  Gameplay: {len(existing_gameplay)} strings")
print(f"  Core: {len(existing_core)} strings")
print(f"  Total: {original_total} strings")

print(f"\nNew coverage:")
print(f"  Menu: {len(final_menu)} strings (+{len(final_menu)-len(existing_menu)})")
print(f"  Gameplay: {len(final_gameplay)} strings (+{len(final_gameplay)-len(existing_gameplay)})")
print(f"  Core: {len(final_core)} strings (+{len(final_core)-len(existing_core)})")
print(f"  Total: {new_total} strings (+{added})")

if original_total > 0:
    improvement = (added / original_total) * 100
    print(f"\nImprovement: +{added} strings ({improvement:.1f}% increase)")

print(f"\nEstimated new coverage: ~{(new_total/4145)*100:.1f}% of 4,145 total strings")

print("\n" + "="*60)
print("Files saved successfully!")
print("Original files backed up with .backup extension")
print("="*60)
