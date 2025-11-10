"""
РАБОЧИЙ КОД БОТА для полноэкранного режима мини-приложения
ВАЖНО: Используйте KeyboardButton с web_app, НЕ InlineKeyboardButton!
"""

from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Ваш токен бота
BOT_TOKEN = "7171341328:AAFn6u2zdI3Ht8gCUtFmPvnt4n-aPPednLw"

# URL вашего мини-приложения (ОБЯЗАТЕЛЬНО HTTPS!)
WEB_APP_URL = "https://guglshotir-ops.github.io/azizaliev/"

# Версия кнопки - МЕНЯЙТЕ ЭТО ПРИ КАЖДОМ ОБНОВЛЕНИИ HTML В GITHUB!
# Формат: test_1, test_2, test_3 и т.д.
# Я буду автоматически менять эту версию при каждом обновлении HTML
BUTTON_VERSION = "test_6"  # Увеличьте номер при каждом обновлении HTML: test_1 → test_2 → test_3...

def get_button_text():
    """Генерирует текст кнопки с версией"""
    return BUTTON_VERSION  # "test_1", "test_2" и т.д.

def create_webapp_keyboard():
    """Создает клавиатуру с кнопкой WebApp для полноэкранного режима"""
    button_text = get_button_text()
    
    # КРИТИЧЕСКИ ВАЖНО: KeyboardButton с web_app, НЕ InlineKeyboardButton!
    # Согласно документации: web_app работает только в приватных чатах
    web_app_info = WebAppInfo(url=WEB_APP_URL)
    web_app_button = KeyboardButton(
        text=button_text,  # Динамический текст кнопки с версией
        web_app=web_app_info  # URL мини-приложения
    )
    
    # Проверка для отладки
    print(f"🔍 Создана кнопка: text='{button_text}', url='{WEB_APP_URL}'")
    print(f"🔍 Тип кнопки: KeyboardButton с web_app")
    
    # Создаем клавиатуру
    keyboard = ReplyKeyboardMarkup(
        [[web_app_button]],  # Кнопка в одной строке
        resize_keyboard=True,  # Автоматически изменять размер
        one_time_keyboard=False,  # Кнопка остается видимой
        input_field_placeholder="Нажмите кнопку для открытия приложения"
    )
    
    return keyboard

async def start(update, context):
    """Обработчик команды /start"""
    # Проверка типа чата для отладки
    chat_type = update.effective_chat.type
    print(f"🔍 Команда /start от пользователя {update.effective_user.id} в чате типа: {chat_type}")
    
    keyboard = create_webapp_keyboard()
    button_text = get_button_text()
    
    await update.message.reply_text(
        "👋 Добро пожаловать!\n\n"
        f"Нажмите кнопку '{button_text}' ниже для открытия приложения в полноэкранном режиме.\n\n"
        f"📱 URL: {WEB_APP_URL}\n"
        f"💬 Тип чата: {chat_type}",
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
    print("✅ Бот запущен и готов к работе!")
    print(f"📱 URL мини-приложения: {WEB_APP_URL}")
    print(f"🔘 Текст кнопки: {button_text}")
    print(f"📌 Версия кнопки: {BUTTON_VERSION}")
    application.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()

