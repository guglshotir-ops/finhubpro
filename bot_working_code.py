"""
РАБОЧИЙ КОД БОТА для полноэкранного режима мини-приложения
ВАЖНО: Используйте KeyboardButton с web_app, НЕ InlineKeyboardButton!
"""

from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Ваш токен бота
BOT_TOKEN = "7171341328:AAFn6u2zdI3Ht8gCUtFmPvnt4n-aPPednLw"

# URL вашего мини-приложения (ОБЯЗАТЕЛЬНО HTTPS!)
WEB_APP_URL = "https://guglshotir-ops.github.io/finhub-pro/"

def create_webapp_keyboard():
    """Создает клавиатуру с кнопкой WebApp для полноэкранного режима"""
    # КРИТИЧЕСКИ ВАЖНО: KeyboardButton с web_app, НЕ InlineKeyboardButton!
    web_app_button = KeyboardButton(
        text="aaaa",  # Текст кнопки
        web_app=WebAppInfo(url=WEB_APP_URL)  # URL мини-приложения
    )
    
    # Создаем клавиатуру
    return ReplyKeyboardMarkup(
        [[web_app_button]],  # Кнопка в одной строке
        resize_keyboard=True,  # Автоматически изменять размер
        one_time_keyboard=False,  # Кнопка остается видимой
        input_field_placeholder="Нажмите кнопку 'aaaa' для открытия приложения"
    )

async def start(update, context):
    """Обработчик команды /start"""
    keyboard = create_webapp_keyboard()
    
    await update.message.reply_text(
        "👋 Добро пожаловать!\n\n"
        "Нажмите кнопку 'aaaa' ниже для открытия приложения в полноэкранном режиме.",
        reply_markup=keyboard
    )

async def handle_message(update, context):
    """Обработчик обычных сообщений"""
    # Всегда показываем кнопку WebApp
    keyboard = create_webapp_keyboard()
    
    await update.message.reply_text(
        "Используйте кнопку 'aaaa' для открытия приложения.",
        reply_markup=keyboard
    )

def main():
    """Запуск бота"""
    print("🚀 Запуск бота...")
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    print("✅ Бот запущен и готов к работе!")
    print(f"📱 URL мини-приложения: {WEB_APP_URL}")
    application.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()

