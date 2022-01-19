import telebot
from BotConfig import BotToken as bt

bot = telebot.TeleBot(bt)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет")
bot.infinity_poling()
