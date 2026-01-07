/**
 * i18n (Internationalization) system for Noname
 * 无名杀国际化系统
 *
 * This module provides multi-language support for the game.
 */

import { game, lib, _status } from "noname";

export class I18n {
	constructor() {
		/** @type {string} Current locale (e.g., 'zh-CN', 'en-US', 'vi-VN') */
		this.currentLocale = "vi-VN";

		/** @type {Object.<string, Object>} Loaded translation data */
		this.translations = {};

		/** @type {Object} Locale configuration */
		this.localeConfig = {};

		/** @type {boolean} Whether i18n is initialized */
		this.initialized = false;

		/** @type {string[]} Available locales */
		this.availableLocales = ["vi-VN", "zh-CN", "en-US"];

		/** @type {Object.<string, string>} Locale display names */
		this.localeNames = {
			"zh-CN": "简体中文",
			"en-US": "English",
			"vi-VN": "Tiếng Việt",
		};
	}

	/**
	 * Initialize i18n system
	 * @returns {Promise<void>}
	 */
	async init() {
		if (this.initialized) return;

		try {
			// Load locale configuration
			await this.loadLocaleConfig();

			// Priority order:
			// 1. Saved preference (if exists and valid)
			// 2. Default to Vietnamese (vi-VN)
			// Note: We no longer auto-detect browser language by default
			let locale = "vi-VN"; // Default to Vietnamese

			if (lib.config.language && this.availableLocales.includes(lib.config.language)) {
				// Use saved preference only if it's valid
				locale = lib.config.language;
				console.log(`[i18n] Using saved locale: ${locale}`);
			} else {
				console.log(`[i18n] No saved preference, using default: vi-VN`);
			}

			// Set current locale
			await this.setLocale(locale);

			this.initialized = true;
			console.log(`[i18n] Initialized with locale: ${this.currentLocale}`);
		} catch (error) {
			console.error("[i18n] Initialization failed:", error);
			// Fallback to Vietnamese if initialization fails
			this.currentLocale = "vi-VN";
			this.initialized = true;
		}
	}

	/**
	 * Load locale configuration
	 * @returns {Promise<void>}
	 */
	async loadLocaleConfig() {
		try {
			const response = await fetch(`${lib.assetURL}locales/config.json`);
			if (response.ok) {
				this.localeConfig = await response.json();
				if (this.localeConfig.locales) {
					this.availableLocales = Object.keys(this.localeConfig.locales);
					this.localeNames = {};
					for (const locale in this.localeConfig.locales) {
						this.localeNames[locale] = this.localeConfig.locales[locale].name;
					}
				}
			}
		} catch (error) {
			console.warn("[i18n] Could not load locale config:", error);
		}
	}

	/**
	 * Detect locale from browser settings
	 * @returns {string}
	 */
	detectLocale() {
		const browserLang = navigator.language || navigator.userLanguage;

		// Try exact match
		if (this.availableLocales.includes(browserLang)) {
			return browserLang;
		}

		// Try language code match (e.g., 'en' matches 'en-US')
		const langCode = browserLang.split("-")[0];
		const match = this.availableLocales.find(locale => locale.startsWith(langCode));

		if (match) return match;

		// Default to Vietnamese
		return "vi-VN";
	}

	/**
	 * Set current locale and load translations
	 * @param {string} locale - Locale code (e.g., 'zh-CN', 'en-US', 'vi-VN')
	 * @returns {Promise<void>}
	 */
	async setLocale(locale) {
		if (!this.availableLocales.includes(locale)) {
			console.warn(`[i18n] Locale '${locale}' not available, using 'vi-VN'`);
			locale = "vi-VN";
		}

		this.currentLocale = locale;

		// Load translations for this locale
		await this.loadTranslations(locale);

		// Save preference
		game.saveConfig("language", locale);

		// Apply translations
		this.applyTranslations();
	}

	/**
	 * Load translation files for a locale
	 * @param {string} locale - Locale code
	 * @returns {Promise<void>}
	 */
	async loadTranslations(locale) {
		// Don't load for Chinese (it's the default/source language)
		if (locale === "zh-CN") {
			this.translations[locale] = {};
			console.log(`[i18n] Skipping translations for zh-CN (source language)`);
			return;
		}

		const categories = ["core", "cards", "characters", "modes", "menu", "gameplay"];
		this.translations[locale] = {};

		console.log(`[i18n] Loading translations for ${locale}...`);
		console.log(`[i18n] Asset URL: "${lib.assetURL}"`);

		for (const category of categories) {
			try {
				const url = `${lib.assetURL}locales/${locale}/${category}.json`;
				console.log(`[i18n] Fetching: ${url}`);
				const response = await fetch(url);

				if (response.ok) {
					const data = await response.json();
					this.translations[locale][category] = data;
					const keyCount = Object.keys(data).length;
					console.log(`[i18n] ✅ Loaded ${locale}/${category}.json (${keyCount} keys)`);
				} else {
					console.warn(`[i18n] ❌ Failed to load ${locale}/${category}.json - Status: ${response.status}`);
				}
			} catch (error) {
				console.error(`[i18n] ❌ Error loading ${locale}/${category}.json:`, error);
			}
		}

		const totalKeys = Object.keys(this.translations[locale]).reduce((sum, cat) => {
			return sum + Object.keys(this.translations[locale][cat] || {}).length;
		}, 0);
		console.log(`[i18n] Total translations loaded for ${locale}: ${totalKeys} keys across ${Object.keys(this.translations[locale]).length} categories`);
	}

	/**
	 * Apply translations to lib.translate
	 */
	applyTranslations() {
		console.log(`[i18n] applyTranslations() called - currentLocale: ${this.currentLocale}`);

		if (this.currentLocale === "zh-CN") {
			// Chinese is the default, no need to override
			console.log(`[i18n] Skipping applyTranslations for zh-CN (source language)`);
			return;
		}

		const translations = this.translations[this.currentLocale];
		if (!translations) {
			console.warn(`[i18n] No translations found for ${this.currentLocale}`);
			return;
		}

		console.log(`[i18n] Applying translations from ${this.currentLocale}...`);
		let totalApplied = 0;

		// Merge all category translations into lib.translate
		for (const category in translations) {
			const categoryData = translations[category];
			const keyCount = Object.keys(categoryData).length;
			Object.assign(lib.translate, categoryData);
			totalApplied += keyCount;
			console.log(`[i18n] ✅ Applied ${keyCount} translations from category: ${category}`);
		}

		console.log(`[i18n] 🎉 Total ${totalApplied} translations applied to lib.translate`);

		// Test a few translations
		console.log(`[i18n] Test translations:`, {
			sha: lib.translate.sha,
			shan: lib.translate.shan,
			tao: lib.translate.tao,
			zhaoyun: lib.translate.zhaoyun,
			hp: lib.translate.hp
		});

		// Trigger UI update event
		if (typeof game.broadcast === "function") {
			game.broadcast(function (locale) {
				if (_status.event) {
					_status.event.trigger("languageChange");
				}
			}, this.currentLocale);
		}
	}

	/**
	 * Get translation for a key
	 * @param {string} key - Translation key
	 * @param {string} [defaultValue] - Default value if translation not found
	 * @returns {string}
	 */
	t(key, defaultValue) {
		// First check lib.translate (includes both default Chinese and loaded translations)
		if (lib.translate && lib.translate[key]) {
			return lib.translate[key];
		}

		// Return default value or key itself
		return defaultValue || key;
	}

	/**
	 * Get all available locales
	 * @returns {Array<{code: string, name: string}>}
	 */
	getAvailableLocales() {
		return this.availableLocales.map(code => ({
			code: code,
			name: this.localeNames[code] || code,
		}));
	}

	/**
	 * Check if a locale is available
	 * @param {string} locale - Locale code
	 * @returns {boolean}
	 */
	isLocaleAvailable(locale) {
		return this.availableLocales.includes(locale);
	}

	/**
	 * Get current locale
	 * @returns {string}
	 */
	getLocale() {
		return this.currentLocale;
	}

	/**
	 * Get locale display name
	 * @param {string} [locale] - Locale code (defaults to current locale)
	 * @returns {string}
	 */
	getLocaleName(locale) {
		locale = locale || this.currentLocale;
		return this.localeNames[locale] || locale;
	}
}

// Export singleton instance
export const i18n = new I18n();
