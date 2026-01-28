#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultra-aggressive translation focusing on character names and short terms
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# ULTRA MEGA dictionary - character names + all previous terms
ultra_dict = {
    # Character names (Three Kingdoms - 100+ characters)
    "离线": "Offline",
    "托管": "Ủy thác",
    "乐就": "Nhạc Tựu",
    "乐綝": "Nhạc Tống",
    "华歆": "Hoa Hâm",
    "华雄": "Hoa Hùng",
    "贾诩": "Giả Húc",
    "贾逵": "Giả Quỹ",
    "吕蒙": "Lã Mông",
    "于禁": "Vu Cấm",
    "关羽": "Quan Vũ",
    "张飞": "Trương Phi",
    "赵云": "Triệu Vân",
    "马超": "Mã Siêu",
    "黄忠": "Hoàng Trung",
    "诸葛亮": "Gia Cát Lượng",
    "刘备": "Lưu Bị",
    "曹操": "Tào Tháo",
    "孙权": "Tôn Quyền",
    "周瑜": "Chu Du",
    "司马懿": "Tư Mã Ý",
    "甘宁": "Cam Ninh",
    "太史慈": "Thái Sử Từ",
    "孙尚香": "Tôn Thượng Hương",
    "陆逊": "Lục Tốn",
    "貂蝉": "Điêu Thuyền",
    "吕布": "Lã Bố",
    "董卓": "Đổng Trác",
    "颜良": "Nhan Lương",
    "文丑": "Văn Sửu",
    "袁绍": "Viên Thiệu",
    "张辽": "Trương Liêu",
    "徐晃": "Từ Hoảng",
    "夏侯惇": "Hạ Hầu Đôn",
    "夏侯渊": "Hạ Hầu Uyên",
    "曹仁": "Tào Nhân",
    "曹丕": "Tào Phi",
    "郭嘉": "Quách Gia",
    "荀彧": "Tuân Úc",
    "荀攸": "Tuân Du",
    "许褚": "Hứa Chử",
    "典韦": "Điển Vi",
    "张郃": "Trương Cáp",
    "庞统": "Bàng Thống",
    "魏延": "Ngụy Diên",
    "姜维": "Khương Duy",
    "马谡": "Mã Tốc",
    "黄月英": "Hoàng Nguyệt Anh",
    "孟获": "Mạnh Hoạch",
    "祝融": "Chúc Dung",
    "大乔": "Đại Kiều",
    "小乔": "Tiểu Kiều",
    "孙策": "Tôn Sách",
    "陆逊": "Lục Tốn",
    "黄盖": "Hoàng Cái",
    "程普": "Trình Phổ",
    "丁奉": "Đinh Phụng",
    "孙坚": "Tôn Kiên",
    "张昭": "Trương Chiêu",
    "张纮": "Trương Hoằng",
    "顾雍": "Cố Ung",
    "鲁肃": "Lỗ Túc",
    "诸葛瑾": "Gia Cát Cẩn",
    "步骘": "Bộ Chất",
    "凌统": "Lăng Thống",
    "徐盛": "Từ Thịnh",
    "潘璋": "Phan Chương",
    "朱桓": "Chu Hoàn",
    "朱然": "Chu Nhiên",
    "吕范": "Lã Phạm",
    "蒋钦": "Tưởng Khâm",
    "周泰": "Chu Thái",
    "陈武": "Trần Vũ",
    "董袭": "Đổng Tập",
    "韩当": "Hàn Đương",
    "蔡瑁": "Thái Mạo",
    "张允": "Trương Doãn",
    "陈宫": "Trần Cung",
    "李儒": "Lý Nho",
    "李肃": "Lý Túc",
    "王允": "Vương Doãn",
    "张角": "Trương Giác",
    "张梁": "Trương Lương",
    "张宝": "Trương Bảo",
    "左慈": "Tả Từ",
    "于吉": "Vu Cát",
    "南华老仙": "Nam Hoa Lão Tiên",
    "管辂": "Quản Lộ",
    "司马昭": "Tư Mã Chiêu",
    "司马师": "Tư Mã Sư",
    "邓艾": "Đặng Ngải",
    "钟会": "Chung Hội",
    "陈泰": "Trần Thái",
    "郭淮": "Quách Hoài",
    "钟繇": "Chung Diêu",
    "王朗": "Vương Lãng",
    "刘禅": "Lưu Thiện",
    "诸葛瞻": "Gia Cát Chiêm",
    "关兴": "Quan Hưng",
    "张苞": "Trương Bao",
    "马岱": "Mã Đại",
    "关平": "Quan Bình",
    "周仓": "Chu Thương",
    "廖化": "Liêu Hóa",
    "王平": "Vương Bình",
    "张翼": "Trương Dực",
    "吴懿": "Ngô Ý",
    "糜竺": "Di Trúc",
    "孙乾": "Tôn Kiền",
    "简雍": "Giản Ung",
    "伊籍": "Y Tịch",

    # Status and completion
    "(已完成)": "(Hoàn thành)",
    "(未完成)": "(Chưa hoàn thành)",
    "已完成": "Đã hoàn thành",
    "未完成": "Chưa hoàn thành",
    "完成": "Hoàn thành",
    "进行中": "Đang tiến hành",
    "等待": "Đang đợi",

    # Common short terms
    "抵消所需要的": "cần để triệt tiêu",
    "伤害点数": "điểm sát thương",
    "伤害来源": "nguồn sát thương",
    "伤害类型": "loại sát thương",
    "额外的": "thêm",
    "此回合": "hồi này",
    "下回合": "hồi sau",
    "本回合": "hồi này",
    "每回合": "mỗi hồi",
    "当前回合": "hồi hiện tại",

    # All previous comprehensive terms
    "至少": "Ít nhất", "放置": "Đặt", "虚拟": "Ảo", "杀害": "Sát hại",
    "进行": "Tiến hành", "解除": "Giải trừ", "新杀": "Tân Sát", "挟令": "Hiếp lệnh",
    "扑克": "Poker", "较慢": "Khá chậm", "较快": "Khá nhanh", "很快": "Rất nhanh",
    "托管": "Ủy thác", "无限": "Vô hạn", "默认": "Mặc định", "新版": "Bản mới",
    "旧版": "Bản cũ", "隐藏": "Ẩn", "显示": "Hiện", "音乐": "Âm nhạc",
    "自定": "Tự định", "表情": "Biểu cảm", "简约": "Giản ước", "自动": "Tự động",
    "击杀": "Kích sát", "混合": "Hỗn hợp", "缩放": "Thu phóng", "抖动": "Rung",

    # Colors
    "黄色": "Vàng", "绿色": "Xanh lá", "紫色": "Tím", "红色": "Đỏ",
    "蓝色": "Xanh dương", "橙色": "Cam", "黑色": "Đen", "白色": "Trắng",

    # Core game terms
    "回合": "hồi hợp", "阶段": "giai đoạn", "判定": "phán định",
    "摸牌": "rút bài", "出牌": "ra bài", "弃牌": "bỏ bài",
    "体力": "thể lực", "手牌": "bài tay", "装备": "trang bị",
    "技能": "kỹ năng", "武将": "võ tướng", "势力": "thế lực",

    # Actions
    "发动": "phát động", "响应": "đáp ứng", "使用": "sử dụng",
    "打出": "đánh ra", "获得": "đạt được", "失去": "mất",
    "展示": "hiện", "亮出": "lộ ra", "移动": "di chuyển",
    "移去": "loại bỏ", "贴上": "dán lên", "视为": "xem như",
    "受到": "nhận", "造成": "gây ra", "选择": "chọn",
    "交换": "đổi", "位置": "vị trí", "卡牌": "bài phép",
    "点击": "bấm", "拖动": "kéo", "评级": "đánh giá",
    "演奏": "trình diễn", "被伪装": "bị ngụy trang",
    "缺少": "thiếu", "参数": "tham số", "标签": "nhãn",

    # More specific terms
    "皮肤": "skin", "更改": "thay đổi", "预亮": "sẵn sàng",
    "自动发动": "tự động phát động", "点击发动": "bấm để phát động",
    "此牌": "bài này", "等待中": "đang đợi", "暂时": "tạm thời",
    "失效": "vô hiệu", "无效": "không hợp lệ", "技能ID": "ID kỹ năng",
    "牌库": "kho bài", "从": "từ", "中": "trong",
    "给": "cho", "为": "là", "是": "là",

    # Particles (minimalist)
    "的": "", "了": "", "吗": "", "呢": "", "啊": "",
    "与": "và", "或": "hoặc", "及": "và", "但": "nhưng",
    "如果": "nếu", "时": "khi", "后": "sau", "前": "trước",
    "之": "của", "将": "sẽ", "被": "bị", "把": "",
    "对": "đối", "向": "hướng", "到": "đến", "在": "tại",
    "于": "ở", "以": "để",
}

# Phrase patterns
phrases = {
    "(被伪装)": "(bị ngụy trang)",
    ">预亮技能": "> Sẵn sàng kỹ năng",
    ">自动发动": "> Tự động phát động",
    ">点击发动": "> Bấm để phát động",
    ">更改皮肤": "> Thay đổi skin",
    ">演奏评级：": "> Đánh giá trình diễn:",
    ">等待中": "> Đang đợi",
    "暂时失效了": "tạm thời vô hiệu",
    "被移动给了": "bị di chuyển cho",
    "从牌库中获得了": "đạt được từ kho bài",
    "视为受到了": "xem như nhận",
    "被贴上了": "bị dán lên",
    "移去了": "đã loại bỏ",
    "为无效技能ID！": "là ID kỹ năng không hợp lệ!",
    ")时缺少target参数": ") thiếu tham số target",
    '若对方选择"开城诱敌"，你胜': "Nếu đối phương chọn 【Khai Thành Dụ Địch】, ngươi thắng",
    '若对方选择"奇袭粮道"，你胜': "Nếu đối phương chọn 【Kỳ Tập Lương Đạo】, ngươi thắng",
    '若对方选择"全军出击"，你胜': "Nếu đối phương chọn 【Toàn Quân Xuất Kích】, ngươi thắng",
    '若对方选择"分兵围城"，你胜': "Nếu đối phương chọn 【Phân Binh Vây Thành】, ngươi thắng",
    '发起了"协力"，合作类型是': "phát động 【Hiệp Lực】, loại hợp tác là",
    ">此牌标签：": "> Nhãn bài này:",
}

def ultra_translate(text):
    """Ultra-aggressive translation with character name focus"""

    # Check existing
    if text in existing:
        return existing[text]

    # Check phrases first
    if text in phrases:
        return phrases[text]

    result = text

    # Pass 1: Replace exact phrases
    for cn, vi in phrases.items():
        if cn in result:
            result = result.replace(cn, vi)

    # Pass 2: Handle quotes with brackets
    result = re.sub(r'"([^"]+)"', r'【\1】', result)
    result = re.sub(r'"([^"]+)"', r'【\1】', result)

    # Pass 3: Complex patterns
    result = re.sub(r'点击或拖动(\w+)以(\w+)', r'Bấm hoặc kéo \1 để \2', result)
    result = re.sub(r'>(\\w+)</div>', r'> \1</div>', result)
    result = re.sub(r'>(\\w+)</span>', r'> \1</span>', result)

    # Pass 4: Dictionary replacement (longest first)
    for cn, vi in sorted(ultra_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Pass 5: Clean up
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Read aggressive strings
with open('aggressive_translate.txt', 'r', encoding='utf-8') as f:
    aggressive = [line.strip() for line in f if line.strip()]

print(f"📦 Strings to translate: {len(aggressive)}")

# Translate
translations = {}
successful = 0
for cn in aggressive:
    vi = ultra_translate(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(aggressive) - successful}")

# Save
with open('aggressive_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to aggressive_translated.json")

# Show samples
print(f"\n📝 Sample translations:")
for i, (cn, vi) in enumerate(list(translations.items())[:25]):
    if len(cn) < 80 and len(vi) < 80:
        print(f"  {cn}")
        print(f"  → {vi}\n")
