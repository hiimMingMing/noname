# -*- coding: utf-8 -*-
import json
import re

# Comprehensive character translation dictionary - Batch 2 expansion
character_translations = {
    # Base characters (from previous batch)
    "曹操": "Tào Tháo",
    "刘备": "Lưu Bị",
    "孙权": "Tôn Quyền",
    "关羽": "Quan Vũ",
    "张飞": "Trương Phi",
    "赵云": "Triệu Vân",
    "诸葛亮": "Gia Cát Lượng",
    "周瑜": "Chu Du",
    "孙策": "Tôn Sách",
    "吕布": "Lã Bố",
    "貂蝉": "Điêu Thuyền",
    "华佗": "Hoa Đà",
    "司马懿": "Tư Mã Ý",
    "曹丕": "Tào Phi",
    "曹植": "Tào Thực",
    "郭嘉": "Quách Gia",
    "贾诩": "Giả Hủ",
    "马超": "Mã Siêu",
    "黄忠": "Hoàng Trung",
    "魏延": "Ngụy Diên",
    "孙尚香": "Tôn Thượng Hương",
    "大乔": "Đại Kiều",
    "小乔": "Tiểu Kiều",
    "甘宁": "Cam Ninh",
    "吕蒙": "Lã Mông",
    "陆逊": "Lục Tốn",
    "孙坚": "Tôn Kiên",
    "夏侯惇": "Hạ Hầu Đôn",
    "张辽": "Trương Liêu",
    "张郃": "Trương Cáp",
    "徐晃": "Từ Hoảng",
    "曹仁": "Tào Nhân",
    "董卓": "Đổng탁",
    "庞统": "Bàng Thống",
    "法正": "Pháp Chính",
    "周不疑": "Chu Bất Nghi",

    # New characters from batch 2
    "徐氏": "Từ Thị",
    "曹洪": "Tào Hồng",
    "孙寒华": "Tôn Hàn Hoa",
    "庞德公": "Bàng Đức Công",
    "刘协": "Lưu Hiệp",
    "吉本": "Cát Bổn",
    "庞德": "Bàng Đức",
    "灵雎": "Linh Thư",
    "穆顺": "Mục Thuận",
    "神马超": "Thần Mã Siêu",
    "傅肜": "Phó Dung",
    "刘宏": "Lưu Hoằng",
    "卑弥呼": "Ti Di Hô",
    "卞夫人": "Biện Phu Nhân",
    "司马孚": "Tư Mã Phù",
    "吴班": "Ngô Ban",
    "周处": "Chu Xứ",
    "夏侯霸": "Hạ Hầu Bá",
    "大乔小乔": "Đại Tiểu Kiều",
    "孙翊": "Tôn Dực",
    "宗预": "Tông Dự",
    "张允": "Trương Doãn",
    "张宁": "Trương Ninh",
    "张既": "Trương Ký",
    "曹昂": "Tào Ngang",
    "李遗": "Lý Di",
    "桥蕤": "Kiều Nhuỵ",
    "毌丘俭": "Quán Khâu Kiệm",
    "牛金": "Ngưu Kim",
    "王凌": "Vương Lăng",
    "王昶": "Vương Xương",
    "王粲": "Vương Xán",
    "田豫": "Điền Dự",
    "祖茂": "Tổ Mậu",
    "神关羽": "Thần Quan Vũ",
    "神吕蒙": "Thần Lã Mông",
    "葛玄": "Cát Huyền",
    "蒋济": "Tưởng Tế",
    "诸葛果": "Gia Cát Quả",
    "谋曹丕": "Mưu Tào Phi",
    "谋诸葛亮": "Mưu Gia Cát Lượng",
    "谯周": "Tiều Chu",
    "赵襄": "Triệu Tương",
    "何进": "Hà Tiến",
    "皇甫嵩": "Hoàng Phủ Tung",
    "阎象": "Diêm Tượng",
    "陈武董袭": "Trần Vũ Đổng Tập",
    "陈震": "Trần Chấn",
    "马云騄": "Mã Vân Lục",
    "麴义": "Khúc Nghĩa",
    "鲍信": "Bão Tín",

    # Japanese crossover characters
    "一之濑琴美": "Ichinose Kotomi",
    "七濑留美": "Nanase Rumi",
    "三枝二木": "Saegusa Futaki",
    "三谷良一": "Mitani Ryoichi",
    "久岛鸥": "Hisashima Kamome",
    "中津静流": "Nakatsu Shizuru",
    "乙坂有宇": "Otosaka Yuu",

    # Princess and special titles
    "万年公主": "Vạn Niên Công Chúa",
    "严夫人": "Nghiêm Phu Nhân",
    "乐周妃": "Nhạc Chu Phi",
    "乐诸葛果": "Nhạc Gia Cát Quả",

    # Historical figures
    "严颜": "Nghiêm Nhan",
    "严畯": "Nghiêm Tuấn",
    "严虎": "Nghiêm Hổ",
    "丘力居": "Khâu Lực Cư",
    "丰祈": "Phong Kì",
}

# Skill name translations (Vietnamese martial arts style)
skill_translations = {
    "七出": "Thất Xuất",
    "七哀": "Thất Ai",
    "七幻": "Thất Huyễn",
    "七弦": "Thất Huyền",
    "七星": "Thất Tinh",
    "七步": "Thất Bộ",
    "七笺": "Thất Tiên",
    "七辩": "Thất Biện",
    "七进": "Thất Tiến",
    "三头": "Tam Đầu",
    "三恇": "Tam Khương",
    "三殴": "Tam Âu",
    "三点": "Tam Điểm",
    "三略": "Tam Lược",
    "三礼": "Tam Lễ",
    "三窟": "Tam Quật",
    "三陈": "Tam Trần",
    "三顾": "Tam Cố",
    "三首": "Tam Thủ",
    "下书": "Hạ Thư",
    "不屈": "Bất Khuất",
    "不弃": "Bất Khí",
    "不悔": "Bất Hối",
    "不戢": "Bất Tập",
    "不臣": "Bất Thần",
    "专对": "Chuyên Đối",
    "业仇": "Nghiệp Cừu",
    "业火": "Nghiệp Hỏa",
    "业炎": "Nghiệp Viêm",
    "两点": "Lưỡng Điểm",
    "严政": "Nghiêm Chính",
    "严教": "Nghiêm Giáo",
    "严整": "Nghiêm Chỉnh",
    "严纪": "Nghiêm Kỷ",
    "严纲": "Nghiêm Cương",
    "严霜": "Nghiêm Sương",
    "丧乱": "Tang Loạn",
    "丧尸": "Tang Thi",
    "中枢": "Trung Xu",
    "中流": "Trung Lưu",
    "丰姿": "Phong Tư",
    "丰愍": "Phong Mẫn",
    "丰田": "Phong Điền",
    "丰积": "Phong Tích",
    "临节": "Lâm Tiết",
    "临阵": "Lâm Trận",
    "丹心": "Đan Tâm",
    "丹法": "Đan Pháp",
    "为乱": "Vi Loạn",
    "举义": "Cử Nghĩa",
    "举兵": "Cử Binh",
    "举寇": "Cử Khấu",
    "举棋": "Cử Kỳ",
    "举策": "Cử Sách",
    "举荐": "Cử Tiến",
    "举讹": "Cử Ngoa",
    "义争": "Nghĩa Tranh",
    "义从": "Nghĩa Tùng",
    "义兵": "Nghĩa Binh",
    "义叱": "Nghĩa Sất",
    "义拒": "Nghĩa Cự",
    "义烈": "Nghĩa Liệt",
    "义绝": "Nghĩa Tuyệt",
    "义舍": "Nghĩa Xá",
    "义襄": "Nghĩa Tương",
    "义贤": "Nghĩa Hiền",
    "义释": "Nghĩa Thích",
    "乌鹊": "Ô Thước",
    "乐泉": "Nhạc Tuyền",
    "乐虞": "Nhạc Ngu",
    "乐陵": "Nhạc Lăng",
    "乐马": "Nhạc Mã",
    "乘变": "Thừa Biến",
    "乘流": "Thừa Lưu",
    "乘烟": "Thừa Yên",
    "乘虚": "Thừa Hư",
    "乘袭": "Thừa Tập",
    "九伐": "Cửu Phạt",
    "一点": "Nhất Điểm",
    "一鼓作气": "Nhất Cổ Tác Khí",
    "万王": "Vạn Vương",
    "世公": "Thế Công",
    "东道": "Đông Đạo",
    "东郊": "Đông Giao",
    "丝刃": "Ti Nhận",
    "不可响应": "bất khả hưởng ứng",
    "丑牛": "Sửu Ngưu",
    "天书": "Thiên Thư",
}

# Prefix translations
prefix_translations = {
    "OL": "OL",
    "SP": "SP",
    "界": "Giới",
    "神": "Thần",
    "TW": "TW",
    "SCL": "SCL",
    "26": "26",
    "26SP": "26SP",
    "★": "★",
    "☆": "☆",
    "〖": "〖",
    "〗": "〗",
    "S特": "S Đặc",
    "TW|": "TW|",
    "九鼎": "Cửu Đỉnh",
    "起": "Khởi",
    "将": "Tướng",
    "谋": "Mưu",
    "魔": "Ma",
    "乐": "Nhạc",
}

def translate_name(name):
    """Translate character/skill name with prefix handling"""
    name = name.strip()

    # Handle special quote case
    if name == '"天书"':
        return '"Thiên Thư"'

    # Check if it's a pure skill name
    if name in skill_translations:
        return skill_translations[name]

    # Check if it's a pure character name
    if name in character_translations:
        return character_translations[name]

    # Handle TW special cases first
    if name.startswith("TW起"):
        base_name = name[3:]
        if base_name in character_translations:
            return f"TW Khởi {character_translations[base_name]}"

    if name.startswith("TW将"):
        base_name = name[3:]
        if base_name in character_translations:
            return f"TW Tướng {character_translations[base_name]}"

    if name.startswith("TW谋"):
        base_name = name[3:]
        if base_name in character_translations:
            return f"TW Mưu {character_translations[base_name]}"

    if name.startswith("TW魔"):
        base_name = name[3:]
        if base_name in character_translations:
            return f"TW Ma {character_translations[base_name]}"

    if name.startswith("TW神"):
        base_name = name[3:]
        if base_name in character_translations:
            return f"TW Thần {character_translations[base_name]}"

    if name.startswith("TW"):
        base_name = name[2:]
        if base_name in character_translations:
            return f"TW {character_translations[base_name]}"
        if base_name in skill_translations:
            return f"TW {skill_translations[base_name]}"

    # Handle other prefixes
    for prefix in ["26SP", "SCL", "OL乐", "九鼎", "☆SP", "S特神", "TW|"]:
        if name.startswith(prefix):
            base_name = name[len(prefix):]
            if base_name in character_translations:
                return f"{prefix} {character_translations[base_name]}"
            if base_name in skill_translations:
                return f"{prefix} {skill_translations[base_name]}"

    for prefix in ["OL", "SP", "界", "神", "26", "★", "☆", "〖"]:
        if name.startswith(prefix):
            base_name = name[len(prefix):]
            if base_name in character_translations:
                prefix_vi = prefix_translations.get(prefix, prefix)
                return f"{prefix_vi} {character_translations[base_name]}"
            if base_name in skill_translations:
                prefix_vi = prefix_translations.get(prefix, prefix)
                return f"{prefix_vi} {skill_translations[base_name]}"

    # Handle suffix 〗
    if name.endswith("〗"):
        base_name = name[:-1]
        if base_name in skill_translations:
            return f"{skill_translations[base_name]}〗"

    return None

# Read input file
with open('remaining_names_batch1.txt', 'r', encoding='utf-8') as f:
    names = [line.strip() for line in f if line.strip()]

# Translate
results = {}
translated_count = 0
skipped_count = 0

for name in names:
    translation = translate_name(name)
    if translation:
        results[name] = translation
        translated_count += 1
        print(f"✓ {name} → {translation}")
    else:
        skipped_count += 1
        print(f"✗ {name} (no translation)")

# Save results
with open('batch2_translated.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"✅ Translated: {translated_count}")
print(f"⏭️  Skipped: {skipped_count}")
print(f"📊 Success rate: {translated_count}/{len(names)} ({translated_count*100//len(names)}%)")
print(f"💾 Saved to: batch2_translated.json")
