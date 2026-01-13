#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pattern-based Auto Translation for Noname Game
Handles common patterns automatically
"""

import json
import re

# Character name mappings (Three Kingdoms)
CHARACTER_NAMES = {
    "刘备": "Lưu Bị", "关羽": "Quan Vũ", "张飞": "Trương Phi", "诸葛亮": "Gia Cát Lượng",
    "赵云": "Triệu Vân", "马超": "Mã Siêu", "黄忠": "Hoàng Trung", "魏延": "Ngụy Diên",
    "曹操": "Tào Tháo", "司马懿": "Tư Mã Ý", "夏侯惇": "Hạ Hầu Đôn", "张辽": "Trương Liêu",
    "许褚": "Hứa Chử", "曹仁": "Tào Nhân", "曹丕": "Tào Phi", "郭嘉": "Quách Gia",
    "孙权": "Tôn Quyền", "周瑜": "Chu Du", "陆逊": "Lục Tốn", "甘宁": "Cam Ninh",
    "太史慈": "Thái Sử Từ", "孙尚香": "Tôn Thượng Hương", "吕蒙": "Lữ Mông", "黄盖": "Hoàng Cái",
    "吕布": "Lữ Bố", "貂蝉": "Điêu Thuyền", "董卓": "Đổng Trác", "袁绍": "Viên Thiệu",
    "于禁": "Vu Cấm", "乐进": "Nhạc Tiến", "刘禅": "Lưu Thiện", "华雄": "Hoa Hùng",
    "华歆": "Hoa Hân", "刘辟": "Lưu Tịch",
}

# Card names (standard cards)
CARD_NAMES = {
    "杀": "Sát",
    "闪": "Tránh",
    "桃": "Đào",
    "决斗": "Quyết Đấu",
    "南蛮入侵": "Nam Man Nhập Xâm",
    "万箭齐发": "Vạn Tiễn Tề Phát",
    "桃园结义": "Đào Viên Kết Nghĩa",
    "无中生有": "Vô Trung Sinh Hữu",
    "过河拆桥": "Quá Hà Khư Kiều",
    "顺手牵羊": "Thuận Thủ Thiên Dương",
    "无懈可击": "Vô Tà Khả Kích",
    "借刀杀人": "Tá Đao Sát Nhân",
    "火攻": "Hỏa Công",
    "铁索连环": "Thiết Tỏa Liên Hoàn",
    "五谷丰登": "Ngũ Cốc Phong Đăng",
    "闪电": "Thiểm Điện",
    "乐不思蜀": "Nhạc Bất Tư Thục",
    "兵粮寸断": "Binh Lương Thốn Đoạn",
}

# Equipment names
EQUIPMENT_NAMES = {
    "诸葛连弩": "Gia Cát Liên Nỏ",
    "青釭剑": "Thanh Cương Kiếm",
    "寒冰剑": "Hàn Băng Kiếm",
    "方天画戟": "Phương Thiên Họa Kích",
    "丈八蛇矛": "Trượng Bát Xà Mâu",
    "贯石斧": "Quán Thạch Phủ",
    "青龙偃月刀": "Thanh Long Yển Nguyệt Đao",
    "雌雄双股剑": "Thư Hùng Song Cổ Kiếm",
    "麒麟弓": "Kỳ Lân Cung",
    "八卦阵": "Bát Quái Trận",
    "仁王盾": "Nhân Vương Thuẫn",
    "白银狮子": "Bạch Ngân Sư Tử",
    "藤甲": "Đằng Giáp",
    "绝影": "Tuyệt Ảnh",
    "的卢": "Đích Lô",
    "赤兔": "Xích Thố",
    "紫骍": "Tử Tinh",
    "大宛": "Đại Uyển",
    "爪黄飞电": "Trảo Hoàng Phi Điện",
}

# Common game terms
GAME_TERMS = {
    "武将": "Võ tướng",
    "技能": "Kỹ năng",
    "主公": "Chủ công",
    "忠臣": "Trung thần",
    "反贼": "Phản tặc",
    "内奸": "Nội gian",
    "体力": "Thể lực",
    "手牌": "Bài tay",
    "装备": "Trang bị",
    "判定": "Phán định",
    "伤害": "Sát thương",
    "回合": "Hồi hợp",
    "阶段": "Giai đoạn",
    "摸牌": "Rút bài",
    "弃牌": "Bỏ bài",
    "出牌": "Ra bài",
    "锦囊": "Cẩm nang",
    "延时锦囊": "Trì Hoãn Cẩm nang",
    "拼点": "Đấu điểm",
    "距离": "Khoảng cách",
    "濒死": "Hấp hối",
    "阵亡": "Trận vong",
    "复活": "Phục sinh",
    "横置": "Ngang trí",
    "连环": "Liên hoàn",
    "翻面": "Lật mặt",
    "牌堆": "Chồng bài",
    "弃牌堆": "Chồng bài bỏ",
    "护甲": "Hộ giáp",
}

# Skill types
SKILL_TYPES = {
    "锁定技": "Tỏa Định Kỹ",
    "限定技": "Hạn Định Kỹ",
    "觉醒技": "Giác Tỉnh Kỹ",
    "主公技": "Chủ Công Kỹ",
    "主将技": "Chủ Tướng Kỹ",
    "副将技": "Phó Tướng Kỹ",
    "转换技": "Chuyển Hoán Kỹ",
    "阵法技": "Trận Pháp Kỹ",
    "隐匿技": "Ẩn Nặc Kỹ",
    "使命技": "Sứ Mệnh Kỹ",
    "君主技": "Quân Chủ Kỹ",
    "宗族技": "Tông Tộc Kỹ",
    "势力技": "Thế Lực Kỹ",
}

# Number words
NUMBER_WORDS = {
    "一": "Một", "二": "Hai", "三": "Ba", "四": "Bốn", "五": "Năm",
    "六": "Sáu", "七": "Bảy", "八": "Tám", "九": "Chín", "十": "Mười",
}

def translate_by_pattern(text):
    """Translate using pattern matching"""

    # Direct character name translation
    for cn_name, vi_name in CHARACTER_NAMES.items():
        if text == cn_name:
            return vi_name

    # Direct card translation
    for cn_card, vi_card in CARD_NAMES.items():
        if text == cn_card:
            return vi_card

    # Direct equipment translation
    for cn_equip, vi_equip in EQUIPMENT_NAMES.items():
        if text == cn_equip:
            return vi_equip

    # Direct skill type translation
    for cn_skill, vi_skill in SKILL_TYPES.items():
        if text == cn_skill:
            return vi_skill

    # Pattern: X人 -> X người
    match = re.match(r'^([一二三四五六七八九十百]+)人$', text)
    if match:
        num_word = match.group(1)
        if num_word in NUMBER_WORDS:
            return f"{NUMBER_WORDS[num_word]} người"
        return f"{num_word} người"

    # Pattern: X号位 -> Vị trí X
    match = re.match(r'^([一二三四五六七八九十百\d]+)号位$', text)
    if match:
        num = match.group(1)
        if num in NUMBER_WORDS:
            num = NUMBER_WORDS[num]
        return f"Vị trí {num}"

    # Pattern: X回合 -> X hồi hợp
    match = re.match(r'^([一二三四五六七八九十百\d]+)回合$', text)
    if match:
        num = match.group(1)
        if num in NUMBER_WORDS:
            num = NUMBER_WORDS[num]
        elif num.isdigit():
            if int(num) == 20:
                num = "Hai mươi"
            elif int(num) == 30:
                num = "Ba mươi"
        return f"{num} hồi hợp"

    # Pattern: X局 -> X ván
    match = re.match(r'^([一二三四五六七八九十百\d]+)局$', text)
    if match:
        num = match.group(1)
        if num in NUMBER_WORDS:
            num = NUMBER_WORDS[num]
        elif num.isdigit():
            if int(num) == 20:
                num = "Hai mươi"
            elif int(num) == 50:
                num = "Năm mươi"
        return f"{num} ván"

    # Pattern: X轮 -> X vòng
    match = re.match(r'^([一二三四五六七八九十百]+)轮$', text)
    if match:
        num_word = match.group(1)
        if num_word in NUMBER_WORDS:
            return f"{NUMBER_WORDS[num_word]} vòng"
        return f"{num_word} vòng"

    # Pattern: X次 -> X lần
    match = re.match(r'^([一二三四五六七八九十百]+)次$', text)
    if match:
        num_word = match.group(1)
        if num_word in NUMBER_WORDS:
            return f"{NUMBER_WORDS[num_word]} lần"
        return f"{num_word} lần"

    # Pattern: X分钟 -> X phút
    match = re.match(r'^([一二三四五六七八九十百半]+)分钟$', text)
    if match:
        num_word = match.group(1)
        if num_word == "半":
            return "Nửa phút"
        if num_word in NUMBER_WORDS:
            return f"{NUMBER_WORDS[num_word]} phút"
        return f"{num_word} phút"

    # Pattern: X连击 -> X Liên Kích
    match = re.match(r'^([一二三四五六七八九十]+)连击$', text)
    if match:
        num_word = match.group(1)
        if num_word in NUMBER_WORDS:
            return f"{NUMBER_WORDS[num_word]} Liên Kích"
        return f"{num_word} Liên Kích"

    # Pattern: 不XXX -> Không XXX (negation)
    if text.startswith("不") and len(text) > 1:
        rest = text[1:]
        # Try to translate the rest
        rest_trans = translate_by_pattern(rest)
        if rest_trans and rest_trans != rest:
            return f"Không {rest_trans}"

    # Common prefixes/suffixes
    if text.endswith("模式"):
        base = text[:-2]
        base_trans = translate_by_pattern(base)
        if base_trans and base_trans != base:
            return f"Chế độ {base_trans}"

    if text.endswith("包"):
        base = text[:-1]
        if base in GAME_TERMS:
            return f"Gói {GAME_TERMS[base]}"

    # Game term replacement in longer strings
    result = text
    for cn, vi in GAME_TERMS.items():
        result = result.replace(cn, vi)
    if result != text:
        return result

    return None

def load_comprehensive_dict():
    """Load the comprehensive dictionary"""
    try:
        from comprehensive_translations import get_all_translations
        return get_all_translations()
    except:
        return {}

def translate_all_files():
    """Translate all remaining strings"""

    # Load comprehensive dictionary
    comp_dict = load_comprehensive_dict()
    print(f"Loaded {len(comp_dict)} translations from comprehensive dictionary")

    # Process UI strings
    with open('ui_strings_to_translate.txt', 'r', encoding='utf-8') as f:
        ui_strings = [line.strip() for line in f if line.strip()]

    ui_translations = {}
    ui_remaining = []

    for s in ui_strings:
        # Try comprehensive dict first
        if s in comp_dict:
            ui_translations[s] = comp_dict[s]
        else:
            # Try pattern matching
            trans = translate_by_pattern(s)
            if trans:
                ui_translations[s] = trans
            else:
                ui_remaining.append(s)

    # Process gameplay strings
    with open('gameplay_strings_to_translate.txt', 'r', encoding='utf-8') as f:
        gameplay_strings = [line.strip() for line in f if line.strip()]

    gameplay_translations = {}
    gameplay_remaining = []

    for s in gameplay_strings:
        # Try comprehensive dict first
        if s in comp_dict:
            gameplay_translations[s] = comp_dict[s]
        else:
            # Try pattern matching
            trans = translate_by_pattern(s)
            if trans:
                gameplay_translations[s] = trans
            else:
                gameplay_remaining.append(s)

    # Save translations
    with open('ui_translations_final.json', 'w', encoding='utf-8') as f:
        json.dump(ui_translations, f, ensure_ascii=False, indent=2)

    with open('gameplay_translations_final.json', 'w', encoding='utf-8') as f:
        json.dump(gameplay_translations, f, ensure_ascii=False, indent=2)

    # Save remaining
    with open('ui_remaining_final.txt', 'w', encoding='utf-8') as f:
        for s in ui_remaining:
            f.write(s + '\n')

    with open('gameplay_remaining_final.txt', 'w', encoding='utf-8') as f:
        for s in gameplay_remaining:
            f.write(s + '\n')

    # Print statistics
    print("\n=== TRANSLATION STATISTICS ===")
    print(f"\nUI Strings:")
    print(f"  Total: {len(ui_strings)}")
    print(f"  Translated: {len(ui_translations)}")
    print(f"  Remaining: {len(ui_remaining)}")
    print(f"  Coverage: {len(ui_translations)/len(ui_strings)*100:.1f}%")

    print(f"\nGameplay Strings:")
    print(f"  Total: {len(gameplay_strings)}")
    print(f"  Translated: {len(gameplay_translations)}")
    print(f"  Remaining: {len(gameplay_remaining)}")
    print(f"  Coverage: {len(gameplay_translations)/len(gameplay_strings)*100:.1f}%")

    print(f"\nOverall:")
    print(f"  Total: {len(ui_strings) + len(gameplay_strings)}")
    print(f"  Translated: {len(ui_translations) + len(gameplay_translations)}")
    print(f"  Remaining: {len(ui_remaining) + len(gameplay_remaining)}")
    print(f"  Coverage: {(len(ui_translations) + len(gameplay_translations))/(len(ui_strings) + len(gameplay_strings))*100:.1f}%")

if __name__ == '__main__':
    translate_all_files()
