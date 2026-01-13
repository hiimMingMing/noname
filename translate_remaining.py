#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate remaining Chinese strings to Vietnamese
Uses pattern matching and dictionary-based translation
"""

import json
import re

# Load existing translations to maintain consistency
with open('locales/vi-VN/menu.json', 'r', encoding='utf-8') as f:
    existing_menu = json.load(f)
with open('locales/vi-VN/gameplay.json', 'r', encoding='utf-8') as f:
    existing_gameplay = json.load(f)
with open('locales/vi-VN/core.json', 'r', encoding='utf-8') as f:
    existing_core = json.load(f)

# Combine existing for lookup
existing_translations = {**existing_menu, **existing_gameplay, **existing_core}

# Comprehensive translation dictionary
translation_dict = {
    # Common single words
    "至少": "Ít nhất",
    "放置": "Đặt",
    "虚拟": "Ảo",
    "杀害": "Sát hại",
    "进行": "Tiến hành",
    "解除": "Giải trừ",
    "新杀": "Tân Sát",
    "挟令": "Hiếp lệnh",
    "扑克": "Poker",
    "较慢": "Khá chậm",
    "较快": "Khá nhanh",
    "很快": "Rất nhanh",
    "托管": "Ủy thác",
    "无限": "Vô hạn",
    "默认": "Mặc định",
    "新版": "Bản mới",
    "旧版": "Bản cũ",
    "隐藏": "Ẩn",
    "显示": "Hiện",
    "音乐": "Âm nhạc",
    "自定": "Tự định",
    "表情": "Biểu cảm",
    "简约": "Giản ước",
    "自动": "Tự động",
    "击杀": "Kích sát",
    "混合": "Hỗn hợp",
    "缩放": "Thu phóng",
    "抖动": "Rung",
    "铁索": "Thiết tỏa",
    "手动": "Thủ công",
    "横置": "Ngang trí",
    "濒死": "Hấp hối",
    "阵亡": "Trận vong",
    "连环": "Liên hoàn",
    "翻面": "Lật mặt",
    "重铸": "Trùng đúc",
    "刷新": "Làm mới",
    "复制": "Sao chép",
    "粘贴": "Dán",
    "剪切": "Cắt",
    "撤销": "Hoàn tác",
    "重做": "Làm lại",
    "保存": "Lưu",
    "删除": "Xóa",
    "取消": "Hủy",
    "确认": "Xác nhận",
    "确定": "OK",
    "关闭": "Đóng",
    "开启": "Mở",
    "暂停": "Tạm dừng",
    "继续": "Tiếp tục",
    "跳过": "Bỏ qua",
    "重播": "Phát lại",
    "加速": "Tăng tốc",
    "减速": "Giảm tốc",
    "原速": "Tốc gốc",

    # Colors
    "黄色": "Vàng",
    "绿色": "Xanh lá",
    "紫色": "Tím",
    "红色": "Đỏ",
    "蓝色": "Xanh dương",
    "橙色": "Cam",
    "黑色": "Đen",
    "白色": "Trắng",
    "金色": "Vàng kim",
    "银色": "Bạc",

    # Themes
    "木纹": "Vân gỗ",
    "流沙": "Lưu sa",
    "水墨": "Thủy mặc",
    "竹杖": "Trúc trượng",
    "黑暗": "Hắc ám",
    "魔爪": "Ma trảo",
    "金框": "Khung vàng",
    "银框": "Khung bạc",
    "铜框": "Khung đồng",

    # Dragons/Mythical
    "金龙": "Kim Long",
    "银龙": "Ngân Long",
    "玉龙": "Ngọc Long",
    "神剑": "Thần Kiếm",
    "御剑": "Ngự Kiếm",
    "金箭": "Kim Tiễn",
    "乐仙": "Nhạc Tiên",
    "星蝶": "Tinh Điệp",
    "落英": "Lạc Anh",
    "蛇杖": "Xà Trượng",

    # Game terms
    "回合": "Hồi hợp",
    "阶段": "Giai đoạn",
    "判定": "Phán định",
    "摸牌": "Rút bài",
    "出牌": "Ra bài",
    "弃牌": "Bỏ bài",
    "准备": "Chuẩn bị",
    "结束": "Kết thúc",
    "体力": "Thể lực",
    "手牌": "Bài tay",
    "装备": "Trang bị",
    "标记": "Dấu",
    "技能": "Kỹ năng",
    "武将": "Võ tướng",
    "势力": "Thế lực",
    "身份": "Thân phận",
    "主公": "Chủ công",
    "忠臣": "Trung thần",
    "反贼": "Phản tặc",
    "内奸": "Nội gián",

    # Actions
    "发动": "Phát động",
    "响应": "Đáp ứng",
    "使用": "Sử dụng",
    "打出": "Đánh ra",
    "弃置": "Bỏ đi",
    "获得": "Đạt được",
    "失去": "Mất",
    "交换": "Đổi",
    "移动": "Di chuyển",
    "选择": "Chọn",
    "指定": "Chỉ định",
    "观看": "Xem",
    "展示": "Hiện",

    # Combat
    "伤害": "Sát thương",
    "回复": "Hồi phục",
    "恢复": "Khôi phục",
    "受伤": "Thụ thương",
    "死亡": "Tử vong",
    "复活": "Phục sinh",
    "失血": "Mất máu",
    "流血": "Chảy máu",

    # Skill types
    "锁定技": "Tỏa Định Kỹ",
    "限定技": "Hạn Định Kỹ",
    "觉醒技": "Giác Tỉnh Kỹ",
    "主公技": "Chủ Công Kỹ",
    "转换技": "Chuyển Hoán Kỹ",
    "隐匿技": "Ẩn Nặc Kỹ",
    "使命技": "Sứ Mệnh Kỹ",
    "势力技": "Thế Lực Kỹ",
}

# Character names (common ones)
character_names = {
    "曹操": "Tào Tháo",
    "刘备": "Lưu Bị",
    "孙权": "Tôn Quyền",
    "关羽": "Quan Vũ",
    "张飞": "Trương Phi",
    "赵云": "Triệu Vân",
    "诸葛亮": "Gia Cát Lượng",
    "周瑜": "Chu Du",
    "吕布": "Lã Bố",
    "貂蝉": "Điêu Thuyền",
    "司马懿": "Tư Mã Ý",
    "孙尚香": "Tôn Thượng Hương",
    "甄姬": "Chẩm Cơ",
    "黄盖": "Hoàng Cái",
    "陆逊": "Lục Tốn",
    "大乔": "Đại Kiều",
    "小乔": "Tiểu Kiều",
    "曹丕": "Tào Phi",
    "孙策": "Tôn Sách",
    "徐晃": "Từ Hoảng",
    "张辽": "Trương Liêu",
    "许褚": "Hứa Chử",
    "典韦": "Điển Vi",
    "郭嘉": "Quách Gia",
    "荀彧": "Tuân Úc",
    "贾诩": "Giả Hủ",
}

def translate_string(chinese):
    """Translate a Chinese string to Vietnamese"""

    # Check if already translated
    if chinese in existing_translations:
        return existing_translations[chinese]

    # Direct dictionary lookup
    if chinese in translation_dict:
        return translation_dict[chinese]

    # Character name lookup
    if chinese in character_names:
        return character_names[chinese]

    # Try to build translation from parts
    result = chinese
    for cn, vi in translation_dict.items():
        if cn in result:
            result = result.replace(cn, vi)

    # If we made ANY changes, return the result
    if result != chinese:
        return result

    # Return original if no translation found
    return chinese

# Read batch 3
with open('user_facing_batch_3.txt', 'r', encoding='utf-8') as f:
    batch3 = [line.strip() for line in f if line.strip()]

# Read batch 4
with open('user_facing_batch_4.txt', 'r', encoding='utf-8') as f:
    batch4 = [line.strip() for line in f if line.strip()]

print(f"📦 Batch 3: {len(batch3)} strings")
print(f"📦 Batch 4: {len(batch4)} strings")
print(f"📊 Total to translate: {len(batch3) + len(batch4)}")

# Translate batch 3
batch3_translations = {}
for cn in batch3:
    vi = translate_string(cn)
    if vi != cn:  # Only add if we found a translation
        batch3_translations[cn] = vi

# Translate batch 4
batch4_translations = {}
for cn in batch4:
    vi = translate_string(cn)
    if vi != cn:  # Only add if we found a translation
        batch4_translations[cn] = vi

print(f"\n✅ Batch 3: {len(batch3_translations)} translated ({len(batch3) - len(batch3_translations)} untranslated)")
print(f"✅ Batch 4: {len(batch4_translations)} translated ({len(batch4) - len(batch4_translations)} untranslated)")

# Save batch 3
with open('final_batch_3_vi.json', 'w', encoding='utf-8') as f:
    json.dump(batch3_translations, f, ensure_ascii=False, indent=2)
print(f"\n💾 Saved final_batch_3_vi.json")

# Save batch 4
with open('final_batch_4_vi.json', 'w', encoding='utf-8') as f:
    json.dump(batch4_translations, f, ensure_ascii=False, indent=2)
print(f"💾 Saved final_batch_4_vi.json")

print(f"\n🎉 Total new translations: {len(batch3_translations) + len(batch4_translations)}")
