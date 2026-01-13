import re
import json

# Read the filtered strings
with open('filtered_chinese_strings.txt', 'r', encoding='utf-8') as f:
    strings = [line.strip() for line in f if line.strip()]

# Categorize strings
ui_strings = []
gameplay_strings = []
technical_strings = []

# Technical keywords to filter out
technical_keywords = [
    '函数', '参数', '属性', '变量', '运行', '代码', '语法', '错误', '返回值',
    '构造函数', '全局', '对象', '实现', '封送', '存储库', '分支', 'API',
    '不传入', '不传参', '不可配置', '测试模式', '解析', '订阅者', '监听',
    '扩展相关', '运行域', '卸载', '加载', '类型检查', '忽略', '标识符',
    '基本类型', '赋值行为', '转义字符', '运算符', '数据', '检索'
]

# UI keywords
ui_keywords = [
    '号位', '人', '局', '回合', '轮', '页', '上移', '下移', '显示', '隐藏',
    '选择', '设置', '配置', '模式', '按钮', '菜单', '界面', '效果', '音',
    '皮肤', '主题', '背景', '字体', '颜色', '触摸', '手势', '点击'
]

# Gameplay keywords
gameplay_keywords = [
    '武将', '技能', '牌', '伤害', '体力', '回合', '阶段', '装备', '判定',
    '摸牌', '弃牌', '出牌', '卡牌', '手牌', '桃', '杀', '闪', '锦囊',
    '阵亡', '复活', '势力', '主公', '忠臣', '反贼', '内奸', '距离', '范围',
    '触发', '发动', '使用', '打出', '目标', '来源', '拼点', '横置', '连环',
    '濒死', '受伤', '失去', '获得', '弃置', '展示', '亮出', '明置'
]

for s in strings:
    # Skip very technical strings
    is_technical = False
    for keyword in technical_keywords:
        if keyword in s:
            is_technical = True
            technical_strings.append(s)
            break

    if is_technical:
        continue

    # Skip strings that are clearly code comments or descriptions
    if any(x in s for x in ['若不存在', '不直接使用', '与的区别', '将被转移到', '用来兼容']):
        technical_strings.append(s)
        continue

    # Skip strings longer than 50 characters (likely descriptions)
    if len(s) > 50:
        technical_strings.append(s)
        continue

    # Categorize into UI or gameplay
    is_gameplay = False
    for keyword in gameplay_keywords:
        if keyword in s:
            is_gameplay = True
            gameplay_strings.append(s)
            break

    if not is_gameplay:
        # Check if UI
        is_ui = False
        for keyword in ui_keywords:
            if keyword in s:
                is_ui = True
                ui_strings.append(s)
                break

        if not is_ui:
            # Default to UI for short strings
            if len(s) <= 10:
                ui_strings.append(s)
            else:
                gameplay_strings.append(s)

# Remove duplicates
ui_strings = sorted(list(set(ui_strings)))
gameplay_strings = sorted(list(set(gameplay_strings)))

print(f"UI strings: {len(ui_strings)}")
print(f"Gameplay strings: {len(gameplay_strings)}")
print(f"Technical strings (filtered out): {len(technical_strings)}")
print(f"Total user-facing strings: {len(ui_strings) + len(gameplay_strings)}")

# Save categorized strings
with open('ui_strings_to_translate.txt', 'w', encoding='utf-8') as f:
    for s in ui_strings:
        f.write(s + '\n')

with open('gameplay_strings_to_translate.txt', 'w', encoding='utf-8') as f:
    for s in gameplay_strings:
        f.write(s + '\n')

print("\nSaved to ui_strings_to_translate.txt and gameplay_strings_to_translate.txt")
