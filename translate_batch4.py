# -*- coding: utf-8 -*-
import json
import re

# MASSIVE EXPANDED character dictionary
characters = {
    # Previous characters (keep all from before)
    "曹操": "Tào Tháo", "刘备": "Lưu Bị", "孙权": "Tôn Quyền", "关羽": "Quan Vũ",
    "张飞": "Trương Phi", "赵云": "Triệu Vân", "诸葛亮": "Gia Cát Lượng", "周瑜": "Chu Du",
    "孙策": "Tôn Sách", "吕布": "Lã Bố", "貂蝉": "Điêu Thuyền", "华佗": "Hoa Đà",
    "司马懿": "Tư Mã Ý", "曹丕": "Tào Phi", "曹植": "Tào Thực", "郭嘉": "Quách Gia",
    "贾诩": "Giả Hủ", "马超": "Mã Siêu", "黄忠": "Hoàng Trung", "魏延": "Ngụy Diên",
    "孙尚香": "Tôn Thượng Hương", "大乔": "Đại Kiều", "小乔": "Tiểu Kiều",
    "甘宁": "Cam Ninh", "吕蒙": "Lã Mông", "陆逊": "Lục Tốn", "孙坚": "Tôn Kiên",
    "夏侯惇": "Hạ Hầu Đôn", "张辽": "Trương Liêu", "张郃": "Trương Cáp",
    "徐晃": "Từ Hoảng", "曹仁": "Tào Nhân", "董卓": "Đổng Trác", "庞统": "Bàng Thống",
    "法正": "Pháp Chính", "周不疑": "Chu Bất Nghi", "徐氏": "Từ Thị",
    "曹洪": "Tào Hồng", "孙寒华": "Tôn Hàn Hoa", "庞德公": "Bàng Đức Công",
    "刘协": "Lưu Hiệp", "吉本": "Cát Bổn", "庞德": "Bàng Đức", "灵雎": "Linh Thư",
    "穆顺": "Mục Thuận", "傅肜": "Phó Dung", "刘宏": "Lưu Hoằng",
    "卑弥呼": "Ti Di Hô", "卞夫人": "Biện Phu Nhân", "司马孚": "Tư Mã Phù",
    "吴班": "Ngô Ban", "周处": "Chu Xứ", "夏侯霸": "Hạ Hầu Bá",
    "孙翊": "Tôn Dực", "宗预": "Tông Dự", "张允": "Trương Doãn",
    "张宁": "Trương Ninh", "张既": "Trương Ký", "曹昂": "Tào Ngang",
    "李遗": "Lý Di", "桥蕤": "Kiều Nhuỵ", "毌丘俭": "Quán Khâu Kiệm",
    "牛金": "Ngưu Kim", "王凌": "Vương Lăng", "王昶": "Vương Xương",
    "王粲": "Vương Xán", "田豫": "Điền Dự", "祖茂": "Tổ Mậu",
    "葛玄": "Cát Huyền", "蒋济": "Tưởng Tế", "诸葛果": "Gia Cát Quả",
    "谯周": "Tiều Chu", "赵襄": "Triệu Tương", "何进": "Hà Tiến",
    "皇甫嵩": "Hoàng Phủ Tung", "阎象": "Diêm Tượng", "陈武董袭": "Trần Vũ Đổng Tập",
    "陈震": "Trần Chấn", "马云騄": "Mã Vân Lục", "麴义": "Khúc Nghĩa",
    "鲍信": "Bão Tín", "严颜": "Nghiêm Nhan", "严畯": "Nghiêm Tuấn",
    "严虎": "Nghiêm Hổ", "丘力居": "Khâu Lực Cư", "丰祈": "Phong Kì",
    "关兴张苞": "Quan Hưng Trương Bao",
    "于禁": "Vu Cấm", "华歆": "Hoa Hâm", "司马师": "Tư Mã Sư",
    "司马昭": "Tư Mã Chiêu", "夏侯徽": "Hạ Hầu Huy", "姜维": "Khương Duy",
    "孟获": "Mạnh Hoạch", "杨婉": "Dương Uyển", "袁绍": "Viên Thiệu",
    "韩龙": "Hàn Long", "黄月英": "Hoàng Nguyệt Anh", "于夫罗": "Vu Phu La",
    "张芝": "Trương Chi", "王元姬": "Vương Nguyên Cơ",

    # NEW - Batch 4 additions
    "马忠": "Mã Trung", "马腾": "Mã Đằng", "马良": "Mã Lương",
    "丁原": "Đinh Nguyên", "丁奉": "Đinh Phụng", "丁尚涴": "Đinh Thượng Uyển",
    "周瑜": "Chu Du", "蔡琰": "Thái Diễm", "蔡邕": "Thái Ung",
    "祢衡": "Nể Hành", "乐进": "Nhạc Tiến", "乐就": "Nhạc Tựu",
    "乐綝": "Nhạc Toản", "邹氏": "Trâu Thị",
}

# MASSIVE EXPANDED skill dictionary
skills = {
    # Previous skills (keep all)
    "七出": "Thất Xuất", "七哀": "Thất Ai", "七幻": "Thất Huyễn",
    "七弦": "Thất Huyền", "七星": "Thất Tinh", "七步": "Thất Bộ",
    "七笺": "Thất Tiên", "七辩": "Thất Biện", "七进": "Thất Tiến",
    "三头": "Tam Đầu", "三恇": "Tam Khương", "三殴": "Tam Âu",
    "三点": "Tam Điểm", "三略": "Tam Lược", "三礼": "Tam Lễ",
    "三窟": "Tam Quật", "三陈": "Tam Trần", "三顾": "Tam Cố",
    "三首": "Tam Thủ", "下书": "Hạ Thư", "不屈": "Bất Khuất",
    "不弃": "Bất Khí", "不悔": "Bất Hối", "不戢": "Bất Tập",
    "不臣": "Bất Thần", "专对": "Chuyên Đối", "业仇": "Nghiệp Cừu",
    "业火": "Nghiệp Hỏa", "业炎": "Nghiệp Viêm", "两点": "Lưỡng Điểm",
    "严政": "Nghiêm Chính", "严教": "Nghiêm Giáo", "严整": "Nghiêm Chỉnh",
    "严纪": "Nghiêm Kỷ", "严纲": "Nghiêm Cương", "严霜": "Nghiêm Sương",
    "丧乱": "Tang Loạn", "丧尸": "Tang Thi", "中枢": "Trung Xu",
    "中流": "Trung Lưu", "丰姿": "Phong Tư", "丰愍": "Phong Mẫn",
    "丰田": "Phong Điền", "丰积": "Phong Tích", "临节": "Lâm Tiết",
    "临阵": "Lâm Trận", "丹心": "Đan Tâm", "丹法": "Đan Pháp",
    "为乱": "Vi Loạn", "举义": "Cử Nghĩa", "举兵": "Cử Binh",
    "举寇": "Cử Khấu", "举棋": "Cử Kỳ", "举策": "Cử Sách",
    "举荐": "Cử Tiến", "举讹": "Cử Ngoa", "义争": "Nghĩa Tranh",
    "义从": "Nghĩa Tùng", "义兵": "Nghĩa Binh", "义叱": "Nghĩa Sất",
    "义拒": "Nghĩa Cự", "义烈": "Nghĩa Liệt", "义绝": "Nghĩa Tuyệt",
    "义舍": "Nghĩa Xá", "义襄": "Nghĩa Tương", "义贤": "Nghĩa Hiền",
    "义释": "Nghĩa Thích", "乌鹊": "Ô Thước", "乐泉": "Nhạc Tuyền",
    "乐虞": "Nhạc Ngu", "乐陵": "Nhạc Lăng", "乐马": "Nhạc Mã",
    "乘变": "Thừa Biến", "乘流": "Thừa Lưu", "乘烟": "Thừa Yên",
    "乘虚": "Thừa Hư", "乘袭": "Thừa Tập", "九伐": "Cửu Phạt",
    "一点": "Nhất Điểm", "一鼓作气": "Nhất Cổ Tác Khí", "万王": "Vạn Vương",
    "世公": "Thế Công", "东道": "Đông Đạo", "东郊": "Đông Giao",
    "丝刃": "Ti Nhận", "不可响应": "bất khả hưởng ứng", "丑牛": "Sửu Ngưu",
    "克昌": "Khắc Xương", "习事": "Tập Sự", "乡害": "Hương Hại",
    "乱击": "Loạn Kích", "乱年": "Loạn Niên", "乱战": "Loạn Chiến",
    "乱掠": "Loạn Lược", "乱朝": "Loạn Triều", "乱武": "Loạn Vũ",
    "乱群": "Loạn Quần", "乱魁": "Loạn Khôi", "乾纲": "Càn Cương",
    "争义": "Tranh Nghĩa", "争功": "Tranh Công", "争嗣": "Tranh Tự",
    "争擎": "Tranh Kình", "争適": "Tranh Thích", "于毒": "Vu Độc",
    "互忌": "Hỗ Kỵ", "互雠": "Hỗ Thù", "五星连珠": "Ngũ Tinh Liên Châu",
    "五灵": "Ngũ Linh", "五禽戏": "Ngũ Cầm Hí", "五虎": "Ngũ Hổ",
    "亡鹊": "Vong Thước", "亢勇": "Kháng Dũng", "亢悔": "Kháng Hối",
    "亢锐": "Kháng Nhuế", "交辉": "Giao Huy", "交锋": "Giao Phong",
    "亥猪": "Hợi Trư", "亦算": "Dịch Toán", "享乐": "Hưởng Lạc",
    "人公": "Nhân Công", "人望": "Nhân Vọng", "亿金": "Ức Kim",
    "仁仕": "Nhân Sĩ", "仁彀": "Nhân Cấu", "仁德": "Nhân Đức",
    "仁心": "Nhân Tâm", "仁政": "Nhân Chính", "仁智": "Nhân Trí",
    "仁望": "Nhân Vọng", "仁王": "Nhân Vương",
    "仁王金刚盾": "Nhân Vương Kim Cương Thuẫn",
    "仁释": "Nhân Thích", "仇决": "Cừu Quyết", "仇海": "Cừu Hải",
    "仇猎": "Cừu Liệp", "仇讨": "Cừu Thảo", "仇铓": "Cừu Mang",
    "介绫": "Giới Lăng", "从军": "Tùng Quân", "从击": "Tùng Kích",
    "从势": "Tùng Thế", "从汉": "Tùng Hán", "从谏": "Tùng Gián",
    "从鉴": "Tùng Giám", "从风": "Tùng Phong", "从龙": "Tùng Long",
    "仓储": "Thương Trữ", "仗关": "Trượng Quan", "付相": "Phó Tướng",
    "仙授": "Tiên Thụ",

    # NEW additions
    "一": "Nhất",
    "三": "Tam",
    "乐": "Nhạc",
}

# Japanese names
japanese_names = {
    "一之濑琴美": "Ichinose Kotomi",
    "七濑留美": "Nanase Rumi",
    "三枝二木": "Saegusa Futaki",
    "三谷良一": "Mitani Ryoichi",
    "久岛鸥": "Hisashima Kamome",
    "中津静流": "Nakatsu Shizuru",
    "乙坂有宇": "Otosaka Yuu",
    "井上晶": "Inoue Akira",
    "井之原真人": "Inohara Makoto",
    "三枝叶留佳": "Saegusa Haruka",
    "二木佳奈多": "Futaki Kanata",
}

def translate(text):
    """Translate with comprehensive prefix/suffix handling"""
    text = text.strip()

    # Handle special cases
    if text == '"天书"':
        return '"Thiên Thư"'
    if text == "〖克昌〗":
        return "〖Khắc Xương〗"
    if text == "【命运签】说明":
        return "【Vận Mệnh Thẻ】 Giải thích"
    if text == "不能触发〖雷击〗的判定":
        return "Không thể kích hoạt phán xét 〖Lôi Kích〗"

    # Skip very long text
    if len(text) > 40:
        return None

    # Japanese names
    if text in japanese_names:
        return japanese_names[text]

    # Check & separator
    if '&' in text:
        parts = text.split('&')
        translated = []
        for part in parts:
            trans = translate(part.strip())
            if trans:
                translated.append(trans)
        if len(translated) == len(parts):
            return ' & '.join(translated)
        return None

    # Direct matches
    if text in skills:
        return skills[text]
    if text in characters:
        return characters[text]

    # Handle TW special prefixes
    tw_specials = [
        ("TW起", "TW Khởi"),
        ("TW将", "TW Tướng"),
        ("TW谋", "TW Mưu"),
        ("TW魔", "TW Ma"),
        ("TW神", "TW Thần"),
    ]
    for prefix_cn, prefix_vi in tw_specials:
        if text.startswith(prefix_cn):
            base = text[len(prefix_cn):]
            if base in characters:
                return f"{prefix_vi} {characters[base]}"
            if base in skills:
                return f"{prefix_vi} {skills[base]}"

    # Handle TW general prefix
    if text.startswith("TW"):
        base = text[2:]
        if base in characters:
            return f"TW {characters[base]}"
        if base in skills:
            return f"TW {skills[base]}"

    # Handle 乐 prefix (music characters)
    if text.startswith("乐") and len(text) > 1:
        base = text[1:]
        if base in characters:
            return f"Nhạc {characters[base]}"

    # Handle other prefixes
    prefixes = [
        ("OL界", "OL Giới"),
        ("九鼎", "Cửu Đỉnh"),
        ("26SP", "26SP"),
        ("☆SP", "☆SP"),
        ("S特神", "S Đặc Thần"),
        ("SCL", "SCL"),
        ("OL", "OL"),
        ("SP", "SP"),
        ("界", "Giới"),
        ("神", "Thần"),
        ("★", "★"),
        ("☆", "☆"),
        ("26", "26"),
        ("书", "Thư"),
    ]

    for prefix_cn, prefix_vi in prefixes:
        if text.startswith(prefix_cn):
            base = text[len(prefix_cn):]
            if base in characters:
                return f"{prefix_vi} {characters[base]}"
            if base in skills:
                return f"{prefix_vi} {skills[base]}"

    return None

# Read input
with open('remaining_names_batch4.txt', 'r', encoding='utf-8') as f:
    names_list = [line.strip() for line in f if line.strip()]

# Translate
results = {}
success = 0
failed = 0

print("Translating batch 4...")
for name in names_list:
    trans = translate(name)
    if trans:
        results[name] = trans
        success += 1
        if success % 50 == 0:
            print(f"Progress: {success} translated...")
    else:
        failed += 1

# Save
with open('batch4_translated.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"✅ Translated: {success}")
print(f"⏭️  Skipped: {failed}")
print(f"📊 Success rate: {success*100//len(names_list)}%")
print(f"💾 Saved to batch4_translated.json")
