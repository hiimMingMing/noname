#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vietnamese Translation Script for Noname Game
Wuxia/Martial Arts Style
"""

import json
import re

# Translation dictionary with wuxia/martial arts style Vietnamese
translations = {
    # Numbers and positions
    "一人": "Một người",
    "两人": "Hai người",
    "三人": "Ba người",
    "四人": "Bốn người",
    "五人": "Năm người",
    "六人": "Sáu người",
    "七人": "Bảy người",
    "八人": "Tám người",
    "一号位": "Vị trí 1",
    "二号位": "Vị trí 2",
    "三号位": "Vị trí 3",
    "四号位": "Vị trí 4",
    "五号位": "Vị trí 5",
    "六号位": "Vị trí 6",
    "七号位": "Vị trí 7",
    "八号位": "Vị trí 8",
    "九号位": "Vị trí 9",

    # Time
    "一分钟": "Một phút",
    "两分钟": "Hai phút",
    "五分钟": "Năm phút",
    "上午": "Buổi sáng",
    "中午": "Buổi trưa",
    "下午": "Buổi chiều",
    "今天": "Hôm nay",
    "下周": "Tuần sau",

    # Rounds and turns
    "一轮": "Một vòng",
    "两轮": "Hai vòng",
    "三轮": "Ba vòng",
    "一次": "Một lần",
    "两次": "Hai lần",
    "二十回合": "Hai mươi hồi hợp",
    "三十回合": "Ba mươi hồi hợp",
    "二十局": "Hai mươi ván",
    "五十局": "Năm mươi ván",
    "五局": "Năm ván",
    "个回合": "hồi hợp",

    # UI Elements
    "上一页": "Trang trước",
    "下一页": "Trang sau",
    "上移": "Di lên",
    "下移": "Di xuống",
    "上移下移": "Di lên/xuống",
    "上划操作": "Thao tác vuốt lên",
    "下划操作": "Thao tác vuốt xuống",
    "不显示": "Không hiển thị",
    "不显示前缀": "Không hiển thị tiền tố",
    "不显示颜色": "Không hiển thị màu sắc",
    "不出现": "Không xuất hiện",
    "不滚动": "Không cuộn",
    "显示": "Hiển thị",
    "隐藏": "Ẩn",
    "主题色": "Màu chủ đề",
    "人名字体": "Font chữ tên",
    "人数": "Số người",
    "人物配音": "Lồng tiếng nhân vật",

    # Settings
    "不启用": "Không kích hoạt",
    "不限制": "Không giới hạn",
    "不补充": "Không bổ sung",
    "不替换已有素材": "Không thay thế tài nguyên có sẵn",
    "不能添加或修改": "Không thể thêm hoặc sửa",
    "为游戏主题打开玻璃效果手机暂不支持": "Bật hiệu ứng kính cho giao diện (di động chưa hỗ trợ)",

    # Downloads and files
    "下载失败": "Tải xuống thất bại",
    "下载扩展": "Tải xuống tiện ích",
    "个图片文件": "tập tin ảnh",
    "个字体文件": "tập tin font",
    "个音频文件": "tập tin âm thanh",
    "不是一个文件": "Không phải tập tin",
    "不是一个文件夹": "Không phải thư mục",
    "不是文件夹": "Không phải thư mục",

    # Status
    "不合法": "Không hợp lệ",
    "一个不合法的": "Một cái không hợp lệ",
    "不存在": "Không tồn tại",
    "不是": "Không phải",
    "与冲突": "Xung đột với",
    "不好意思刚才卡了": "Xin lỗi, vừa rồi bị giật",
    "人心散了队伍不好带啊": "Lòng người tản mác, khó lãnh đạo đội ngũ",

    # General UI
    "一般": "Phổ thông",
    "举例": "Ví dụ",
    "下面是": "Dưới đây là",
    "之后进行": "Sau đó tiến hành",
    "人加入": "người tham gia",
    "中量": "Trung bình",
    "事件可以通过": "Sự kiện có thể qua",

    # Game modes and mechanics
    "两军对垒": "Lưỡng Quân Đối Lũy",
    "乱斗": "Loạn Đấu",
    "万箭齐发": "Vạn Tiễn Tề Phát",
    "三连击": "Tam Liên Kích",
    "二连击": "Nhị Liên Kích",
    "丰收年": "Phong Thu Niên",
    "主内单挑特效": "Hiệu ứng đơn đấu chủ nội",

    # Character names (keeping some Chinese phonetics)
    "于禁": "Vu Cấm",
    "乐进": "Nhạc Tiến",
    "乐綝": "Nhạc Chủy",
    "乐无异": "Nhạc Vô Dị",
    "乐仙": "Nhạc Tiên",
    "乐就": "Nhạc Tựu",
    "乐动": "Nhạc Động",
    "七煞": "Thất Sát",
    "七尤": "Thất Vưu",
    "九鼎": "Cửu Đỉnh",
    "九文": "Cửu Văn",
    "一麻": "Nhất Ma",
    "三皆": "Tam Giai",
    "三板斧": "Tam Bản Phủ",
    "二生三": "Nhị Sinh Tam",
    "二波": "Nhị Ba",
    "五微": "Ngũ Vi",
    "亚煞极": "Á Sát Cực",

    # Skills and abilities
    "主将技": "Kỹ năng Chủ tướng",
    "主公技": "Kỹ năng Chủ công",
    "主公": "Chủ công",
    "乘势": "Thừa Thế",
    "伤害": "Sát thương",
    "体力": "Thể lực",

    # Special items
    "仁库": "Nhân Khố",
    "仁库中没有牌": "Nhân Khố không có bài",

    # Wuxia/Gameplay terms
    "不存在战法": "Không tồn tại Chiến Pháp",
    "不无懈自己": "Không Vô Tà chính mình",
    "不询问无懈": "Không hỏi Vô Tà",
    "不对敌方出桃": "Không dùng Đào cho địch",
    "不显示基本牌名称": "Không hiển thị tên bài cơ bản",
    "不显示装备牌名称": "Không hiển thị tên bài trang bị",
    "不享受主公的额外体力上限": "Không hưởng giới hạn thể lực thêm của Chủ công",
    "不享受地主的额外技能": "Không hưởng kỹ năng thêm của Địa chủ",
    "不存在的技能": "Kỹ năng không tồn tại",

    # Character-related
    "专属技能": "Kỹ năng chuyên thuộc",
    "专属武将出场率": "Tỷ lệ xuất trận tướng chuyên thuộc",
    "专属装备": "Trang bị chuyên thuộc",
    "主公仅点将可用隐匿技": "Chủ công chỉ dùng Ẩn Nặc Kỹ khi điểm tướng",
    "主公候选武将数": "Số võ tướng ứng cử Chủ công",
    "主公别开枪自己人": "Chủ công đừng bắn đồng đội",
    "主将和副将都明置后若为特定组合可获得珠联璧合标记": "Sau khi Chủ tướng và Phó tướng đều minh trí, nếu là tổ hợp đặc biệt có thể nhận dấu Châu Liên Bích Hợp",

    # Actions and effects
    "与交换装备区里的牌": "Đổi bài trong khu trang bị với",
    "个目标": "mục tiêu",
    "为无效技能": "là kỹ năng vô hiệu",
    "为牌添加知情者": "Thêm người biết cho bài",
    "亮出了": "Đã lộ ra",
    "交换两个元素的位置并附带动画": "Đổi vị trí hai phần tử kèm hiệu ứng",

    # Card-related
    "从三张随机亮出的牌中选择一张若无特殊说明则获得此牌": "Chọn một trong ba bài lộ ngẫu nhiên, nếu không chú thích đặc biệt thì nhận bài này",
    "从牌堆底摸了": "Đã rút từ đáy chồng bài",
    "从牌库中获得了": "Đã nhận từ thư viện bài",

    # Power scaling effects
    "从第轮开始你的出杀": "Từ vòng thứ, Sát của ngươi",
    "从第轮开始你的摸牌数": "Từ vòng thứ, số bài rút của ngươi",
    "从第轮开始你的杀造成的伤害": "Từ vòng thứ, sát thương Sát của ngươi gây ra",
    "从第轮开始你的锦囊和技能造成的伤害": "Từ vòng thứ, sát thương Cẩm nang và kỹ năng của ngươi gây ra",

    # Special messages
    "三十六计走为上容我去去便回": "Tam thập lục kế, tẩu vi thượng, dung ngã khứ khứ tiện hồi",
    "下家对你使用一张牌": "Người kế tiếp dùng một bài vào ngươi",
    "为什么一定要指名道姓选的东西喵": "Tại sao nhất định phải chỉ danh đạo tính chọn cái gì đó nha",
    "令玩家复活事件化": "Làm sự kiện phục sinh người chơi",
    "你们忍心就这么让我酱油了": "Các ngươi nỡ để ta thành người dự bị sao",
    "你随便杀闪不了算我输": "Ngươi cứ Sát, Tránh không được tính ta thua",

    # Damage and health
    "伤害抖动": "Rung sát thương",
    "体力上限不改变当前体力": "Giới hạn thể lực không đổi thể lực hiện tại",
    "体力上限最低为每轮开始时回复点体力": "Giới hạn thể lực tối thiểu, hồi phục thể lực đầu mỗi vòng",
    "体力上限身份手牌": "Giới hạn thể lực, thân phận, bài tay",
    "体力体限甲": "Thể lực, giới hạn, giáp",
    "体力值": "Giá trị thể lực",
    "体力条样式": "Kiểu thanh thể lực",

    # Player abilities
    "你使用受到的决斗对方需要两张杀": "Quyết Đấu ngươi dùng/nhận, đối phương cần hai Sát",
    "你使用杀后可以至多重铸一张牌": "Sau khi dùng Sát, ngươi có thể trùng đúc tối đa một bài",
    "你使用杀后可以至多重铸两张牌": "Sau khi dùng Sát, ngươi có thể trùng đúc tối đa hai bài",
    "你使用的万箭齐发其他角色需要使用张闪来响应": "Vạn Tiễn Tề Phát của ngươi, nhân vật khác cần dùng Tránh để đáp ứng",
    "你使用的五谷丰登仅友方角色可以获得牌": "Ngũ Cốc Phong Đăng của ngươi, chỉ ta nhận được bài",
    "你使用的桃园结义友方角色回复双倍体力": "Đào Viên Kết Nghĩa của ngươi, ta hồi phục gấp đôi thể lực",
    "你使用的顺手牵羊可额外结算一次": "Thuận Thủ Thiên Dương của ngươi có thể kết toán thêm một lần",
    "你使用的顺手牵羊无距离限制": "Thuận Thủ Thiên Dương của ngươi không giới hạn khoảng cách",
    "你使用过河拆桥时至多弃置目标三张牌": "Khi dùng Quá Hà Khư Kiều, ngươi tối đa bỏ ba bài mục tiêu",
    "你使用过河拆桥时至多弃置目标两张牌": "Khi dùng Quá Hà Khư Kiều, ngươi tối đa bỏ hai bài mục tiêu",

    # Combat abilities
    "你对其他人造成伤害时无视其护甲": "Khi gây sát thương cho người khác, ngươi vô thị hộ giáp",
    "你手牌数量少于你的杀伤害": "Số bài tay ngươi ít hơn, sát thương Sát của ngươi",
    "你每摸九张卡牌你对随机敌方造成点伤害": "Mỗi rút chín bài, ngươi gây sát thương cho địch ngẫu nhiên",
    "你每摸六张卡牌你对随机敌方造成点伤害": "Mỗi rút sáu bài, ngươi gây sát thương cho địch ngẫu nhiên",
    "你每轮杀首次造成伤害后摸一张牌": "Mỗi vòng, sau lần Sát đầu gây sát thương, ngươi rút một bài",
    "你每轮杀首次造成伤害后摸两张牌": "Mỗi vòng, sau lần Sát đầu gây sát thương, ngươi rút hai bài",

    # Stats and limits
    "你的主副将体力上限之和是奇数是否摸一张牌": "Tổng giới hạn thể lực Chủ Phó tướng của ngươi là số lẻ, có rút một bài?",
    "你的体力上限固定为无法通过任何途径改变体力值上限": "Giới hạn thể lực của ngươi cố định là, không thể thay đổi qua bất kỳ cách nào",
    "你的手牌上限不因体力值改变而改变": "Giới hạn bài tay của ngươi không đổi theo thể lực",
    "你的手牌小于当前体力时你造成的伤害": "Khi bài tay ngươi nhỏ hơn thể lực hiện tại, sát thương ngươi gây ra",
    "你的拼点牌点数最大为": "Điểm bài đấu điểm của ngươi tối đa là",
    "你的摸牌阶段你额外摸两张牌手牌上限": "Giai đoạn rút bài của ngươi, ngươi rút thêm hai bài, giới hạn bài tay",
    "你的每第三张杀伤害": "Mỗi Sát thứ ba của ngươi, sát thương",
    "你的装备不能被弃置": "Trang bị của ngươi không thể bỏ",
    "你的借刀杀人成功时伤害": "Khi Tá Đao Sát Nhân của ngươi thành công, sát thương",
    "你的出牌阶段你的出杀次数": "Giai đoạn ra bài của ngươi, số lần Sát",

    # Turn start abilities
    "你的回合开始时从牌堆中获得一张随机锦囊牌": "Đầu hồi hợp ngươi, nhận một Cẩm nang ngẫu nhiên từ chồng bài",
    "你的回合开始时从牌堆中获得三张随机锦囊牌": "Đầu hồi hợp ngươi, nhận ba Cẩm nang ngẫu nhiên từ chồng bài",
    "你的回合开始时从牌堆中获得两张随机锦囊牌": "Đầu hồi hợp ngươi, nhận hai Cẩm nang ngẫu nhiên từ chồng bài",
    "你的回合开始时从随机敌方手牌区获得张牌": "Đầu hồi hợp ngươi, nhận bài từ khu bài tay địch ngẫu nhiên",
    "你的回合开始时你获得一张决斗": "Đầu hồi hợp ngươi, ngươi nhận một Quyết Đấu",
    "你的回合开始时你获得一张杀": "Đầu hồi hợp ngươi, ngươi nhận một Sát",
    "你的回合开始时你获得一张桃": "Đầu hồi hợp ngươi, ngươi nhận một Đào",
    "你的回合开始时你获得一张火攻": "Đầu hồi hợp ngươi, ngươi nhận một Hỏa Công",
    "你的回合开始时你获得一张过河拆桥": "Đầu hồi hợp ngươi, ngươi nhận một Quá Hà Khư Kiều",
    "你的回合开始时你获得一张铁索连环": "Đầu hồi hợp ngươi, ngươi nhận một Thiết Tỏa Liên Hoàn",
    "你的回合开始时你获得一张闪": "Đầu hồi hợp ngươi, ngươi nhận một Tránh",
    "你的回合开始时你获得一张顺手牵羊": "Đầu hồi hợp ngươi, ngươi nhận một Thuận Thủ Thiên Dương",
    "你离开濒死时对所有敌方造成点伤害": "Khi ngươi thoát Hấp Hối, gây sát thương cho toàn bộ địch",

    # License
    "你可以在遵守协议的基础上任意使用修改并转发无名杀以及所有基于无名杀开发的扩展": "Ngươi có thể tùy ý dùng, sửa và chuyển tiếp Vô Danh Sát cùng mọi tiện ích phát triển dựa trên Vô Danh Sát, trên cơ sở tuân thủ thỏa thuận",

    # Common actions
    "使用": "Sử dụng",
}

def translate_string(chinese_str):
    """Translate a Chinese string to Vietnamese"""
    if chinese_str in translations:
        return translations[chinese_str]
    return None

def process_file(input_file, output_file):
    """Process a file of Chinese strings and create translation JSON"""
    with open(input_file, 'r', encoding='utf-8') as f:
        strings = [line.strip() for line in f if line.strip()]

    result = {}
    untranslated = []

    for s in strings:
        translation = translate_string(s)
        if translation:
            result[s] = translation
        else:
            untranslated.append(s)

    # Save translations
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Translated: {len(result)}")
    print(f"Untranslated: {len(untranslated)}")
    print(f"Saved to: {output_file}")

    # Save untranslated for reference
    untrans_file = output_file.replace('.json', '_remaining.txt')
    with open(untrans_file, 'w', encoding='utf-8') as f:
        for s in untranslated:
            f.write(s + '\n')
    print(f"Remaining strings saved to: {untrans_file}")

if __name__ == '__main__':
    print("Processing UI strings...")
    process_file('ui_strings_to_translate.txt', 'ui_translations_vi.json')
    print("\nProcessing gameplay strings...")
    process_file('gameplay_strings_to_translate.txt', 'gameplay_translations_vi.json')
