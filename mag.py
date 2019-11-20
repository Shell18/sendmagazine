
import telebot
from telebot import types
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро Пожаловать в магазин,чтобы перезапустить/запустить бота напишите /start')
bot.polling()