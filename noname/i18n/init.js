/**
 * i18n initialization module
 * 国际化系统初始化模块
 *
 * This module integrates i18n into the game initialization process
 */

import { i18n } from './index.js';
import { setupTranslationInterceptor } from './interceptor.js';
import { game, lib } from 'noname';

/**
 * Initialize i18n during game boot
 * Should be called early in the game initialization process
 * @returns {Promise<void>}
 */
export async function initI18n() {
	console.log('[i18n] Starting initialization...');

	try {
		await i18n.init();
		console.log(`[i18n] System ready - Current locale: ${i18n.getLocale()}`);

		// Make i18n globally available
		if (!lib.i18n) {
			lib.i18n = i18n;
		}

		// Add helper method to lib
		if (!lib.translate) {
			lib.translate = {};
		}

		// Setup translation interceptor to make translations work automatically
		setupTranslationInterceptor();

		// Add translation helper to get
		if (typeof get !== 'undefined' && !get.translation) {
			/**
			 * Get translation with i18n support
			 * @param {string} key - Translation key
			 * @param {string} [defaultValue] - Default value
			 * @returns {string}
			 */
			const originalTranslation = get.translation;
			if (originalTranslation) {
				get.translation = function(key, defaultValue) {
					// First try i18n system
					const i18nResult = i18n.t(key);
					if (i18nResult !== key) {
						return i18nResult;
					}
					// Fall back to original get.translation
					return originalTranslation.call(this, key, defaultValue);
				};
			}
		}

		return true;
	} catch (error) {
		console.error('[i18n] Initialization error:', error);
		return false;
	}
}

/**
 * Change language at runtime
 * @param {string} locale - New locale code
 * @returns {Promise<boolean>}
 */
export async function changeLanguage(locale) {
	try {
		await i18n.setLocale(locale);

		// Reload UI elements that display text
		if (typeof game.reload === 'function') {
			// For a complete language switch, we need to reload the game
			// Show a confirmation dialog
			const localeName = i18n.getLocaleName(locale);
			if (confirm(`语言已更改为${localeName}\nLanguage changed to ${localeName}\nĐã đổi ngôn ngữ sang ${localeName}\n\n是否重新加载游戏？\nReload game?\nTải lại trò chơi?`)) {
				game.reload();
			}
		}

		return true;
	} catch (error) {
		console.error('[i18n] Language change failed:', error);
		return false;
	}
}

/**
 * Get language selector UI config for settings
 * @returns {Object}
 */
export function getLanguageSelectorConfig() {
	const locales = i18n.getAvailableLocales();

	return {
		name: '语言 / Language / Ngôn ngữ',
		init: i18n.getLocale(),
		intro: '选择游戏语言 / Select game language / Chọn ngôn ngữ',
		item: Object.fromEntries(locales.map(locale => [locale.code, locale.name])),
		onclick: async function(locale) {
			await changeLanguage(locale);
		}
	};
}
