from config import token
import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def swnd_hello(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, и умею делать...')

bot.infinity_polling()