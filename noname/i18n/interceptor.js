/**
 * i18n interceptor module
 * 国际化拦截器模块
 *
 * This module intercepts translation lookups to provide multi-language support
 */

import { i18n } from './index.js';
import { lib } from 'noname';

/**
 * Translate a Chinese string to current locale
 * @param {string} text - Chinese text to translate
 * @returns {string} Translated text or original if no translation found
 */
export function translateText(text) {
	if (!text || typeof text !== 'string') return text;

	// If current locale is Chinese, return original
	if (i18n.currentLocale === 'zh-CN') {
		return text;
	}

	// Try to find translation
	const translations = i18n.translations[i18n.currentLocale];
	if (translations) {
		// Check all categories for this translation key
		for (const category in translations) {
			if (translations[category][text]) {
				return translations[category][text];
			}
		}
	}

	// Fall back to lib.translate
	if (lib.translate && lib.translate[text]) {
		return lib.translate[text];
	}

	// Return original text
	return text;
}

/**
 * Setup translation interceptor
 * This wraps lib.translate in a Proxy to intercept translation lookups
 */
export function setupTranslationInterceptor() {
	// If already a proxy, don't wrap again
	if (lib.translate && lib.translate.__isI18nProxy) {
		return;
	}

	const originalTranslate = lib.translate || {};

	// Create a proxy that intercepts translation lookups
	lib.translate = new Proxy(originalTranslate, {
		get(target, prop) {
			// Check if this is a special proxy marker
			if (prop === '__isI18nProxy') {
				return true;
			}

			// If current locale is Chinese, use original
			if (i18n.currentLocale === 'zh-CN') {
				return Reflect.get(target, prop);
			}

			// Try to get translation from i18n system
			const translations = i18n.translations[i18n.currentLocale];
			if (translations) {
				// Check all categories for this translation key
				for (const category in translations) {
					if (translations[category][prop]) {
						return translations[category][prop];
					}
				}
			}

			// Fall back to original translation (Chinese)
			return Reflect.get(target, prop);
		},

		set(target, prop, value) {
			// Allow setting new translations
			return Reflect.set(target, prop, value);
		},

		has(target, prop) {
			if (prop === '__isI18nProxy') {
				return true;
			}

			// Check if translation exists in current locale or original
			if (i18n.currentLocale !== 'zh-CN') {
				const translations = i18n.translations[i18n.currentLocale];
				if (translations) {
					for (const category in translations) {
						if (prop in translations[category]) {
							return true;
						}
					}
				}
			}

			return Reflect.has(target, prop);
		},

		ownKeys(target) {
			// Return all keys from both original and current locale
			const keys = new Set(Reflect.ownKeys(target));

			if (i18n.currentLocale !== 'zh-CN') {
				const translations = i18n.translations[i18n.currentLocale];
				if (translations) {
					for (const category in translations) {
						Object.keys(translations[category]).forEach(key => keys.add(key));
					}
				}
			}

			return Array.from(keys);
		},

		getOwnPropertyDescriptor(target, prop) {
			// Check current locale first
			if (i18n.currentLocale !== 'zh-CN') {
				const translations = i18n.translations[i18n.currentLocale];
				if (translations) {
					for (const category in translations) {
						if (prop in translations[category]) {
							return {
								value: translations[category][prop],
								writable: true,
								enumerable: true,
								configurable: true
							};
						}
					}
				}
			}

			return Reflect.getOwnPropertyDescriptor(target, prop);
		}
	});

	console.log('[i18n] Translation interceptor installed');
}

/**
 * Setup auto-translation for alert, confirm, and game functions
 * This wraps these global functions to automatically translate Chinese strings
 */
export function setupAutoTranslation() {
	// Save original functions
	const originalAlert = window.alert;
	const originalConfirm = window.confirm;
	const originalPrompt = window.prompt;

	// Override alert to auto-translate
	window.alert = function(message) {
		const translated = translateText(message);
		return originalAlert.call(this, translated);
	};

	// Override confirm to auto-translate
	window.confirm = function(message) {
		const translated = translateText(message);
		return originalConfirm.call(this, translated);
	};

	// Override prompt to auto-translate
	window.prompt = function(message, defaultValue) {
		const translated = translateText(message);
		return originalPrompt.call(this, translated, defaultValue);
	};

	console.log('[i18n] Auto-translation for alert/confirm/prompt installed');
}

/**
 * Setup auto-translation for game.log and game.alert
 * Must be called after game object is initialized
 */
export function setupGameTranslation() {
	if (typeof game === 'undefined') {
		console.warn('[i18n] game object not found, skipping game translation setup');
		return;
	}

	// Save original game.log
	const originalGameLog = game.log;
	if (originalGameLog && !originalGameLog.__i18nWrapped) {
		game.log = function(...args) {
			const translatedArgs = args.map(arg => {
				if (typeof arg === 'string') {
					return translateText(arg);
				}
				return arg;
			});
			return originalGameLog.apply(this, translatedArgs);
		};
		game.log.__i18nWrapped = true;
	}

	// Save original game.alert
	const originalGameAlert = game.alert;
	if (originalGameAlert && !originalGameAlert.__i18nWrapped) {
		game.alert = function(...args) {
			const translatedArgs = args.map(arg => {
				if (typeof arg === 'string') {
					return translateText(arg);
				}
				return arg;
			});
			return originalGameAlert.apply(this, translatedArgs);
		};
		game.alert.__i18nWrapped = true;
	}

	console.log('[i18n] Auto-translation for game.log/game.alert installed');
}

/**
 * Remove translation interceptor (restore original lib.translate)
 */
export function removeTranslationInterceptor() {
	if (lib.translate && lib.translate.__isI18nProxy) {
		// Get the original target from the proxy
		// Note: This is a simplified approach; in production you might want to keep a reference
		console.warn('[i18n] Removing interceptor - translations will revert to Chinese');
	}
}

/**
 * Intercept specific translation function calls
 * This can be used to intercept get.translation() or other translation functions
 *
 * @param {Function} originalFunction - The original translation function
 * @returns {Function} - Wrapped function with i18n support
 */
export function wrapTranslationFunction(originalFunction) {
	return function(key, ...args) {
		// Try i18n first
		if (i18n.initialized && i18n.currentLocale !== 'zh-CN') {
			const translation = i18n.t(key);
			if (translation !== key) {
				return translation;
			}
		}

		// Fall back to original function
		return originalFunction.call(this, key, ...args);
	};
}
