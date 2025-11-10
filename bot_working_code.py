"""
РАБОЧИЙ КОД БОТА для полноэкранного режима мини-приложения
ВАЖНО: Используйте KeyboardButton с web_app, НЕ InlineKeyboardButton!
"""

from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from datetime import datetime

# Ваш токен бота
BOT_TOKEN = "7171341328:AAFn6u2zdI3Ht8gCUtFmPvnt4n-aPPednLw"

# URL вашего мини-приложения (ОБЯЗАТЕЛЬНО HTTPS!)
WEB_APP_URL = "https://guglshotir-ops.github.io/finhub-pro/"

# Версия кнопки - АВТОМАТИЧЕСКИ МЕНЯЕТСЯ на основе timestamp
# Формат: test_1, test_2, test_3 и т.д.
# Используется timestamp для генерации уникального номера при каждом обновлении

def get_button_version():
    """Генерирует версию кнопки на основе timestamp"""
    # Используем timestamp Unix и берем последние 4 цифры
    # Это даст уникальный номер при каждом обновлении
    timestamp = int(datetime.now().timestamp())
    version_num = (timestamp % 10000) + 1  # От 1 до 10000
    return f"test_{version_num}"

def get_button_text():
    """Генерирует текст кнопки с версией"""
    version = get_button_version()
    return version  # Просто "test_1", "test_2" и т.д.

def create_webapp_keyboard():
    """Создает клавиатуру с кнопкой WebApp для полноэкранного режима"""
    button_text = get_button_text()
    
    # КРИТИЧЕСКИ ВАЖНО: KeyboardButton с web_app, НЕ InlineKeyboardButton!
    web_app_button = KeyboardButton(
        text=button_text,  # Динамический текст кнопки с версией
        web_app=WebAppInfo(url=WEB_APP_URL)  # URL мини-приложения
    )
    
    # Создаем клавиатуру
    return ReplyKeyboardMarkup(
        [[web_app_button]],  # Кнопка в одной строке
        resize_keyboard=True,  # Автоматически изменять размер
        one_time_keyboard=False,  # Кнопка остается видимой
        input_field_placeholder="Нажмите кнопку для открытия приложения"
    )

async def start(update, context):
    """Обработчик команды /start"""
    keyboard = create_webapp_keyboard()
    
    button_text = get_button_text()
    await update.message.reply_text(
        "👋 Добро пожаловать!\n\n"
        f"Нажмите кнопку '{button_text}' ниже для открытия приложения в полноэкранном режиме.",
        reply_markup=keyboard
    )

async def handle_message(update, context):
    """Обработчик обычных сообщений"""
    # Всегда показываем кнопку WebApp
    keyboard = create_webapp_keyboard()
    button_text = get_button_text()
    
    await update.message.reply_text(
        f"Используйте кнопку '{button_text}' для открытия приложения.",
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
    button_text = get_button_text()
    version = get_button_version()
    print("✅ Бот запущен и готов к работе!")
    print(f"📱 URL мини-приложения: {WEB_APP_URL}")
    print(f"🔘 Текст кнопки: {button_text}")
    print(f"📌 Версия кнопки: {version}")
    print(f"💡 Версия меняется автоматически при каждом обновлении HTML!")
    application.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()

