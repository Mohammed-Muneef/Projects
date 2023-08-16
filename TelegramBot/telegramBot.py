import os

import telebot
from dotenv import load_dotenv

load_dotenv('bot.env')

bot_token = os.getenv('BOT_TOKEN')
# print(bot_token)

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "fuck off")

bot.infinity_polling()
