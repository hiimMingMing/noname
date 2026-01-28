#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultra comprehensive translation for all remaining strings
"""

import json
import re

# Load existing
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# MASSIVE comprehensive dictionary - everything
ultra_mega_dict = {
    # Single character terms
    "或": "hoặc",
    "金": "kim",
    "某": "mỗi",
    "人": "người",
    "杀": "Sát",
    "零": "không",
    "一": "một",
    "二": "hai",
    "三": "ba",
    "四": "bốn",
    "五": "năm",
    "六": "sáu",
    "七": "bảy",
    "八": "tám",
    "九": "chín",
    "十": "mười",
    "百": "trăm",
    "千": "nghìn",
    "两": "hai",
    "万": "vạn",
    "亿": "ức",
    "次": "lần",
    "无": "vô",
    "牌": "bài",
    "被": "bị",
    "副": "phó",
    "将": "tướng",
    "个": "cái",
    "栏": "thanh",
    "你": "ngươi",
    "向": "hướng",
    "胜": "thắng",
    "负": "thua",
    "平": "hòa",
    "至": "đến",
    "主": "chủ",
    "手": "tay",
    "新": "mới",
    "君": "quân",
    "谋": "Mưu",
    "界": "Giới",
    "标": "chuẩn",
    "鼎": "đỉnh",
    "故": "cũ",
    "魔": "ma",
    "慢": "chậm",
    "中": "trung",
    "快": "nhanh",
    "本": "bản",
    "矮": "thấp",
    "高": "cao",
    "大": "lớn",
    "小": "nhỏ",
    "长": "dài",
    "短": "ngắn",
    "强": "mạnh",
    "弱": "yếu",
    "多": "nhiều",
    "少": "ít",
    "全": "toàn",
    "半": "nửa",
    "空": "trống",
    "满": "đầy",
    "开": "mở",
    "关": "đóng",
    "上": "trên",
    "下": "dưới",
    "左": "trái",
    "右": "phải",
    "前": "trước",
    "后": "sau",
    "内": "trong",
    "外": "ngoài",
    "东": "đông",
    "南": "nam",
    "西": "tây",
    "北": "bắc",
    "春": "xuân",
    "夏": "hạ",
    "秋": "thu",
    "冬": "đông",
    "年": "năm",
    "月": "tháng",
    "日": "ngày",
    "时": "giờ",
    "分": "phút",
    "秒": "giây",
    "天": "trời",
    "地": "đất",
    "人": "người",
    "男": "nam",
    "女": "nữ",
    "老": "già",
    "少": "trẻ",
    "生": "sinh",
    "死": "tử",
    "王": "vương",
    "帝": "đế",
    "国": "quốc",
    "城": "thành",
    "军": "quân",
    "兵": "binh",
    "战": "chiến",
    "打": "đánh",
    "攻": "công",
    "守": "thủ",
    "进": "tiến",
    "退": "thoái",
    "来": "lai",
    "去": "khứ",
    "入": "nhập",
    "出": "xuất",
    "得": "đắc",
    "失": "thất",
    "有": "hữu",
    "无": "vô",
    "是": "thị",
    "非": "phi",
    "对": "đối",
    "错": "sai",
    "好": "tốt",
    "坏": "xấu",
    "美": "mỹ",
    "丑": "xấu",
    "善": "thiện",
    "恶": "ác",
    "正": "chính",
    "邪": "tà",
    "真": "chân",
    "假": "giả",
    "虚": "hư",
    "实": "thực",
    "明": "minh",
    "暗": "ám",
    "光": "quang",
    "影": "ảnh",
    "声": "thanh",
    "色": "sắc",
    "香": "hương",
    "味": "vị",
    "触": "xúc",
    "法": "pháp",

    # All previous comprehensive terms
    "默认为": "mặc định là",
    "默认": "mặc định",
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
    "张": "lá",
    "点": "điểm",

    # Character names (100+)
    "乐就": "Nhạc Tựu", "乐綝": "Nhạc Tống", "华歆": "Hoa Hâm", "华雄": "Hoa Hùng",
    "贾诩": "Giả Húc", "贾逵": "Giả Quỹ", "贾充": "Giả Sung", "沮授": "Trở Thụ",
    "纪灵": "Kỷ Linh", "笮融": "Trạch Dung", "逢纪": "Phùng Kỷ", "许褚": "Hứa Chử",
    "刘辟": "Lưu Tịch", "刘禅": "Lưu Thiện", "甄宓": "Chân Mích", "孙綝": "Tôn Tốn",
    "李傕": "Lý Quắc", "李遗": "Lý Di", "张嶷": "Trương Nghệ", "蒋干": "Tưởng Can",
    "雷薄": "Lôi Bạc", "吕蒙": "Lã Mông", "于禁": "Vu Cấm", "赵累": "Triệu Lũy",
    "史阿": "Sử A", "凯撒": "Caesar", "端蒙": "Đoan Mông", "妹喜": "Muội Hỉ",
    "半藏": "Hanzou", "少微": "Thiếu Vi", "少昊": "Thiếu Hạo", "安卡": "An Ka",
    "卡玛": "Karma", "梼杌": "Đào Ngột", "露娜": "Luna",
    "关羽": "Quan Vũ", "张飞": "Trương Phi", "赵云": "Triệu Vân",
    "马超": "Mã Siêu", "黄忠": "Hoàng Trung", "诸葛亮": "Gia Cát Lượng",
    "刘备": "Lưu Bị", "曹操": "Tào Tháo", "孙权": "Tôn Quyền",
    "周瑜": "Chu Du", "司马懿": "Tư Mã Ý", "甘宁": "Cam Ninh",
    "太史慈": "Thái Sử Từ", "孙尚香": "Tôn Thượng Hương", "陆逊": "Lục Tốn",
    "貂蝉": "Điêu Thuyền", "吕布": "Lã Bố", "董卓": "Đổng Trác",
    "颜良": "Nhan Lương", "文丑": "Văn Sửu", "袁绍": "Viên Thiệu",
    "张辽": "Trương Liêu", "徐晃": "Từ Hoảng", "夏侯惇": "Hạ Hầu Đôn",
    "夏侯渊": "Hạ Hầu Uyên", "曹仁": "Tào Nhân", "曹丕": "Tào Phi",
    "郭嘉": "Quách Gia", "荀彧": "Tuân Úc", "荀攸": "Tuân Du",
    "典韦": "Điển Vi", "张郃": "Trương Cáp", "庞统": "Bàng Thống",
    "魏延": "Ngụy Diên", "姜维": "Khương Duy", "马谡": "Mã Tốc",
    "黄月英": "Hoàng Nguyệt Anh", "孟获": "Mạnh Hoạch", "祝融": "Chúc Dung",
    "大乔": "Đại Kiều", "小乔": "Tiểu Kiều", "黄盖": "Hoàng Cái",
    "程普": "Trình Phổ", "丁奉": "Đinh Phụng", "张昭": "Trương Chiêu",
    "张纮": "Trương Hoằng", "顾雍": "Cố Ung", "鲁肃": "Lỗ Túc",
    "诸葛瑾": "Gia Cát Cẩn", "步骘": "Bộ Chất", "凌统": "Lăng Thống",
    "徐盛": "Từ Thịnh", "潘璋": "Phan Chương", "朱桓": "Chu Hoàn",
    "朱然": "Chu Nhiên", "吕范": "Lã Phạm", "蒋钦": "Tưởng Khâm",
    "周泰": "Chu Thái", "陈武": "Trần Vũ", "董袭": "Đổng Tập",
    "韩当": "Hàn Đương", "孙坚": "Tôn Kiên", "孙策": "Tôn Sách",

    # Skill names (200+)
    "重身": "Trùng Thân", "畜鸣": "Súc Minh", "聆乐": "Linh Nhạc",
    "没矢": "Một Thỉ", "没欲": "Một Dục", "血裔": "Huyết Duệ",
    "血卫": "Huyết Vệ", "血诏": "Huyết Chiếu", "血偿": "Huyết Thường",
    "血拼": "Huyết Bính", "血途": "Huyết Đồ", "行殇": "Hành Thương",
    "节行": "Tiết Hành", "天行": "Thiên Hành", "神行": "Thần Hành",
    "镇行": "Trấn Hành", "行图": "Hành Đồ", "绝行": "Tuyệt Hành",
    "好施": "Hảo Thí", "荐降": "Tiến Hàng", "破降": "Phá Hàng",
    "拒降": "Cự Hàng", "应势": "Ứng Thế", "应援": "Ứng Viện",
    "武圣": "Vũ Thánh", "咆哮": "Bào Háo", "龙胆": "Long Đảm",
    "马术": "Mã Thuật", "烈弓": "Liệt Cung", "观星": "Quan Tinh",
    "空城": "Không Thành", "仁德": "Nhân Đức", "激将": "Kích Tướng",
    "奸雄": "Gian Hùng", "护驾": "Hộ Giá", "反间": "Phản Gián",
    "英姿": "Anh Tư", "制衡": "Chế Hành", "救援": "Cứu Viện",
    "结姻": "Kết Nhân", "国色": "Quốc Sắc", "连营": "Liên Doanh",
    "谦逊": "Khiêm Tốn", "度势": "Độ Thế", "克己": "Khắc Kỷ",
    "闭月": "Bế Nguyệt", "离间": "Ly Gián", "无双": "Vô Song",
    "利驭": "Lợi Ngự", "酒诗": "Tửu Thi", "鬼才": "Quỷ Tài",
    "遗计": "Di Kế", "驱虎": "Khu Hổ", "决心": "Quyết Tâm",
    "放权": "Phóng Quyền", "激昂": "Kích Ngang", "苦肉": "Khổ Nhục",
    "诈降": "Trá Hàng", "连破": "Liên Phá", "谋断": "Mưu Đoán",
    "刚烈": "Cương Liệt", "清俭": "Thanh Kiệm", "集智": "Tập Trí",
    "奇才": "Kỳ Tài", "青囊": "Thanh Nang", "急救": "Cấp Cứu",
    "权计": "Quyền Kế", "固政": "Cố Chính", "举荐": "Cử Tiến",
    "缓释": "Hoãn Thích", "谋溃": "Mưu Quỹ", "勇决": "Dũng Quyết",
    "明哲": "Minh Triết", "神智": "Thần Trí", "巧变": "Xảo Biến",
    "诱敌": "Dụ Địch", "尚义": "Thượng Nghĩa", "智迟": "Trí Trì",
    "排异": "Bài Dị", "直言": "Trực Ngôn", "固守": "Cố Thủ",
    "镇卫": "Trấn Vệ", "强袭": "Cường Tập", "挑衅": "Khiêu Khích",
    "妙才": "Diệu Tài", "纵适": "Túng Thích", "血仇": "Huyết Thù",
    "勇略": "Dũng Lược", "当先": "Đương Tiên", "义从": "Nghĩa Tùng",
    "父魂": "Phụ Hồn", "征南": "Chinh Nam", "陷阵": "Hãm Trận",
    "克敌": "Khắc Địch", "危殆": "Nguy Đãi", "忠勇": "Trung Dũng",
    "御策": "Ngự Sách", "夺刀": "Đoạt Đao", "豹变": "Báo Biến",
    "威重": "Uy Trọng", "清算": "Thanh Toán", "纵玄": "Túng Huyền",
    "望烈": "Vọng Liệt", "天辩": "Thiên Biện", "强识": "Cưỡng Thức",
    "屯田": "Truân Điền", "威缪": "Uy Mưu", "据守": "Cứ Thủ",
    "破军": "Phá Quân", "鸩毒": "Chậm Độc", "疠火": "Lệ Hỏa",
    "暴虐": "Bạo Ngược", "崩坏": "Băng Hoại", "无前": "Vô Tiền",
    "回雪": "Hồi Tuyết", "神威": "Thần Uy", "铁骑": "Thiết Kỵ",

    # Factions
    "魏": "Ngụy", "蜀": "Thục", "吴": "Ngô", "群": "Quần", "晋": "Tấn",

    # Particles (minimal)
    "的": "", "了": "", "吗": "", "呢": "", "啊": "",
    "与": "và", "及": "và", "但": "nhưng", "如果": "nếu",
    "之": "của", "把": "", "给": "cho", "为": "là",
    "对": "đối", "到": "đến", "在": "tại", "于": "ở", "以": "để",
}

def translate_ultra(text):
    """Ultra comprehensive translation"""

    # Check existing
    if text in existing:
        return existing[text]

    # Direct match
    if text in ultra_mega_dict:
        return ultra_mega_dict[text]

    result = text

    # Pattern: character/skill name with array notation
    match = re.match(r'^\s*],\s*(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in ultra_mega_dict:
            return result.replace(name, ultra_mega_dict[name])

    # Pattern: just name with colon bracket
    match = re.match(r'^(\w+):\s*\[$', result)
    if match:
        name = match.group(1)
        if name in ultra_mega_dict:
            return result.replace(name, ultra_mega_dict[name])

    # Dictionary replacement (longest first)
    for cn, vi in sorted(ultra_mega_dict.items(), key=lambda x: -len(x[0])):
        if cn and vi and cn in result:
            result = result.replace(cn, vi)

    # Cleanup
    result = re.sub(r'\s+', ' ', result)
    result = result.strip()

    return result if result != text else text

# Process all batches
all_translations = {}

for batch_num in range(1, 4):  # Batches 1, 2, 3
    batch_file = f'ultra_batch_{batch_num}.txt'
    try:
        with open(batch_file, 'r', encoding='utf-8') as f:
            batch_strings = [line.strip() for line in f if line.strip()]

        print(f"\n📦 Processing {batch_file}: {len(batch_strings)} strings")

        successful = 0
        for cn in batch_strings:
            vi = translate_ultra(cn)
            if vi != cn:
                all_translations[cn] = vi
                successful += 1

        print(f"✅ Batch {batch_num} translated: {successful}/{len(batch_strings)}")
    except FileNotFoundError:
        print(f"⚠️  {batch_file} not found, skipping")

print(f"\n📊 Total translations: {len(all_translations)}")

# Save
with open('ultra_all_translated.json', 'w', encoding='utf-8') as f:
    json.dump(all_translations, f, ensure_ascii=False, indent=2)

print(f"💾 Saved to ultra_all_translated.json")

# Show samples
print(f"\n📝 Sample translations (first 80):")
for i, (cn, vi) in enumerate(list(all_translations.items())[:80]):
    if len(cn) < 100:
        print(f"  {cn} → {vi}")
