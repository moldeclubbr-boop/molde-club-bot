import telebot
import os
import requests

# Tokens from environment variables
TOKEN = os.environ["TOKEN"]
OPENROUTER_KEY = os.environ["OPENROUTER_KEY"]

# Initialize bot
bot = telebot.TeleBot(TOKEN)

def ask_ai(text):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {os.environ.get('OPENROUTER_KEY', '')}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": text}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]

        # если AI не сработал
        return "AI сейчас недоступен 😅 попробуй позже"

    except:
        return "AI временно не работает 😴"

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
