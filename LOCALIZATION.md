# 无名杀国际化系统 / Noname Internationalization System

## 概述 / Overview

无名杀现在支持多语言！本文档介绍如何使用和扩展国际化(i18n)系统。

Noname now supports multiple languages! This document describes how to use and extend the internationalization (i18n) system.

## 支持的语言 / Supported Languages

- 🇨🇳 **简体中文** (zh-CN) - 默认语言 / Default language
- 🇺🇸 **English** (en-US) - 英语
- 🇻🇳 **Tiếng Việt** (vi-VN) - 越南语（武侠风格 / Martial arts style）

## 目录结构 / Directory Structure

```
locales/
├── config.json           # 语言配置文件 / Locale configuration
├── zh-CN/               # 简体中文翻译（源语言，无需文件）
├── en-US/               # 英语翻译
│   ├── core.json        # 核心UI翻译
│   ├── cards.json       # 卡牌翻译
│   ├── characters.json  # 武将翻译
│   ├── modes.json       # 模式翻译
│   └── menu.json        # 菜单翻译
└── vi-VN/               # 越南语翻译
    ├── core.json
    ├── cards.json
    ├── characters.json
    ├── modes.json
    └── menu.json
```

## 系统架构 / System Architecture

### 核心模块 / Core Modules

1. **noname/i18n/index.js** - 主i18n类和单例
   - 语言检测和切换
   - 翻译文件加载
   - 翻译查找

2. **noname/i18n/init.js** - 初始化模块
   - 游戏启动时初始化i18n
   - 语言切换功能
   - 设置界面集成

3. **noname/i18n/interceptor.js** - 拦截器
   - 透明拦截`lib.translate`
   - 自动应用翻译
   - 支持热切换语言

### 工作原理 / How It Works

1. **初始化阶段**:
   - 游戏启动时，i18n系统自动初始化
   - 检测浏览器语言或加载用户保存的语言偏好
   - 加载对应语言的翻译文件

2. **翻译查找**:
   - 代码使用`lib.translate[key]`访问翻译
   - 拦截器自动查找当前语言的翻译
   - 如果找不到，回退到中文（默认语言）

3. **语言切换**:
   - 用户在设置中选择语言
   - 系统重新加载翻译文件
   - 建议重新启动游戏以完全应用更改

## 使用方法 / Usage

### 在代码中使用翻译 / Using Translations in Code

```javascript
// 方法1：使用lib.translate（推荐）
const cardName = lib.translate.sha; // 自动返回当前语言的翻译

// 方法2：使用i18n.t()方法
import { i18n } from '@/i18n';
const translation = i18n.t('sha', '默认值');

// 方法3：使用get.translation()（如果已扩展）
const text = get.translation('sha');
```

### 切换语言 / Switching Language

```javascript
import { changeLanguage } from '@/i18n/init.js';

// 切换到越南语
await changeLanguage('vi-VN');

// 切换到英语
await changeLanguage('en-US');

// 切换回中文
await changeLanguage('zh-CN');
```

### 获取可用语言 / Getting Available Languages

```javascript
import { i18n } from '@/i18n';

const locales = i18n.getAvailableLocales();
// 返回: [
//   { code: 'zh-CN', name: '简体中文' },
//   { code: 'en-US', name: 'English' },
//   { code: 'vi-VN', name: 'Tiếng Việt' }
// ]
```

## 添加新语言 / Adding New Languages

### 步骤1：创建翻译文件 / Step 1: Create Translation Files

在`locales/`下创建新的语言目录，例如`ja-JP`（日语）：

```
locales/ja-JP/
├── core.json
├── cards.json
├── characters.json
├── modes.json
└── menu.json
```

### 步骤2：编写翻译 / Step 2: Write Translations

每个JSON文件包含键值对：

```json
{
  "_comment": "注释说明此文件的用途",
  "_description": "更详细的描述",

  "sha": "斬",
  "shan": "閃",
  "tao": "桃"
}
```

### 步骤3：更新配置 / Step 3: Update Configuration

编辑`locales/config.json`，添加新语言：

```json
{
  "locales": {
    "ja-JP": {
      "name": "日本語",
      "nativeName": "日本語",
      "direction": "ltr",
      "enabled": true,
      "isDefault": false
    }
  }
}
```

### 步骤4：测试 / Step 4: Test

重新启动游戏，在设置中应该能看到新语言选项。

## 翻译指南 / Translation Guidelines

### 越南语武侠风格 / Vietnamese Martial Arts Style

越南语翻译采用武侠/古风风格，使用汉越词和古典用语：

- **保持武侠氛围**: 使用"ngươi"（汝）而非"bạn"（你）
- **使用汉越词**: "Trảm"（斩）、"Tướng"（将）、"Kỹ năng"（技能）
- **诗意表达**: "Thanh Long Đao"（青龙刀）、"Bát Quái Trận"（八卦阵）

示例对比：
- ❌ 现代风格: "Bạn cần sử dụng một lá bài Dodge"
- ✅ 武侠风格: "Ngươi phải sử dụng một【Tránh】"

### 一般原则 / General Principles

1. **保持一致性**: 相同的术语使用相同的翻译
2. **尊重原意**: 理解中文原文的含义和语境
3. **适应文化**: 考虑目标语言的文化背景
4. **简洁明了**: 翻译应该清晰易懂
5. **测试验证**: 在游戏中测试翻译效果

## 翻译类别 / Translation Categories

### core.json - 核心UI
- 游戏阶段、状态
- 通用按钮和操作
- 系统消息

### cards.json - 卡牌
- 卡牌名称
- 卡牌描述
- 卡牌效果说明

### characters.json - 武将
- 武将名字
- 技能名称
- 技能描述

### modes.json - 游戏模式
- 模式名称
- 身份名称
- 特殊术语

### menu.json - 菜单
- 主菜单项
- 设置选项
- 帮助文本

## API参考 / API Reference

### I18n类 / I18n Class

```javascript
class I18n {
  // 初始化i18n系统
  async init(): Promise<void>

  // 设置当前语言
  async setLocale(locale: string): Promise<void>

  // 获取翻译
  t(key: string, defaultValue?: string): string

  // 获取当前语言
  getLocale(): string

  // 获取可用语言列表
  getAvailableLocales(): Array<{code: string, name: string}>

  // 检查语言是否可用
  isLocaleAvailable(locale: string): boolean
}
```

### 初始化函数 / Initialization Functions

```javascript
// 初始化i18n系统
async function initI18n(): Promise<boolean>

// 切换语言
async function changeLanguage(locale: string): Promise<boolean>

// 获取语言选择器配置
function getLanguageSelectorConfig(): Object
```

## 故障排除 / Troubleshooting

### 问题：翻译不显示
**解决方案**:
1. 检查翻译文件是否存在
2. 确认JSON格式正确（无语法错误）
3. 检查键名是否匹配
4. 查看浏览器控制台错误信息

### 问题：切换语言后没有效果
**解决方案**:
1. 确认已调用`game.reload()`重新加载
2. 清除浏览器缓存
3. 检查`lib.config.language`是否正确保存

### 问题：部分文本未翻译
**解决方案**:
1. 某些文本可能硬编码在代码中，需要修改源代码
2. 检查是否遗漏了某些翻译键
3. 提交issue报告缺失的翻译

## 贡献 / Contributing

欢迎为无名杀贡献翻译！

We welcome translations for Noname!

### 如何贡献 / How to Contribute

1. Fork本仓库
2. 创建新的语言目录或改进现有翻译
3. 测试您的翻译
4. 提交Pull Request

### 翻译质量标准 / Translation Quality Standards

- ✅ 准确性：翻译准确传达原意
- ✅ 一致性：术语翻译保持一致
- ✅ 完整性：所有必要的键都已翻译
- ✅ 格式：JSON格式正确，无语法错误
- ✅ 测试：在游戏中测试过

## 许可证 / License

本项目采用GPL-3.0许可证，翻译文件同样适用。

This project is licensed under GPL-3.0, which also applies to translation files.

## 联系方式 / Contact

- GitHub Issues: https://github.com/libnoname/noname/issues
- 讨论区: https://github.com/libnoname/noname/discussions

---

## 更新日志 / Changelog

### v1.0.0 (2026-01-07)
- ✨ 初始i18n系统实现
- ✨ 添加英语支持
- ✨ 添加越南语支持（武侠风格）
- 📝 完整的文档和API参考

---

**感谢所有翻译贡献者！**
**Thanks to all translation contributors!**
**Cảm ơn tất cả những người đóng góp bản dịch!**
