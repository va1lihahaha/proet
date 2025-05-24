import telebot
import requests
import json


TELEGRAM_TOKEN = ""

TEXTGEARS_API_KEY = ''

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def go_api(text):


    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {TEXTGEARS_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "deepseek/deepseek-prover-v2:free",
        "messages": [
        {
            "role": "user",
            "content": 'Исправь ошибки в тексте и напиши их количеств: ' + text
        }
        ],
        
    })
    )
    # print(response.json()['choices'][0]['message']['content'])
    return response.json()['choices'][0]['message']['content']

@bot.message_handler(commands=['start'])
def on_start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который поможет исправить ошибки в твоём')


@bot.message_handler(content_types=['text'])
def on_text(message):
    answer = go_api(message.text)
    bot.send_message(message.chat.id, answer)


bot.polling()
