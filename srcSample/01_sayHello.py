#!/usr/bin/python3

import os
import telebot

# Set ENV APK_KEY=012345678:XXXxxxxxxxxxxxxxxxxx-xxxxxx
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! How's it going?")

bot.polling()

