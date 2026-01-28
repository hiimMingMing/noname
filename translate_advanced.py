#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced translation with comprehensive rules
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# MASSIVE comprehensive dictionary - expanded even more
mega_dict = {
    # All previous terms
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

    # Actions - MASSIVE expansion
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
    "牌库": "kho bài", "从": "từ", "中": "trong", "了": "",
    "给": "cho", "为": "là", "是": "là",

    # Strategy terms
    "若对方选择": "Nếu đối phương chọn",
    "你胜": "ngươi thắng",
    "开城诱敌": "Khai Thành Dụ Địch",
    "奇袭粮道": "Kỳ Tập Lương Đạo",
    "全军出击": "Toàn Quân Xuất Kích",
    "分兵围城": "Phân Binh Vây Thành",
    "协力": "Hiệp Lực",
    "合作类型": "loại hợp tác",
    "发起了": "đã phát động",

    # HTML/UI specific
    "点击或拖动两张牌以交换位置": "Bấm hoặc kéo hai lá bài để đổi vị trí",
    "点击一张牌并点击其他区域": "Bấm một lá bài rồi bấm vùng khác",
    "拖动到其他区域以移动卡牌": "kéo đến vùng khác để di chuyển bài phép",
    "其他区域": "vùng khác",
    "以": "để",

    # Common particles and connectors
    "的": "", "了": "", "吗": "", "呢": "", "啊": "",
    "与": "và", "或": "hoặc", "及": "và", "但": "nhưng",
    "如果": "nếu", "时": "khi", "后": "sau", "前": "trước",
    "之": "của", "将": "sẽ", "被": "bị", "把": "",
    "给": "cho", "对": "đối", "向": "hướng", "从": "từ",
    "到": "đến", "在": "tại", "于": "ở", "以": "để",
}

# Game-specific phrases
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

def advanced_translate(text):
    """Advanced translation with multiple passes"""

    # Check existing
    if text in existing:
        return existing[text]

    # Check phrases first (exact matches)
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
    result = re.sub(r'>(\w+)</div>', r'> \1</div>', result)
    result = re.sub(r'>(\w+)</span>', r'> \1</span>', result)

    # Pass 4: Dictionary replacement (longest first)
    for cn, vi in sorted(mega_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Pass 5: Clean up multiple spaces
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Read remaining meaningful strings
with open('remaining_meaningful.txt', 'r', encoding='utf-8') as f:
    remaining = [line.strip() for line in f if line.strip()]

print(f"📦 Strings to translate: {len(remaining)}")

# Translate
translations = {}
successful = 0
for cn in remaining:
    vi = advanced_translate(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(remaining) - successful}")

# Save
with open('remaining_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to remaining_translated.json")

# Show samples
print(f"\n📝 Sample translations:")
for i, (cn, vi) in enumerate(list(translations.items())[:20]):
    if len(cn) < 80 and len(vi) < 80:
        print(f"  {cn}")
        print(f"  → {vi}\n")
