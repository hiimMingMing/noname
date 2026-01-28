#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate next batch with expanded character names and skills
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Ultra-expanded dictionary with character names and skill names
next_dict = {
    # Previous character names
    "乐就": "Nhạc Tựu", "乐綝": "Nhạc Tống", "华歆": "Hoa Hâm", "华雄": "Hoa Hùng",
    "贾诩": "Giả Húc", "贾逵": "Giả Quỹ", "贾充": "Giả Sung", "沮授": "Trở Thụ",
    "纪灵": "Kỷ Linh", "笮融": "Trạch Dung", "逢纪": "Phùng Kỷ", "许褚": "Hứa Chử",
    "刘辟": "Lưu Tịch", "刘禅": "Lưu Thiện", "甄宓": "Chân Mích", "孙綝": "Tôn Tốn",
    "李傕": "Lý Quắc", "李遗": "Lý Di", "张嶷": "Trương Nghệ", "蒋干": "Tưởng Can",
    "雷薄": "Lôi Bạc", "吕蒙": "Lã Mông", "于禁": "Vu Cấm", "赵累": "Triệu Lũy",
    "史阿": "Sử A", "凯撒": "Caesar", "端蒙": "Đoan Mông", "妹喜": "Muội Hỉ",
    "半藏": "Hanzou", "少微": "Thiếu Vi",

    # Additional character names
    "少昊": "Thiếu Hạo", "安卡": "An Ka", "卡玛": "Karma", "梼杌": "Đào Ngột",
    "露娜": "Luna", "孙坚": "Tôn Kiên", "孙权": "Tôn Quyền", "孙策": "Tôn Sách",
    "关羽": "Quan Vũ", "张飞": "Trương Phi", "赵云": "Triệu Vân", "马超": "Mã Siêu",
    "黄忠": "Hoàng Trung", "诸葛亮": "Gia Cát Lượng", "刘备": "Lưu Bị",
    "曹操": "Tào Tháo", "周瑜": "Chu Du", "司马懿": "Tư Mã Ý", "甘宁": "Cam Ninh",
    "太史慈": "Thái Sử Từ", "孙尚香": "Tôn Thượng Hương", "陆逊": "Lục Tốn",
    "貂蝉": "Điêu Thuyền", "吕布": "Lã Bố", "董卓": "Đổng Trác", "颜良": "Nhan Lương",
    "文丑": "Văn Sửu", "袁绍": "Viên Thiệu", "张辽": "Trương Liêu", "徐晃": "Từ Hoảng",
    "夏侯惇": "Hạ Hầu Đôn", "夏侯渊": "Hạ Hầu Uyên", "曹仁": "Tào Nhân",
    "曹丕": "Tào Phi", "郭嘉": "Quách Gia", "荀彧": "Tuân Úc", "荀攸": "Tuân Du",
    "典韦": "Điển Vi", "张郃": "Trương Cáp", "庞统": "Bàng Thống", "魏延": "Ngụy Diên",
    "姜维": "Khương Duy", "马谡": "Mã Tốc", "黄月英": "Hoàng Nguyệt Anh",
    "孟获": "Mạnh Hoạch", "祝融": "Chúc Dung", "大乔": "Đại Kiều", "小乔": "Tiểu Kiều",
    "黄盖": "Hoàng Cái", "程普": "Trình Phổ", "丁奉": "Đinh Phụng", "张昭": "Trương Chiêu",
    "张纮": "Trương Hoằng", "顾雍": "Cố Ung", "鲁肃": "Lỗ Túc", "诸葛瑾": "Gia Cát Cẩn",
    "步骘": "Bộ Chất", "凌统": "Lăng Thống", "徐盛": "Từ Thịnh", "潘璋": "Phan Chương",
    "朱桓": "Chu Hoàn", "朱然": "Chu Nhiên", "吕范": "Lã Phạm", "蒋钦": "Tưởng Khâm",
    "周泰": "Chu Thái", "陈武": "Trần Vũ", "董袭": "Đổng Tập", "韩当": "Hàn Đương",

    # Skill names (common Three Kingdoms skills)
    "重身": "Trùng Thân",
    "畜鸣": "Súc Minh",
    "聆乐": "Linh Nhạc",
    "没矢": "Một Thỉ",
    "没欲": "Một Dục",
    "血裔": "Huyết Duệ",
    "血卫": "Huyết Vệ",
    "血诏": "Huyết Chiếu",
    "血偿": "Huyết Thường",
    "血拼": "Huyết Bính",
    "血途": "Huyết Đồ",
    "行殇": "Hành Thương",
    "节行": "Tiết Hành",
    "天行": "Thiên Hành",
    "武圣": "Vũ Thánh",
    "咆哮": "Bào Háo",
    "龙胆": "Long Đảm",
    "马术": "Mã Thuật",
    "烈弓": "Liệt Cung",
    "观星": "Quan Tinh",
    "空城": "Không Thành",
    "仁德": "Nhân Đức",
    "激将": "Kích Tướng",
    "奸雄": "Gian Hùng",
    "护驾": "Hộ Giá",
    "反间": "Phản Gián",
    "英姿": "Anh Tư",
    "制衡": "Chế Hành",
    "救援": "Cứu Viện",
    "结姻": "Kết Nhân",
    "国色": "Quốc Sắc",
    "连营": "Liên Doanh",
    "谦逊": "Khiêm Tốn",
    "度势": "Độ Thế",
    "克己": "Khắc Kỷ",
    "闭月": "Bế Nguyệt",
    "离间": "Ly Gián",
    "无双": "Vô Song",
    "利驭": "Lợi Ngự",
    "酒诗": "Tửu Thi",
    "鬼才": "Quỷ Tài",
    "遗计": "Di Kế",
    "驱虎": "Khu Hổ",
    "决心": "Quyết Tâm",
    "放权": "Phóng Quyền",
    "激昂": "Kích Ngang",
    "苦肉": "Khổ Nhục",
    "诈降": "Trá Hàng",
    "连破": "Liên Phá",
    "谋断": "Mưu Đoán",

    # Game terms
    "回合": "hồi hợp", "阶段": "giai đoạn", "判定": "phán định",
    "摸牌": "rút bài", "出牌": "ra bài", "弃牌": "bỏ bài",
    "体力": "thể lực", "手牌": "bài tay", "装备": "trang bị",
    "技能": "kỹ năng", "武将": "võ tướng", "势力": "thế lực",
    "伤害": "sát thương", "恢复": "hồi phục", "至少": "ít nhất",
    "张": "lá", "牌": "bài", "点": "điểm", "次": "lần",
    "默认为": "mặc định là", "默认": "mặc định",

    # Common particles
    "的": "", "了": "", "与": "và", "或": "hoặc", "及": "và",
    "但": "nhưng", "如果": "nếu", "时": "khi", "后": "sau",
    "前": "trước", "之": "của", "将": "sẽ", "被": "bị",
    "给": "cho", "为": "là", "是": "là", "从": "từ",
    "中": "trong", "对": "đối", "向": "hướng", "到": "đến",
    "在": "tại", "于": "ở", "以": "để",
}

def translate_next(text):
    """Translate next batch strings"""

    # Check existing
    if text in existing:
        return existing[text]

    # Direct match
    if text in next_dict:
        return next_dict[text]

    result = text

    # Pattern: character/skill name with array notation
    match = re.match(r'^\s*],\s*(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in next_dict:
            return result.replace(name, next_dict[name])

    # Pattern: just name with colon bracket
    match = re.match(r'^(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in next_dict:
            return result.replace(name, next_dict[name])

    # Dictionary replacement (longest first)
    for cn, vi in sorted(next_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Cleanup
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Read next batch strings
with open('next_batch_to_translate.txt', 'r', encoding='utf-8') as f:
    next_strings = [line.strip() for line in f if line.strip()]

print(f"📦 Strings to translate: {len(next_strings)}")

# Translate
translations = {}
successful = 0
for cn in next_strings:
    vi = translate_next(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(next_strings) - successful}")

# Save
with open('next_batch_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to next_batch_translated.json")

# Show samples
print(f"\n📝 Sample translations:")
for i, (cn, vi) in enumerate(list(translations.items())[:50]):
    if len(cn) < 100 and len(vi) < 100:
        print(f"  {cn} → {vi}")
