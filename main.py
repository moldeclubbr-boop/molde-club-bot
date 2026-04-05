import telebot
import os
from openai import OpenAI

TOKEN = os.getenv("TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

@bot.message_handler(func=lambda message: True)
def handle(message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message.text}]
    )
    
    reply = response.choices[0].message.content
    bot.reply_to(message, reply)

bot.infinity_polling()
