import qrcode
# value = input('Val: ')
# img = qrcode.make(value)
# img.save('qrcode.png')
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup
import config
from markups import *

bot = TeleBot(config.TOKEN)

file_path = 'qr_code.png'


def save_qr_code_to_png(value: str, file_path: str):
    img = qrcode.make(value)
    img.save(file_path, format='PNG')


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, 'Привет, я могу сгенерировать любой QR-code! Просто нажми на кнопку',
                     reply_markup=generate())


@bot.message_handler(regexp='Генерировать')
def gen(message: Message):
    chat_id = message.from_user.id
    msg = bot.send_message(chat_id, 'Отправьте мне текст или ссылку, чтобы сгенерировать QR')
    bot.register_next_step_handler(msg, send_qr)


def send_qr(message: Message):
    chat_id = message.from_user.id
    try:
        if message.text:
            value = message.text
        else:
            pass
        img = qrcode.make(value)
        filename = f'media/qrcode{chat_id}.png'
        img.save(filename)
        with open(filename, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
    except Exception as e:
        print(e)
    gen(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
