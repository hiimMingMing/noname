#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absolute final translation - maximum coverage
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Absolutely complete dictionary
absolute_dict = {
    # New single characters
    "景": "cảnh",
    "亡": "vong",
    "效": "hiệu",
    "图": "đồ",
    "音": "âm",
    "字": "tự",
    "作": "tác",
    "执": "chấp",
    "清": "thanh",
    "播": "bá",
    "存": "tồn",

    # All previous (keeping comprehensive list)
    "铜": "đồng", "银": "bạc", "细": "mảnh", "窄": "hẹp", "宽": "rộng",
    "闪": "Thiểm", "桃": "Đào", "酒": "tửu", "甲": "giáp", "毒": "độc",
    "冰": "băng", "刺": "thích", "键": "phím", "野": "dã", "双": "song",
    "疯": "cuồng", "废": "phế", "布": "bố", "武": "võ", "乐": "nhạc",
    "族": "tộc", "侠": "hiệp", "起": "khởi", "承": "thừa", "转": "chuyển",
    "合": "hợp", "衰": "suy", "兴": "hưng", "梦": "mộng", "疑": "nghi",
    "传": "truyền", "旧": "cũ", "典": "điển", "蛇": "xà", "礼": "lễ",
    "射": "xạ", "书": "thư", "数": "số", "御": "ngự", "汉": "Hán",
    "镐": "Hạo", "渭": "Vị", "星": "tinh", "龙": "long", "玄": "huyền",
    "荆": "kinh", "魂": "hồn", "幻": "huyễn", "牢": "lao", "友": "hữu",
    "競": "cạnh", "烈": "liệt", "幽": "u", "威": "uy", "势": "thế",
    "扬": "dương", "爻": "hào", "忍": "nhẫn", "狂": "cuồng", "绶": "thụ",
    "智": "trí", "徐": "từ", "文": "văn", "仇": "cừu", "财": "tài",
    "戮": "lục", "周": "chu", "设": "thiết", "辅": "phụ", "预": "dự",
    "启": "khải", "选": "chọn", "卡": "thẻ", "技": "kỹ", "码": "mã",
    "添": "thêm", "删": "xóa", "肤": "phù", "模": "mô", "始": "thủy",

    # More skill names
    "应机": "Ứng Cơ",
    "节应": "Tiết Ứng",
    "驰应": "Trì Ứng",
    "断发": "Đoạn Phát",
    "旋风": "Toàn Phong",
    "将驰": "Tướng Trì",
    "将烈": "Tướng Liệt",
    "将略": "Tướng Lược",
    "斩将": "Trảm Tướng",
    "拜将": "Bái Tướng",
    "挟令": "Hiếp Lệnh",
    "扑克": "Poker",

    # All previous comprehensive
    "或": "hoặc", "金": "kim", "某": "mỗi", "人": "người", "杀": "Sát",
    "零": "không", "一": "một", "二": "hai", "三": "ba", "四": "bốn",
    "五": "năm", "六": "sáu", "七": "bảy", "八": "tám", "九": "chín",
    "十": "mười", "百": "trăm", "千": "nghìn", "两": "hai", "万": "vạn",
    "亿": "ức", "次": "lần", "无": "vô", "牌": "bài", "被": "bị",
    "副": "phó", "将": "tướng", "个": "cái", "栏": "thanh", "你": "ngươi",
    "向": "hướng", "胜": "thắng", "负": "thua", "平": "hòa", "至": "đến",
    "主": "chủ", "手": "tay", "新": "mới", "君": "quân", "谋": "Mưu",
    "界": "Giới", "标": "chuẩn", "鼎": "đỉnh", "故": "cũ", "魔": "ma",
    "慢": "chậm", "中": "trung", "快": "nhanh", "本": "bản", "矮": "thấp",
    "高": "cao", "大": "lớn", "小": "nhỏ", "长": "dài", "短": "ngắn",
    "强": "mạnh", "弱": "yếu", "多": "nhiều", "少": "ít", "全": "toàn",
    "半": "nửa", "空": "trống", "满": "đầy", "开": "mở", "关": "đóng",
    "上": "trên", "下": "dưới", "左": "trái", "右": "phải", "前": "trước",
    "后": "sau", "内": "trong", "外": "ngoài", "东": "đông", "南": "nam",
    "西": "tây", "北": "bắc", "魏": "Ngụy", "蜀": "Thục", "吴": "Ngô",
    "群": "Quần", "晋": "Tấn",

    # All game terms
    "默认为": "mặc định là", "默认": "mặc định",
    "回合": "hồi hợp", "阶段": "giai đoạn", "判定": "phán định",
    "摸牌": "rút bài", "出牌": "ra bài", "弃牌": "bỏ bài",
    "体力": "thể lực", "手牌": "bài tay", "装备": "trang bị",
    "技能": "kỹ năng", "武将": "võ tướng", "势力": "thế lực",
    "伤害": "sát thương", "恢复": "hồi phục", "至少": "ít nhất",
    "张": "lá", "点": "điểm",

    # All character names
    "乐就": "Nhạc Tựu", "乐綝": "Nhạc Tống", "华歆": "Hoa Hâm", "华雄": "Hoa Hùng",
    "贾诩": "Giả Húc", "贾逵": "Giả Quỹ", "贾充": "Giả Sung", "沮授": "Trở Thụ",
    "纪灵": "Kỷ Linh", "笮融": "Trạch Dung", "逢纪": "Phùng Kỷ", "许褚": "Hứa Chử",
    "刘辟": "Lưu Tịch", "刘禅": "Lưu Thiện", "甄宓": "Chân Mích", "孙綝": "Tôn Tốn",
    "李傕": "Lý Quắc", "李遗": "Lý Di", "张嶷": "Trương Nghệ", "蒋干": "Tưởng Can",
    "雷薄": "Lôi Bạc", "吕蒙": "Lã Mông", "于禁": "Vu Cấm", "赵累": "Triệu Lũy",
    "史阿": "Sử A", "凯撒": "Caesar", "端蒙": "Đoan Mông", "妹喜": "Muội Hỉ",
    "半藏": "Hanzou", "少微": "Thiếu Vi", "少昊": "Thiếu Hạo", "安卡": "An Ka",
    "卡玛": "Karma", "梼杌": "Đào Ngột", "露娜": "Luna",

    # All skill names
    "重身": "Trùng Thân", "畜鸣": "Súc Minh", "聆乐": "Linh Nhạc",
    "没矢": "Một Thỉ", "没欲": "Một Dục", "血裔": "Huyết Duệ",
    "血卫": "Huyết Vệ", "血诏": "Huyết Chiếu", "血偿": "Huyết Thường",
    "血拼": "Huyết Bính", "血途": "Huyết Đồ", "行殇": "Hành Thương",
    "节行": "Tiết Hành", "天行": "Thiên Hành", "神行": "Thần Hành",
    "镇行": "Trấn Hành", "行图": "Hành Đồ", "绝行": "Tuyệt Hành",
    "好施": "Hảo Thí", "荐降": "Tiến Hàng", "破降": "Phá Hàng",
    "拒降": "Cự Hàng", "应势": "Ứng Thế", "应援": "Ứng Viện",

    # Particles
    "的": "", "了": "", "吗": "", "呢": "", "啊": "",
    "与": "và", "及": "và", "但": "nhưng", "如果": "nếu",
    "之": "của", "把": "", "给": "cho", "为": "là",
    "对": "đối", "到": "đến", "在": "tại", "于": "ở", "以": "để",
}

def translate_absolute(text):
    """Absolute final translation"""

    # Check existing
    if text in existing:
        return existing[text]

    # Direct match
    if text in absolute_dict:
        return absolute_dict[text]

    result = text

    # Pattern: skill/character name with array notation
    match = re.match(r'^\s*],\s*(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in absolute_dict:
            return result.replace(name, absolute_dict[name])

    # Pattern: just name with colon bracket
    match = re.match(r'^(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in absolute_dict:
            return result.replace(name, absolute_dict[name])

    # Dictionary replacement (longest first)
    for cn, vi in sorted(absolute_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Cleanup
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Read final push strings
with open('final_push.txt', 'r', encoding='utf-8') as f:
    final_strings = [line.strip() for line in f if line.strip()]

print(f"📦 Strings to translate: {len(final_strings)}")

# Translate
translations = {}
successful = 0
for cn in final_strings:
    vi = translate_absolute(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(final_strings) - successful}")

# Save
with open('absolute_final_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to absolute_final_translated.json")

# Show samples
print(f"\n📝 Sample translations (first 100):")
for i, (cn, vi) in enumerate(list(translations.items())[:100]):
    if len(cn) < 100:
        print(f"  {cn} → {vi}")
