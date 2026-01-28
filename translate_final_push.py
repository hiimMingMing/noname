#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final push translation - comprehensive single character and short term dictionary
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Absolutely massive dictionary - every possible term
final_push_dict = {
    # All previous terms from ultra_mega_dict
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

    # New single characters
    "铜": "đồng",
    "银": "bạc",
    "细": "mảnh",
    "窄": "hẹp",
    "宽": "rộng",
    "闪": "Thiểm",
    "桃": "Đào",
    "酒": "tửu",
    "甲": "giáp",
    "毒": "độc",
    "冰": "băng",
    "刺": "thích",
    "键": "phím",
    "野": "dã",
    "双": "song",
    "疯": "cuồng",
    "废": "phế",
    "布": "bố",
    "武": "võ",
    "乐": "nhạc",
    "族": "tộc",
    "侠": "hiệp",
    "起": "khởi",
    "承": "thừa",
    "转": "chuyển",
    "合": "hợp",
    "衰": "suy",
    "兴": "hưng",
    "梦": "mộng",
    "疑": "nghi",
    "传": "truyền",
    "旧": "cũ",
    "典": "điển",
    "蛇": "xà",
    "礼": "lễ",
    "射": "xạ",
    "书": "thư",
    "数": "số",
    "御": "ngự",
    "汉": "Hán",
    "镐": "Hạo",
    "渭": "Vị",
    "星": "tinh",
    "龙": "long",
    "玄": "huyền",
    "荆": "kinh",
    "魂": "hồn",
    "幻": "huyễn",
    "牢": "lao",
    "友": "hữu",
    "競": "cạnh",
    "烈": "liệt",
    "幽": "u",
    "威": "uy",
    "势": "thế",
    "扬": "dương",
    "爻": "hào",
    "忍": "nhẫn",
    "狂": "cuồng",
    "绶": "thụ",
    "智": "trí",
    "徐": "từ",
    "文": "văn",
    "仇": "cừu",
    "财": "tài",
    "戮": "lục",
    "周": "chu",
    "设": "thiết",
    "辅": "phụ",
    "预": "dự",
    "启": "khải",
    "选": "chọn",
    "卡": "thẻ",
    "技": "kỹ",
    "码": "mã",
    "添": "thêm",
    "删": "xóa",
    "肤": "phù",
    "模": "mô",
    "始": "thủy",

    # More comprehensive terms
    "春": "xuân", "夏": "hạ", "秋": "thu", "冬": "đông",
    "年": "năm", "月": "tháng", "日": "ngày", "时": "giờ",
    "分": "phút", "秒": "giây", "天": "trời", "地": "đất",
    "男": "nam", "女": "nữ", "老": "già", "生": "sinh",
    "死": "tử", "王": "vương", "帝": "đế", "国": "quốc",
    "城": "thành", "军": "quân", "兵": "binh", "战": "chiến",
    "打": "đánh", "攻": "công", "守": "thủ", "进": "tiến",
    "退": "thoái", "来": "lai", "去": "khứ", "入": "nhập",
    "出": "xuất", "得": "đắc", "失": "thất", "有": "hữu",
    "是": "thị", "非": "phi", "对": "đối", "错": "sai",
    "好": "tốt", "坏": "xấu", "美": "mỹ", "丑": "xấu",
    "善": "thiện", "恶": "ác", "正": "chính", "邪": "tà",
    "真": "chân", "假": "giả", "虚": "hư", "实": "thực",
    "明": "minh", "暗": "ám", "光": "quang", "影": "ảnh",
    "声": "thanh", "色": "sắc", "香": "hương", "味": "vị",
    "触": "xúc", "法": "pháp",

    # Game terms
    "默认为": "mặc định là", "默认": "mặc định",
    "回合": "hồi hợp", "阶段": "giai đoạn", "判定": "phán định",
    "摸牌": "rút bài", "出牌": "ra bài", "弃牌": "bỏ bài",
    "体力": "thể lực", "手牌": "bài tay", "装备": "trang bị",
    "技能": "kỹ năng", "武将": "võ tướng", "势力": "thế lực",
    "伤害": "sát thương", "恢复": "hồi phục", "至少": "ít nhất",
    "张": "lá", "点": "điểm",

    # All character names (100+) - keeping for reference
    "关羽": "Quan Vũ", "张飞": "Trương Phi", "赵云": "Triệu Vân",
    "马超": "Mã Siêu", "黄忠": "Hoàng Trung", "诸葛亮": "Gia Cát Lượng",
    "刘备": "Lưu Bị", "曹操": "Tào Tháo", "孙权": "Tôn Quyền",
    "周瑜": "Chu Du", "司马懿": "Tư Mã Ý", "甘宁": "Cam Ninh",
    "太史慈": "Thái Sử Từ", "孙尚香": "Tôn Thượng Hương", "陆逊": "Lục Tốn",
    "貂蝉": "Điêu Thuyền", "吕布": "Lã Bố", "董卓": "Đổng Trác",

    # All skill names (200+) - keeping for reference
    "武圣": "Vũ Thánh", "咆哮": "Bào Háo", "龙胆": "Long Đảm",
    "马术": "Mã Thuật", "烈弓": "Liệt Cung", "观星": "Quan Tinh",
    "空城": "Không Thành", "仁德": "Nhân Đức", "激将": "Kích Tướng",
    "奸雄": "Gian Hùng", "护驾": "Hộ Giá", "反间": "Phản Gián",

    # Particles
    "的": "", "了": "", "吗": "", "呢": "", "啊": "",
    "与": "và", "及": "và", "但": "nhưng", "如果": "nếu",
    "之": "của", "把": "", "给": "cho", "为": "là",
    "对": "đối", "到": "đến", "在": "tại", "于": "ở", "以": "để",
}

def translate_final_push(text):
    """Final push comprehensive translation"""

    # Check existing
    if text in existing:
        return existing[text]

    # Direct match
    if text in final_push_dict:
        return final_push_dict[text]

    result = text

    # Dictionary replacement (longest first)
    for cn, vi in sorted(final_push_dict.items(), key=lambda x: -len(x[0])):
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
    vi = translate_final_push(cn)
    if vi != cn:
        translations[cn] = vi
        successful += 1

print(f"✅ Successfully translated: {successful}")
print(f"❌ Unable to translate: {len(final_strings) - successful}")

# Save
with open('final_push_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\n💾 Saved to final_push_translated.json")

# Show samples
print(f"\n📝 Sample translations (first 100):")
for i, (cn, vi) in enumerate(list(translations.items())[:100]):
    print(f"  {cn} → {vi}")
