from datetime import date

import telebot

from settings import API_KEY
from queries import GetTable

def ConvertTime(time:str) -> date:
    day, month, year = [int(item) for item in time.split('.')]
    return date(year, month, day)


bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.KeyboardButton("Проверить")
    markup.add(btn)
    bot.send_message(m.chat.id, 'Нажмите "Проверить" чтобы вывести список заказов с прошедшим сроком', reply_markup= markup)

@bot.message_handler(content_types=['text'])
def handler_text(message):
    # row[3] - строка с датой
    expire_rows = tuple(filter(lambda row: ConvertTime(row[3]) < date.today(), GetTable()))
    result = 'Заказы с прошедшим сроком:\n' + '\n'.join([str(row) for row in expire_rows])
    bot.send_message(message.chat.id, result)

bot.polling(none_stop=True, interval=0)