#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate 'other' category strings
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Massive character name + term dictionary
other_dict = {
    # Character names - Extended list
    "乐就": "Nhạc Tựu",
    "乐綝": "Nhạc Tống",
    "华歆": "Hoa Hâm",
    "华雄": "Hoa Hùng",
    "贾诩": "Giả Húc",
    "贾逵": "Giả Quỹ",
    "贾充": "Giả Sung",
    "沮授": "Trở Thụ",
    "纪灵": "Kỷ Linh",
    "笮融": "Trạch Dung",
    "逢纪": "Phùng Kỷ",
    "许褚": "Hứa Chử",
    "刘辟": "Lưu Tịch",
    "刘禅": "Lưu Thiện",
    "甄宓": "Chân Mích",
    "孙綝": "Tôn Tốn",
    "李傕": "Lý Quắc",
    "李遗": "Lý Di",
    "张嶷": "Trương Nghệ",
    "蒋干": "Tưởng Can",
    "雷薄": "Lôi Bạc",
    "吕蒙": "Lã Mông",
    "于禁": "Vu Cấm",
    "赵累": "Triệu Lũy",
    "史阿": "Sử A",
    "凯撒": "Caesar",
    "端蒙": "Đoan Mông",
    "妹喜": "Muội Hỉ",
    "半藏": "Hanzou",
    "少微": "Thiếu Vi",
    "孙坚": "Tôn Kiên",
    "孙权": "Tôn Quyền",
    "孙策": "Tôn Sách",
    "关羽": "Quan Vũ",
    "张飞": "Trương Phi",
    "赵云": "Triệu Vân",
    "马超": "Mã Siêu",
    "黄忠": "Hoàng Trung",
    "诸葛亮": "Gia Cát Lượng",
    "刘备": "Lưu Bị",
    "曹操": "Tào Tháo",
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
    "黄盖": "Hoàng Cái",
    "程普": "Trình Phổ",
    "丁奉": "Đinh Phụng",
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

    # Card count
    "张": "lá",
    "2张": "2 lá",
    "3张": "3 lá",
    "5张": "5 lá",
    "30张": "30 lá",
    "50张": "50 lá",
    "80张": "80 lá",

    # Common phrases
    "的身份牌": "thẻ thân phận",
    "默认为": "mặc định là",
    "，当": ", khi",
    "撤销": "hoàn tác",

    # All previous terms
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
    "至少": "ít nhất",
    "放置": "đặt",
    "虚拟": "ảo",
    "杀害": "sát hại",
    "进行": "tiến hành",
    "解除": "giải trừ",
    "新杀": "Tân Sát",
    "挟令": "Hiếp lệnh",
    "扑克": "Poker",
    "较慢": "khá chậm",
    "较快": "khá nhanh",
    "很快": "rất nhanh",
    "托管": "Ủy thác",
    "无限": "vô hạn",
    "默认": "mặc định",
    "新版": "bản mới",
    "旧版": "bản cũ",
    "隐藏": "ẩn",
    "显示": "hiện",
    "音乐": "âm nhạc",
    "自定": "tự định",
    "表情": "biểu cảm",
    "简约": "giản ước",
    "自动": "tự động",
    "击杀": "kích sát",
    "混合": "hỗn hợp",
    "缩放": "thu phóng",
    "抖动": "rung",
    "黄色": "vàng",
    "绿色": "xanh lá",
    "紫色": "tím",
    "红色": "đỏ",
    "蓝色": "xanh dương",
    "橙色": "cam",
    "黑色": "đen",
    "白色": "trắng",
    "发动": "phát động",
    "响应": "đáp ứng",
    "使用": "sử dụng",
    "打出": "đánh ra",
    "获得": "đạt được",
    "失去": "mất",
    "展示": "hiện",
    "亮出": "lộ ra",
    "移动": "di chuyển",
    "移去": "loại bỏ",
    "贴上": "dán lên",
    "视为": "xem như",
    "受到": "nhận",
    "造成": "gây ra",
    "选择": "chọn",
    "交换": "đổi",
    "位置": "vị trí",
    "卡牌": "bài phép",
    "点击": "bấm",
    "拖动": "kéo",
    "评级": "đánh giá",
    "演奏": "trình diễn",
    "被伪装": "bị ngụy trang",
    "缺少": "thiếu",
    "参数": "tham số",
    "标签": "nhãn",
    "皮肤": "skin",
    "更改": "thay đổi",
    "预亮": "sẵn sàng",
    "自动发动": "tự động phát động",
    "点击发动": "bấm để phát động",
    "此牌": "bài này",
    "等待中": "đang đợi",
    "暂时": "tạm thời",
    "失效": "vô hiệu",
    "无效": "không hợp lệ",
    "技能ID": "ID kỹ năng",
    "牌库": "kho bài",
    "从": "từ",
    "中": "trong",
    "给": "cho",
    "为": "là",
    "是": "là",
    "的": "",
    "了": "",
    "与": "và",
    "或": "hoặc",
    "及": "và",
    "但": "nhưng",
    "如果": "nếu",
    "时": "khi",
    "后": "sau",
    "前": "trước",
    "之": "của",
    "将": "sẽ",
    "被": "bị",
    "把": "",
    "对": "đối",
    "向": "hướng",
    "到": "đến",
    "在": "tại",
    "于": "ở",
    "以": "để",
}

def translate_other(text):
    """Translate other category strings"""

    # Check existing
    if text in existing:
        return existing[text]

    # Direct match
    if text in other_dict:
        return other_dict[text]

    result = text

    # Pattern replacements
    # Character names with colons (list format)
    result = re.sub(r'(\w+): \[', lambda m: other_dict.get(m.group(1), m.group(1)) + ': [', result)

    # Numbers + cards
    result = re.sub(r'(\d+)张', r'\1 lá', result)

    # Dictionary replacement (longest first)
    for cn, vi in sorted(other_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Cleanup
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Read other strings
with open('other_to_translate.txt', 'r', encoding='utf-8') as f:
    other_strings = [line.strip() for line in f if line.strip()]

print(f"📦 Strings to translate: {len(other_strings)}")

# Translate
translations = {}
successful = 0
for cn in other_strings:
    vi = translate_other(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(other_strings) - successful}")

# Save
with open('other_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to other_translated.json")

# Show samples
print(f"\n📝 Sample translations:")
for i, (cn, vi) in enumerate(list(translations.items())[:40]):
    if len(cn) < 100 and len(vi) < 100:
        print(f"  {cn}")
        print(f"  → {vi}")
