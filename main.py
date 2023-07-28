import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')


@bot.message_handler (commands=[ 'start'])
def start(message):
    bot.send_message(message. chat.id, f'<b>Привет</b>,<i>{message.from_user.first_name}</i>.ЕГЭ-это штука, при сдаче которой ты обеспечишь себя благополучием хотя бы ближайшие 5 лет,поэтому хватит болтовни погнали!/subject←тут ты найдешь все что тебе надо',parse_mode='html')


@bot.message_handler(commands=['subject'])
def subject(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
    btn1 = types.KeyboardButton('/maths')
    btn2 = types.KeyboardButton('/russian')
    btn3 = types.KeyboardButton('/physics')
    btn4 = types.KeyboardButton('/history')
    btn5 = types.KeyboardButton('/chemistry')
    btn6 = types.KeyboardButton('/literature')
    btn7 = types.KeyboardButton('/geography')
    btn8 = types.KeyboardButton('/english')
    btn9 = types.KeyboardButton('/information')
    btn10 = types.KeyboardButton('/german')
    btn11 = types.KeyboardButton('/french')
    btn12 = types.KeyboardButton('/stop')
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12)
    mess = f'{message.from_user.first_name},<b>Время учиться!</b>'
    bot.send_message(message.chat.id,mess, parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message. chat.id, f'Оки <b>{message.from_user.first_name}</b>, если что я здесь)',parse_mode='html')


@bot.message_handler(commands=['maths'])
def maths(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по матеше.',url='https://skysmart.ru/articles/mathematic/kak-podgotovitsya-k-ege-po-matematike'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['russian'])
def russian(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по русскому языку.',url='https://maximumtest.ru/free-lessons/russkij'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)

@bot.message_handler(commands=['physics'])
def physics(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по физике.?',url='https://media.foxford.ru/articles/9-advice-ege-physics'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['history'])
def history(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по истории.',url='https://examer.ru/ege_po_istorii/teoriya'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['chemistry'])
def chemistry(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по химии.',url='https://egeturbo.ru/chem'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['literature'])
def literature(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по лит-ре.',url='https://www.kp.ru/edu/shkola/podgotovka-k-ege-po-literature/'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['geography'])
def geography(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по географии.',url='https://tetrika-school.ru/blog/podgotovka-k-ege-po-geografii/'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['english'])
def english(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайтик по англисскому.',url='https://rosuchebnik.ru/material/intensivnaya-podgotovka-k-ege-po-angliyskomu-yazyku/'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['information'])
def information(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайтик по информатике.",url='https://www.labirint.ru/genres/2781/'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['german'])
def german(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайтик по немецкому языку.",url='https://lingvoelf.ru/podgotovka-k-ege-po-nemetskomu-yazyku'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler(commands=['french'])
def french(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайтик по францускому языку.",url='https://repetit.ru/repetitors/frantsuzskiy-yazyk/ege/'))
    bot.send_message(message. chat.id,f'<i>Смотри ниже↓</i>',parse_mode='html',reply_markup=markup)


@bot.message_handler()
def other(message):
    if message.text.lower() == 'hi':
        bot.send_message (message.chat.id, f' {message.from_user.first_name}')
    else:
        bot.send_message(message.chat.id,f'$#@!#$-сможешь прочитать?Вот и тебя не понимаю!')


bot.polling(none_stop=True)