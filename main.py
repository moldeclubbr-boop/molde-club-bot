import telebot
bot = telebot.TeleBot("8682954794:AAEmFzNwtikAA-fgkbW8f4UouMLDPUO8n_E")
@bot.message_handler(func=lambda message: True)
def handle(message):bot.reply_to(message, "Я живой 🔥")
bot.infinity_polling()
