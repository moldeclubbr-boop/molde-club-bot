import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle(message):
    bot.reply_to(message, "Я живой 🔥")

bot.infinity_polling()
