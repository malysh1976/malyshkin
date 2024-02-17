import telebot
import sqlite3
import test
balance=1000
token = '6365100027:AAESUZPeAmVhDtcAPwSGJPl7IS8LINciRIs' 
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if db.get_user(user_id):
        bot.send_message(message.chat.id, 'Добро пожаловать!')
    else:
        db.register(str(user_id),message.from_user.username)
        bot.send_message(message.chat.id, 'Спасибо за регистрацию, Добро пожаловать!')
        bot.send_message(message.chat.id, f'Ваш баланс - {balance}')

def generator_keyboards(ListNameBTN, NumberColumns = 2):
    keyboards = telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns, resize_keyboard=True)
    btn_names = [telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards


if __name__ == '__main__':
    db = test.Database()
    bot.infinity_polling()
