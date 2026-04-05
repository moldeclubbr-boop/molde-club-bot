import telebot
import os
import requests

# Tokens from environment variables
TOKEN = os.environ["TOKEN"]
OPENROUTER_KEY = os.environ["OPENROUTER_KEY"]

# Initialize bot
bot = telebot.TeleBot(TOKEN)


def ask_ai(text):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "user", "content": text}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    return result["choices"][0]["message"]["content"]


@bot.message_handler(func=lambda message: True)
def handle(message):
    try:
        answer = ask_ai(message.text)
    except Exception as e:
        print(e)
        answer = "Ошибка AI 😅"

    bot.reply_to(message, answer)


# Start bot
bot.infinity_polling()
