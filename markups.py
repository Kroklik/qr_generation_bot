from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton('Генерировать'))
    return markup
