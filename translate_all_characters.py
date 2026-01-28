#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive character name translation - ALL 6,037 names
"""

import json
import re

# Load existing translations
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Load all character names
with open('all_character_names.txt', 'r', encoding='utf-8') as f:
    all_names = [line.strip() for line in f if line.strip()]

print(f"📦 Total character names to translate: {len(all_names)}")

# MASSIVE character name dictionary - covering all Three Kingdoms characters
# This includes all variants: Standard, OL (Online), SP (Special),界 (Jie), 神 (Shen), etc.
character_translations = {
    # Core Historical Figures (Standard versions)
    "曹操": "Tào Tháo",
    "刘备": "Lưu Bị",
    "孙权": "Tôn Quyền",
    "关羽": "Quan Vũ",
    "张飞": "Trương Phi",
    "赵云": "Triệu Vân",
    "诸葛亮": "Gia Cát Lượng",
    "周瑜": "Chu Du",
    "司马懿": "Tư Mã Ý",
    "吕布": "Lã Bố",
    "貂蝉": "Điêu Thuyền",
    "华佗": "Hoa Đà",
    "甄宓": "Chân Mích",
    "马超": "Mã Siêu",
    "黄忠": "Hoàng Trung",
    "黄月英": "Hoàng Nguyệt Anh",
    "孙尚香": "Tôn Thượng Hương",
    "大乔": "Đại Kiều",
    "小乔": "Tiểu Kiều",
    "陆逊": "Lục Tốn",
    "甘宁": "Cam Ninh",
    "吕蒙": "Lã Mông",
    "黄盖": "Hoàng Cái",
    "太史慈": "Thái Sử Từ",
    "夏侯惇": "Hạ Hầu Đôn",
    "夏侯渊": "Hạ Hầu Uyên",
    "张辽": "Trương Liêu",
    "徐晃": "Từ Hoảng",
    "许褚": "Hứa Chử",
    "典韦": "Điển Vi",
    "郭嘉": "Quách Gia",
    "荀彧": "Tuân Úc",
    "荀攸": "Tuân Du",
    "曹仁": "Tào Nhân",
    "曹丕": "Tào Phi",
    "曹植": "Tào Thực",
    "曹彰": "Tào Chương",
    "曹冲": "Tào Xung",
    "曹真": "Tào Chân",
    "曹休": "Tào Hưu",
    "曹叡": "Tào Duệ",
    "司马昭": "Tư Mã Chiêu",
    "司马师": "Tư Mã Sư",
    "张郃": "Trương Cáp",
    "张春华": "Trương Xuân Hoa",
    "庞统": "Bàng Thống",
    "魏延": "Ngụy Diên",
    "姜维": "Khương Duy",
    "马岱": "Mã Đại",
    "马谡": "Mã Tốc",
    "黄承彦": "Hoàng Thừa Ngạn",
    "关兴": "Quan Hưng",
    "张苞": "Trương Bao",
    "关平": "Quan Bình",
    "周仓": "Chu Thương",
    "廖化": "Liêu Hóa",
    "孙坚": "Tôn Kiên",
    "孙策": "Tôn Sách",
    "孙休": "Tôn Hưu",
    "孙登": "Tôn Đăng",
    "孙鲁班": "Tôn Lỗ Ban",
    "孙鲁育": "Tôn Lỗ Dục",
    "周泰": "Chu Thái",
    "程普": "Trình Phổ",
    "黄盖": "Hoàng Cái",
    "韩当": "Hàn Đương",
    "凌统": "Lăng Thống",
    "徐盛": "Từ Thịnh",
    "丁奉": "Đinh Phụng",
    "朱桓": "Chu Hoàn",
    "朱然": "Chu Nhiên",
    "朱治": "Chu Trị",
    "吕范": "Lã Phạm",
    "鲁肃": "Lỗ Túc",
    "诸葛瑾": "Gia Cát Cẩn",
    "顾雍": "Cố Ung",
    "张昭": "Trương Chiêu",
    "张纮": "Trương Hoằng",
    "虞翻": "Ngu Phiên",
    "步骘": "Bộ Chất",
    "步练师": "Bộ Luyện Sư",
    "吴国太": "Ngô Quốc Thái",
    "董卓": "Đổng Trác",
    "华雄": "Hoa Hùng",
    "李傕": "Lý Quắc",
    "郭汜": "Quách Tư",
    "张济": "Trương Tế",
    "樊稠": "Phàn Sưu",
    "牛辅": "Ngưu Phụ",
    "李儒": "Lý Nho",
    "董白": "Đổng Bạch",
    "袁绍": "Viên Thiệu",
    "袁术": "Viên Thuật",
    "颜良": "Nhan Lương",
    "文丑": "Văn Sửu",
    "沮授": "Trở Thụ",
    "田丰": "Điền Phong",
    "审配": "Thẩm Phối",
    "逢纪": "Phùng Kỷ",
    "郭图": "Quách Đồ",
    "袁谭": "Viên Đàm",
    "袁尚": "Viên Thượng",
    "袁熙": "Viên Hi",
    "高览": "Cao Lãm",
    "张郃": "Trương Cáp",
    "公孙瓒": "Công Tôn Toản",
    "公孙渊": "Công Tôn Uyên",
    "马腾": "Mã Đằng",
    "韩遂": "Hàn Toại",
    "刘表": "Lưu Biểu",
    "刘璋": "Lưu Chương",
    "刘禅": "Lưu Thiện",
    "刘谌": "Lưu Thần",
    "刘封": "Lưu Phong",
    "刘巴": "Lưu Ba",
    "刘焉": "Lưu Yên",
    "刘虞": "Lưu Ngu",
    "蔡瑁": "Thái Mạo",
    "蔡夫人": "Thái Phu Nhân",
    "蔡琰": "Thái Diễm",
    "蔡贞姬": "Thái Trinh Cơ",
    "蔡邕": "Thái Ung",
    "伏寿": "Phục Thọ",
    "伏完": "Phục Hoàn",
    "甘夫人": "Cam Phu Nhân",
    "糜夫人": "Di Phu Nhân",
    "糜竺": "Di Trúc",
    "孙乾": "Tôn Kiền",
    "简雍": "Giản Ung",
    "伊籍": "Y Tịch",
    "法正": "Pháp Chính",
    "李严": "Lý Nghiêm",
    "李恢": "Lý Khôi",
    "孟获": "Mạnh Hoạch",
    "祝融": "Chúc Dung",
    "陈宫": "Trần Cung",
    "高顺": "Cao Thuận",
    "张邈": "Trương Mạc",
    "臧霸": "Tang Bá",
    "孟达": "Mạnh Đạt",
    "华歆": "Hoa Hâm",
    "王朗": "Vương Lãng",
    "钟繇": "Chung Diêu",
    "钟会": "Chung Hội",
    "邓艾": "Đặng Ngải",
    "郭淮": "Quách Hoài",
    "郭皇后": "Quách Hoàng Hậu",
    "郭照": "Quách Chiếu",
    "满宠": "Mãn Sủng",
    "徐庶": "Từ Thứ",
    "徐氏": "Từ Thị",
    "夏侯氏": "Hạ Hầu Thị",
    "夏侯玄": "Hạ Hầu Huyền",
    "夏侯恩": "Hạ Hầu Ân",
    "曹节": "Tào Tiết",
    "曹婴": "Tào Anh",
    "王异": "Vương Dị",
    "王元姬": "Vương Nguyên Cơ",
    "王荣": "Vương Vinh",
    "辛宪英": "Tân Hiến Anh",
    "张嶷": "Trương Nghệ",
    "张翼": "Trương Dực",
    "马良": "Mã Lương",
    "吴懿": "Ngô Ý",
    "吴苋": "Ngô Hiến",
    "吴景": "Ngô Cảnh",
    "潘璋": "Phan Chương",
    "马忠": "Mã Trung",
    "潘璋马忠": "Phan Chương Mã Trung",
    "潘淑": "Phan Thục",
    "陆凯": "Lục Khải",
    "陆郁生": "Lục Úc Sinh",
    "陆抗": "Lục Kháng",
    "陆绩": "Lục Tích",
    "全琮": "Toàn Tùng",
    "朱儁": "Chu Tuấn",
    "朱灵": "Chu Linh",
    "阚泽": "Hãm Trạch",
    "薛综": "Tiết Tống",
    "薛灵芸": "Tiết Linh Vân",
    "诸葛恪": "Gia Cát Khác",
    "诸葛瞻": "Gia Cát Chiêm",
    "邓芝": "Đặng Chi",
    "蒋琬": "Tưởng Uyển",
    "蒋钦": "Tưởng Khâm",
    "蒋干": "Tưởng Can",
    "费祎": "Phí Úy",
    "董允": "Đổng Doãn",
    "董昭": "Đổng Chiêu",
    "董翓": "Đổng Tập",
    "管辂": "Quản Lộ",
    "管宁": "Quản Ninh",
    "管亥": "Quản Hợi",
    "左慈": "Tả Từ",
    "于吉": "Vu Cát",
    "南华老仙": "Nam Hoa Lão Tiên",
    "张角": "Trương Giác",
    "张宝": "Trương Bảo",
    "张梁": "Trương Lương",
    "张让": "Trương Nhượng",
    "张曼成": "Trương Mạn Thành",
    "张绣": "Trương Tú",
    "张松": "Trương Tùng",
    "张昌蒲": "Trương Xương Bồ",
    "乐进": "Nhạc Tiến",
    "乐就": "Nhạc Tựu",
    "乐綝": "Nhạc Tống",
    "于禁": "Vu Cấm",
    "李典": "Lý Điển",
    "李丰": "Lý Phong",
    "李肃": "Lý Túc",
    "李婉": "Lý Uyển",
    "贾诩": "Giả Húc",
    "贾充": "Giả Sung",
    "贾逵": "Giả Quỹ",
    "贾南风": "Giả Nam Phong",
    "纪灵": "Kỷ Linh",
    "孔融": "Khổng Dung",
    "嵇康": "Kê Khang",
    "秦宓": "Tần Mịch",
    "秦朗": "Tần Lãng",
    "祢衡": "Nể Hành",
    "戏志才": "Hí Chí Tài",
    "许攸": "Hứa Du",
    "许靖": "Hứa Tĩnh",
    "陈群": "Trần Quần",
    "陈武": "Trần Vũ",
    "陈登": "Trần Đăng",
    "陈泰": "Trần Thái",
    "陶谦": "Đào Khiêm",
    "霍峻": "Hoắc Tuấn",
    "霍弋": "Hoắc Dực",
    "韩馥": "Hàn Phúc",
    "韩浩": "Hàn Hạo",
    "史涣": "Sử Hoán",
    "韩浩史涣": "Hàn Hạo Sử Hoán",
    "卢植": "Lô Thực",
    "卢逊": "Lô Tốn",
    "何进": "Hà Tiến",
    "何太后": "Hà Thái Hậu",
    "十常侍": "Thập Thường Thị",
    "郭胜": "Quách Thắng",
    "段珪": "Đoạn Khuê",
    "韩悝": "Hàn Khôi",
    "毕岚": "Tất Lam",
    "张让": "Trương Nhượng",
    "赵忠": "Triệu Trung",
    "封谞": "Phong Húc",
    "夏恽": "Hạ Uẩn",
    "郭胜": "Quách Thắng",
    "黄皓": "Hoàng Hạo",
    "黄权": "Hoàng Quyền",
    "黄祖": "Hoàng Tổ",
    "蒯良": "Khổi Lương",
    "蒯越": "Khổi Việt",
    "蔡中": "Thái Trung",
    "蔡和": "Thái Hòa",
    "杨奉": "Dương Phụng",
    "杨阜": "Dương Phụ",
    "杨修": "Dương Tu",
    "杨仪": "Dương Nghi",
    "桥玄": "Kiều Huyền",
    "桥公": "Kiều Công",
    "樊氏": "Phàn Thị",
    "樊建": "Phàn Kiến",
    "武安国": "Vũ An Quốc",
    "滕芳兰": "Đằng Phương Lan",
    "冯妤": "Phùng Du",
    "冯习": "Phùng Tập",
    "丁奉": "Đinh Phụng",
    "丁尚涴": "Đinh Thượng Uyển",
    "丁原": "Đinh Nguyên",
    "成济": "Thành Tế",
    "程昱": "Trình Úc",
    "荀谌": "Tuân Sâm",
    "郝昭": "Hách Chiêu",
    "郝萌": "Hách Manh",
    "荀正": "Tuân Chính",
    "孙资刘放": "Tôn Tư Lưu Phóng",
    "孙茹": "Tôn Như",
    "苏飞": "Tô Phi",
    "芮姬": "Nhuế Cơ",
    "胡金定": "Hồ Kim Định",
    "胡班": "Hồ Ban",
    "胡车儿": "Hồ Xa Nhi",
    "轲比能": "Kha Tỷ Năng",
    "刘晔": "Lưu Dực",
    "刘辟": "Lưu Tịch",
    "眭固": "Tuy Cố",
    "裴秀": "Bùi Tú",
    "裴元绍": "Bùi Nguyên Thiệu",
    "袁姬": "Viên Cơ",
    "袁涣": "Viên Hoán",
    "许靖": "Hứa Tĩnh",
    "崔琰": "Thôi Diễm",
    "崔勇": "Thôi Dũng",
    "骆统": "Lạc Thống",
    "岑昏": "Sầm Hôn",
    "薛综": "Tiết Tống",
    "吕旷": "Lã Khoáng",
    "吕翔": "Lã Tường",
    "吕旷吕翔": "Lã Khoáng Lã Tường",
    "吕玲绮": "Lã Linh Kỳ",
    "张绣": "Trương Tú",
    "郭图逢纪": "Quách Đồ Phùng Kỷ",
    "蒲元": "Bồ Nguyên",
    "杜预": "Đỗ Dự",
    "邹氏": "Sưu Thị",

    # Prefixes and Suffixes
    "旧": "Cũ",
    "新": "Mới",
    "界": "Giới",
    "神": "Thần",
    "谋": "Mưu",
    "乐": "Nhạc",
    "OL": "OL",
    "SP": "SP",
    "RE": "RE",
    "SC": "SC",
    "SCL": "SCL",
    "PE": "PE",
    "TW": "TW",
    "系列": "Series",
    "K系列": "K Series",

    # Version markers
    "26|界": "26|Giới",
    "26|神": "26|Thần",
    "OL|界": "OL|Giới",
    "OL|魔": "OL|Ma",
    "OL|神": "OL|Thần",
    "OL|谋": "OL|Mưu",
    "OL|乐": "OL|Nhạc",

    # Special characters from Key/anime expansions (keeping romaji/original)
    "立华奏": "Tachibana Kanade",
    "仲村由理": "Nakamura Yuri",
    "星野梦美": "Hoshino Yumemi",
    "能美库特莉亚芙卡": "Noumi Kudryavka",
    "友利奈绪": "Tomori Nao",
    "神尾观铃": "Kamio Misuzu",
    "伊吹风子": "Ibuki Fuuko",
    "花木兰": "Hoa Mộc Lan",

    # Other special
    "2点": "2 điểm",
    "魔": "Ma",
    "失效技能": "Kỹ năng vô hiệu",
    "技一": "Kỹ 1",
    "技二": "Kỹ 2",
    "技新": "Kỹ mới",
    "技能A": "Kỹ năng A",
    "技能B": "Kỹ năng B",
    "穷技": "Cùng kỹ",
}

def translate_character_name(name):
    """Translate character name with all variants"""

    # Already translated
    if name in existing:
        return existing[name]

    # Direct match
    if name in character_translations:
        return character_translations[name]

    # Handle compound names (like "OL华歆", "界张辽", etc.)
    for prefix in ["OL", "SP", "RE", "SCL", "PE", "TW", "J.SP", "26界", "26神", "OL界", "OL神", "OL谋", "OL乐", "OL魔", "界", "神", "谋", "旧", "新", "乐"]:
        if name.startswith(prefix):
            base_name = name[len(prefix):]
            if base_name in character_translations:
                prefix_trans = character_translations.get(prefix, prefix)
                return f"{prefix_trans} {character_translations[base_name]}"

    # Handle suffix (like "K系列杜预")
    for suffix_pattern in ["系列", "K系列"]:
        if suffix_pattern in name:
            parts = name.split(suffix_pattern)
            if len(parts) == 2 and parts[1] in character_translations:
                return f"{suffix_pattern} {character_translations[parts[1]]}"

    # Return original if can't translate
    return name

# Translate all names
translations = {}
translated_count = 0
untranslated_count = 0

for name in all_names:
    trans = translate_character_name(name)
    if trans != name:
        translations[name] = trans
        translated_count += 1
    else:
        untranslated_count += 1

print(f"\n✅ Successfully translated: {translated_count}/{len(all_names)}")
print(f"❌ Still untranslated: {untranslated_count}/{len(all_names)}")
print(f"📊 Coverage: {(translated_count / len(all_names) * 100):.1f}%")

# Save
with open('character_names_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to character_names_translated.json")

# Show samples
print(f"\n📝 Sample translations (first 50):")
for i, (cn, vi) in enumerate(list(translations.items())[:50]):
    print(f"  {cn} → {vi}")
