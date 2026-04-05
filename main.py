import telebot
import os
import requests

# Tokens from environment variables
TOKEN = os.environ["TOKEN"]
OPENROUTER_KEY = os.environ["OPENROUTER_KEY"]

# Initialize bot
bot = telebot.TeleBot(TOKEN)

def ask_ai(text):
    try:API_URL = "https://router.huggingface.co/google/flan-t5-large"
        headers = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN', '')}"}

        payload = {
            "inputs": text
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if isinstance(result, list):
            return result[0].get("generated_text", "Нет ответа")

        return f"Ошибка AI: {result}"

    except Exception as e:
        return f"Crash AI: {str(e)}"

@bot.message_handler(func=lambda message: True)
def handle(message):
    try:
        answer = ask_ai(message.text)
    except Exception as e:
        answer = f"Ошибка: {str(e)}"

    try:
        bot.reply_to(message, answer)
    except Exception as e:
        print(f"Ошибка отправки: {e}")

# Start bot
bot.infinity_polling(none_stop=True, skip_pending=True)
