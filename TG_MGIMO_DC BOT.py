# Импорт библиотеки
import telebot
from telebot import types
import pandas as pd
import random

# Подрубаем бота по токену
TOKEN = '1401870538:AAGgEtW5xQw25-G1NigjY0-6EX4lFiyXXUk'
bot = telebot.TeleBot(TOKEN)

# Парс данных с темами
themes = pd.read_csv(r'themes_rus.csv')
themes_eng = pd.read_csv(r'themes_eng.csv')
a = themes['Резолюция'].shape[0]
b = themes_eng['Резолюция'].shape[0]

# Обработка старта
@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Информация о нас')
    button2 = types.KeyboardButton('Как к нам попасть')
    button3 = types.KeyboardButton('Тема для дебатов')
    markup.add(button1,button2,button3)

    bot.send_message(message.chat.id,'Приветствую тебя, {0.first_name}!\n<b>Я MGIMO DC Bot</b>\nВыбери команду'.format(message.from_user),
        parse_mode='html',reply_markup=markup)

# Отправка сообщений
@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == 'Информация о нас':
            bot.send_message(message.chat.id, 'Дебаты - это интеллектуальная ролевая игра, где команды доказывают позицию, выпавшую по жребию\n\nMGIMO DC является одним из крупнейших клубов дебатов в России\n\nНаши ребята участвуют в международных чемпионатах, работают в крутых компаниях и путешествуют по всему миру\n\nЕсли ты хочешь развить навыки критического мышления, научиться делать сильные речи и получить море эмоций, то присоединяйся',
                parse_mode='html')
        elif message.text == 'Как к нам попасть':
            markup3 = types.InlineKeyboardMarkup()
            buttonx = types.InlineKeyboardButton(text='Регистрация',
                                                 url='https://docs.google.com/forms/d/e/1FAIpQLScR3McA4NI5iO1UGW3UOdNFoNcq52oXUY36uxRyN8rpqHiElw/viewform?vc=0&c=0&w=1&flr=0&gxids=7628')
            markup3.add(buttonx)
            bot.send_message(message.chat.id, 'Презентация нашего клуба состоится совсем скоро!\n\nДля того, чтобы прийти, просто зарегистрируйся:\n\nБолее подробная информация у нас в группе!',
                parse_mode='html',reply_markup=markup3)
        elif (message.text == 'Тема для дебатов') or ('дай тему' in message.text.lower()):
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Тема на русском',callback_data ='one')
            item2 = types.InlineKeyboardButton('Тема на английском',callback_data='two')
            markup.add(item1,item2)
            bot.send_message(message.chat.id,'Выбери язык',reply_markup=markup)
        elif message.text != '':
            bot.send_message(message.chat.id,'Выбери опцию')




@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'one':
                bot.send_message(call.message.chat.id,themes['Резолюция'][random.randint(2153, a)])
            elif call.data == 'two':
                bot.send_message(call.message.chat.id,themes_eng['Резолюция'][random.randint(0, b)])
            elif call.data == 'three:':
                bot.send_message(call.message.chat.id,'')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Тема:", reply_markup=None)

    except Exception as e:
        print(repr(e))

#Run
bot.polling(none_stop=True)