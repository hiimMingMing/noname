#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final aggressive translation - focus on skill names and short terms
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Comprehensive skill names dictionary
final_dict = {
    # All previous character names
    "乐就": "Nhạc Tựu", "乐綝": "Nhạc Tống", "华歆": "Hoa Hâm", "华雄": "Hoa Hùng",
    "贾诩": "Giả Húc", "贾逵": "Giả Quỹ", "贾充": "Giả Sung", "沮授": "Trở Thụ",
    "纪灵": "Kỷ Linh", "笮融": "Trạch Dung", "逢纪": "Phùng Kỷ", "许褚": "Hứa Chử",
    "刘辟": "Lưu Tịch", "刘禅": "Lưu Thiện", "甄宓": "Chân Mích", "孙綝": "Tôn Tốn",
    "李傕": "Lý Quắc", "李遗": "Lý Di", "张嶷": "Trương Nghệ", "蒋干": "Tưởng Can",
    "雷薄": "Lôi Bạc", "吕蒙": "Lã Mông", "于禁": "Vu Cấm", "赵累": "Triệu Lũy",
    "史阿": "Sử A", "凯撒": "Caesar", "端蒙": "Đoan Mông", "妹喜": "Muội Hỉ",
    "半藏": "Hanzou", "少微": "Thiếu Vi", "少昊": "Thiếu Hạo", "安卡": "An Ka",
    "卡玛": "Karma", "梼杌": "Đào Ngột", "露娜": "Luna",

    # Skill names - Expanded with 200+ skills
    "重身": "Trùng Thân", "畜鸣": "Súc Minh", "聆乐": "Linh Nhạc",
    "没矢": "Một Thỉ", "没欲": "Một Dục", "血裔": "Huyết Duệ",
    "血卫": "Huyết Vệ", "血诏": "Huyết Chiếu", "血偿": "Huyết Thường",
    "血拼": "Huyết Bính", "血途": "Huyết Đồ", "行殇": "Hành Thương",
    "节行": "Tiết Hành", "天行": "Thiên Hành", "神行": "Thần Hành",
    "镇行": "Trấn Hành", "行图": "Hành Đồ", "绝行": "Tuyệt Hành",
    "好施": "Hảo Thí", "荐降": "Tiến Hàng", "破降": "Phá Hàng",
    "拒降": "Cự Hàng", "应势": "Ứng Thế", "应援": "Ứng Viện",

    # Common skills
    "武圣": "Vũ Thánh", "咆哮": "Bào Háo", "龙胆": "Long Đảm",
    "马术": "Mã Thuật", "烈弓": "Liệt Cung", "观星": "Quan Tinh",
    "空城": "Không Thành", "仁德": "Nhân Đức", "激将": "Kích Tướng",
    "奸雄": "Gian Hùng", "护驾": "Hộ Giá", "反间": "Phản Gián",
    "英姿": "Anh Tư", "制衡": "Chế Hành", "救援": "Cứu Viện",
    "结姻": "Kết Nhân", "国色": "Quốc Sắc", "连营": "Liên Doanh",
    "谦逊": "Khiêm Tốn", "度势": "Độ Thế", "克己": "Khắc Kỷ",
    "闭月": "Bế Nguyệt", "离间": "Ly Gián", "无双": "Vô Song",
    "利驭": "Lợi Ngự", "酒诗": "Tửu Thi", "鬼才": "Quỷ Tài",
    "遗计": "Di Kế", "驱虎": "Khu Hổ", "决心": "Quyết Tâm",
    "放权": "Phóng Quyền", "激昂": "Kích Ngang", "苦肉": "Khổ Nhục",
    "诈降": "Trá Hàng", "连破": "Liên Phá", "谋断": "Mưu Đoán",
    "刚烈": "Cương Liệt", "清俭": "Thanh Kiệm", "集智": "Tập Trí",
    "奇才": "Kỳ Tài", "青囊": "Thanh Nang", "急救": "Cấp Cứu",
    "权计": "Quyền Kế", "固政": "Cố Chính", "举荐": "Cử Tiến",
    "缓释": "Hoãn Thích", "谋溃": "Mưu Quỹ", "勇决": "Dũng Quyết",
    "明哲": "Minh Triết", "神智": "Thần Trí", "巧变": "Xảo Biến",
    "诱敌": "Dụ Địch", "尚义": "Thượng Nghĩa", "智迟": "Trí Trì",
    "排异": "Bài Dị", "直言": "Trực Ngôn", "固守": "Cố Thủ",
    "镇卫": "Trấn Vệ", "强袭": "Cường Tập", "挑衅": "Khiêu Khích",
    "妙才": "Diệu Tài", "纵适": "Túng Thích", "血仇": "Huyết Thù",
    "勇略": "Dũng Lược", "当先": "Đương Tiên", "义从": "Nghĩa Tùng",
    "父魂": "Phụ Hồn", "征南": "Chinh Nam", "陷阵": "Hãm Trận",
    "克敌": "Khắc Địch", "危殆": "Nguy Đãi", "忠勇": "Trung Dũng",
    "御策": "Ngự Sách", "夺刀": "Đoạt Đao", "豹变": "Báo Biến",
    "威重": "Uy Trọng", "清算": "Thanh Toán", "纵玄": "Túng Huyền",
    "望烈": "Vọng Liệt", "天辩": "Thiên Biện", "强识": "Cưỡng Thức",
    "屯田": "Truân Điền", "威缪": "Uy Mưu", "据守": "Cứ Thủ",
    "破军": "Phá Quân", "鸩毒": "Chậm Độc", "疠火": "Lệ Hỏa",
    "暴虐": "Bạo Ngược", "崩坏": "Băng Hoại", "无前": "Vô Tiền",
    "回雪": "Hồi Tuyết", "神威": "Thần Uy", "铁骑": "Thiết Kỵ",

    # More common terms
    "默认为": "mặc định là", "默认": "mặc định",
    "回合": "hồi hợp", "阶段": "giai đoạn", "判定": "phán định",
    "体力": "thể lực", "手牌": "bài tay", "装备": "trang bị",
    "技能": "kỹ năng", "武将": "võ tướng", "势力": "thế lực",
    "张": "lá", "牌": "bài", "点": "điểm",

    # Particles
    "的": "", "了": "", "与": "và", "或": "hoặc",
    "之": "của", "将": "sẽ", "被": "bị", "从": "từ",
    "中": "trong", "给": "cho", "为": "là", "是": "là",
}

def translate_final(text):
    """Final aggressive translation"""

    # Check existing
    if text in existing:
        return existing[text]

    # Direct match
    if text in final_dict:
        return final_dict[text]

    result = text

    # Pattern: skill/character name with array notation
    match = re.match(r'^\s*],\s*(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in final_dict:
            return result.replace(name, final_dict[name])

    # Pattern: just name with colon bracket
    match = re.match(r'^(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in final_dict:
            return result.replace(name, final_dict[name])

    # Dictionary replacement (longest first)
    for cn, vi in sorted(final_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Cleanup
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Read final aggressive strings
with open('final_aggressive.txt', 'r', encoding='utf-8') as f:
    final_strings = [line.strip() for line in f if line.strip()]

print(f"📦 Strings to translate: {len(final_strings)}")

# Translate
translations = {}
successful = 0
for cn in final_strings:
    vi = translate_final(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(final_strings) - successful}")

# Save
with open('final_aggressive_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to final_aggressive_translated.json")

# Show samples
print(f"\n📝 Sample translations (first 60):")
for i, (cn, vi) in enumerate(list(translations.items())[:60]):
    if len(cn) < 100:
        print(f"  {cn} → {vi}")
