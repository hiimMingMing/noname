#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate innerHTML strings with comprehensive dictionary
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Comprehensive innerHTML dictionary
innerHTML_dict = {
    # Time units
    "秒": "giây",
    "1秒": "1 giây",
    "5秒": "5 giây",
    "10秒": "10 giây",
    "15秒": "15 giây",
    "20秒": "20 giây",
    "30秒": "30 giây",
    "60秒": "60 giây",

    # Person count
    "人": "người",
    "1人": "1 người",
    "2人": "2 người",
    "3人": "3 người",
    "4人": "4 người",
    "5人": "5 người",
    "6人": "6 người",
    "8人": "8 người",
    "10人": "10 người",
    "12人": "12 người",
    "16人": "16 người",
    "20人": "20 người",
    "24人": "24 người",
    "40人": "40 người",

    # Factions (Three Kingdoms)
    "魏：": "Ngụy:",
    "蜀：": "Thục:",
    "吴：": "Ngô:",
    "群：": "Quần:",
    "晋：": "Tấn:",
    "西：": "Tây:",
    "魏": "Ngụy",
    "蜀": "Thục",
    "吴": "Ngô",
    "群": "Quần",
    "晋": "Tấn",

    # Game versions/expansions
    "TW神": "TW Thần",
    "TW将": "TW Tướng",
    "TW谋": "TW Mưu",
    "OL神": "OL Thần",
    "OL界": "OL Giới",
    "OL谋": "OL Mưu",
    "OL乐": "OL Nhạc",
    "界SP": "Giới SP",
    "神": "Thần",
    "谋": "Mưu",
    "界": "Giới",

    # UI elements
    "键：": "Phím:",
    "栏：": "Thanh:",
    "数+1": "Số +1",
    "（与": "(với",

    # Common game terms (from mega dict)
    "回合": "hồi hợp",
    "阶段": "giai đoạn",
    "判定": "phán định",
    "摸牌": "rút bài",
    "出牌": "ra bài",
    "弃牌": "bỏ bài",
    "体力": "thể lực",
    "手牌": "bài tay",
    "装备": "trang bị",
    "技能": "kỹ năng",
    "武将": "võ tướng",
    "势力": "thế lực",
    "伤害": "sát thương",
    "恢复": "hồi phục",
    "摸": "rút",
    "张": "lá",
    "牌": "bài",
    "点": "điểm",
    "次": "lần",
    "距离": "khoảng cách",
    "攻击范围": "tầm đánh",
    "限定技": "hạn định",
    "锁定技": "toả định",
    "觉醒技": "giác tỉnh",
    "主公技": "chủ công",
    "转换技": "chuyển đổi",
    "使用": "sử dụng",
    "弃置": "hủy bỏ",
    "获得": "đạt được",
    "失去": "mất",
    "展示": "hiện",
    "观看": "xem",
    "选择": "chọn",
    "目标": "mục tiêu",
    "来源": "nguồn",
    "当前": "hiện tại",
    "上限": "giới hạn",
    "额外": "thêm",
    "至少": "ít nhất",
    "至多": "nhiều nhất",
    "最多": "tối đa",
    "最少": "tối thiểu",
    "可以": "có thể",
    "必须": "phải",
    "若": "nếu",
    "则": "thì",
    "否则": "ngược lại",
    "然后": "sau đó",
    "直到": "cho đến",
    "结束": "kết thúc",
    "开始": "bắt đầu",
    "准备": "chuẩn bị",
    "开局": "khai cuộc",
    "结算": "kết toán",
    "发动": "phát động",
    "触发": "kích hoạt",
    "响应": "đáp ứng",
    "视为": "xem như",
    "对": "đối",
    "造成": "gây ra",
    "受到": "nhận",
    "濒死": "hấp hối",
    "阵亡": "trận vong",
    "复活": "phục sinh",
    "横置": "ngang",
    "重置": "dọc",
    "翻面": "lật",
    "明置": "úp",
    "暗置": "ngửa",
    "移动": "di chuyển",
    "交换": "đổi",
    "替换": "thay",
    "增加": "tăng",
    "减少": "giảm",
    "修改": "sửa",
    "变更": "đổi",
    "取消": "hủy",
    "无效": "vô hiệu",
    "有效": "hữu hiệu",
    "生效": "có hiệu lực",
    "失效": "mất hiệu lực",
    "持续": "trì tục",
    "永久": "vĩnh viễn",
    "暂时": "tạm thời",
    "立即": "lập tức",
    "延迟": "trì hoãn",
    "跳过": "bỏ qua",
    "额外的": "thêm",
    "所有": "tất cả",
    "任意": "bất kỳ",
    "随机": "ngẫu nhiên",
    "指定": "chỉ định",
    "自选": "tự chọn",
    "自己": "bản thân",
    "其他": "khác",
    "所有其他": "tất cả khác",
    "除你外": "trừ ngươi",
    "包括": "bao gồm",
    "不包括": "không bao gồm",
    "仅": "chỉ",
    "等于": "bằng",
    "大于": "lớn hơn",
    "小于": "nhỏ hơn",
    "不少于": "không ít hơn",
    "不超过": "không quá",
    "范围内": "trong phạm vi",
    "之内": "bên trong",
    "之外": "bên ngoài",
    "为止": "cho tới khi",
    "或": "hoặc",
    "且": "và",
    "并": "đồng thời",
    "从": "từ",
    "到": "đến",
    "于": "ở",
    "在": "tại",
    "对其": "đối với họ",
    "令其": "khiến họ",
    "改为": "đổi thành",
    "代替": "thay thế",
    "作为": "làm",
    "成为": "trở thành",
    "成功": "thành công",
    "失败": "thất bại",
    "完成": "hoàn thành",
    "取消": "hủy bỏ",
    "确定": "xác nhận",
    "确认": "xác nhận",
    "可选": "tùy chọn",
    "必选": "bắt buộc",
}

def translate_innerHTML(text):
    """Translate innerHTML strings"""

    # Check existing
    if text in existing:
        return existing[text]

    # Direct match
    if text in innerHTML_dict:
        return innerHTML_dict[text]

    result = text

    # Pattern replacements
    # Numbers + units
    result = re.sub(r'(\d+)秒', r'\1 giây', result)
    result = re.sub(r'(\d+)人', r'\1 người', result)
    result = re.sub(r'(\d+)次', r'\1 lần', result)
    result = re.sub(r'(\d+)点', r'\1 điểm', result)
    result = re.sub(r'(\d+)张', r'\1 lá', result)

    # Dictionary replacement (longest first)
    for cn, vi in sorted(innerHTML_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Cleanup
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Read innerHTML strings
with open('innerHTML_to_translate.txt', 'r', encoding='utf-8') as f:
    innerHTML_strings = [line.strip() for line in f if line.strip()]

print(f"📦 Strings to translate: {len(innerHTML_strings)}")

# Translate
translations = {}
successful = 0
for cn in innerHTML_strings:
    vi = translate_innerHTML(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(innerHTML_strings) - successful}")

# Save
with open('innerHTML_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to innerHTML_translated.json")

# Show samples
print(f"\n📝 Sample translations:")
for i, (cn, vi) in enumerate(list(translations.items())[:30]):
    print(f"  {cn} → {vi}")
