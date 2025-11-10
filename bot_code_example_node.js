/**
 * Пример кода для бота Telegram (Node.js) с кнопкой с версией
 * для открытия мини-приложения в полноэкранном режиме
 */

const { Telegraf, Markup } = require('telegraf');

// Ваш токен бота
const BOT_TOKEN = "7171341328:AAFn6u2zdI3Ht8gCUtFmPvnt4n-aPPednLw";

// URL вашего мини-приложения
const WEB_APP_URL = "https://guglshotir-ops.github.io/finhub-pro/";

// Версия кнопки - МЕНЯЙТЕ ЭТО ПРИ КАЖДОМ ОБНОВЛЕНИИ!
const BUTTON_VERSION = "v3.0";  // Увеличьте версию при каждом обновлении

// Функция для получения текста кнопки
function getButtonText() {
    const now = new Date();
    const dateStr = now.toLocaleDateString('ru-RU', { day: '2-digit', month: '2-digit' });
    const timeStr = now.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' });
    
    // Вариант 1: С версией и датой
    // return `🚀 FinHub ${BUTTON_VERSION} (${dateStr})`;
    
    // Вариант 2: С версией и временем
    // return `🚀 FinHub ${BUTTON_VERSION} (${timeStr})`;
    
    // Вариант 3: Просто версия (рекомендуется - короче)
    return `🚀 FinHub ${BUTTON_VERSION}`;
    
    // Вариант 4: Только версия без эмодзи
    // return `FinHub ${BUTTON_VERSION}`;
}

const bot = new Telegraf(BOT_TOKEN);

// Обработчик команды /start
bot.command('start', (ctx) => {
    const buttonText = getButtonText();
    
    // Создаем кнопку с WebApp
    // ВАЖНО: Используем web_app для полноэкранного режима
    const keyboard = Markup.keyboard([
        Markup.button.webApp(buttonText, WEB_APP_URL)
    ]).resize(); // resize_keyboard = true
    
    ctx.reply(`Нажмите кнопку "${buttonText}" для открытия приложения`, keyboard);
});

// Обработчик обычных сообщений
bot.on('text', (ctx) => {
    const buttonText = getButtonText();
    
    // Показываем кнопку снова
    const keyboard = Markup.keyboard([
        Markup.button.webApp(buttonText, WEB_APP_URL)
    ]).resize();
    
    ctx.reply(`Используйте кнопку "${buttonText}" для открытия приложения`, keyboard);
});

// Запуск бота
bot.launch();
console.log('Бот запущен...');

// Graceful stop
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));

