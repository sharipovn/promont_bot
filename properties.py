ask_contact=[[{'text': "📞 Kontaktimni jo'natish ⬆️", 'request_contact': True}]]

restart_keyboard = [['🔄 Qayta boshlash']]

unknown_error = (
    "⚠️ Biror xatolik ro'y berdi!\n"
    "⚠️ Произошла ошибка!\n"
    "⚠️ An error occurred!\n"
)

only_your_contact = (
    "✅ Iltimos, foydalanish uchun faqat o'zingizni kontaktingizni yuboring.\n"
    "✅ Пожалуйста, отправьте только свой контакт для использования.\n"
    "✅ Please send only your own contact to use.\n"
)

not_working_bot = (
    "⚠️ Bot vaqtincha ishchi holatida emas!\n"
    "⚠️ Бот временно не работает!\n"
    "⚠️ The bot is temporarily unavailable!\n"
)

ask_contact_msg = (
    "❕ Botdan foydalanish uchun kontaktingizni yuboring!\n"
    "❕ Для использования бота отправьте свой контакт!\n"
    "❕ To use the bot, please send your contact!\n"
)

check_contact_msg = (
    "❕ Kontaktingiz tekshirilmoqda!\n"
    "❕ Ваш контакт проверяется!\n"
    "❕ Your contact is being verified!\n"
)

permission_message = (
    "⚠️ Sizda botdan foydalanish uchun ruxsatnoma mavjud emas!\n"
    "⚠️ У вас нет разрешения на использование бота!\n"
    "⚠️ You do not have permission to use the bot!\n"
)

send_correct_msg = (
    "❗️ To'g'ri ma'lumot kiriting!\n"
    "❗️ Введите правильные данные!\n"
    "❗️ Please enter the correct information!\n"
)

unknown_command = (
    "⚠️ Mavjud bo'lmagan komanda!\n"
    "⚠️ Несуществующая команда!\n"
    "⚠️ Unknown command!"
)


languages=[[{'text': '🟡 O‘zbek', 'callback_data': 'uz'},{'text': '🔵 Русский', 'callback_data': 'ru'},{'text': '🟢 English', 'callback_data': 'en'}]]
 
bot_access_msg = (
    "✅ Botdan foydalanish uchun ruxsat bor!\n"
    "Bildirishnomalar shu yerga keladi.\n"
    "<strong>Tilni tanlang:</strong>\n\n"

    "✅ У вас есть доступ к боту!\n"
    "Уведомления будут приходить сюда.\n"
    "<strong>Выберите язык:</strong>\n\n"

    "✅ You can use the bot!\n"
    "Notifications will arrive here.\n"
    "<strong>Choose language:</strong>"
)



language_codes= ['en','ru','uz']

bot_token='8217778691:AAEaKkCRYPDcwbjIsT4Hmrbd3aGrJ4EmRUU' #REAL
#bot_token='6470196956:AAESN6Fxzp3F6TRQHf_Apj0SK0S6ud2rHRY' #testpurpose
telegram_api = f'https://api.telegram.org/bot{bot_token}/'

db_params = {
    'dbname': 'caslab',
    'user': 'promont_user',
    'password': 'promont_user',
    'host': '192.168.14.171',
    'port': '5432'
}

