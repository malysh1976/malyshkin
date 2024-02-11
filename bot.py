import telebot
import sqlite3
import main
balance=1000
token = '6365100027:AAESUZPeAmVhDtcAPwSGJPl7IS8LINciRIs' 
bot=telebot.TeleBot(token)
shop={
    'Молоко':200,
    "Хлеб":300,
    'Печенье':500,
}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if db.get_user(user_id):
        bot.send_message(message.chat.id, 'Добро пожаловать!')
    else:
        db.register(str(user_id),message.from_user.username)
        bot.send_message(message.chat.id, 'Спасибо за регистрацию, Добро пожаловать!')
        bot.send_message(message.chat.id, f'Ваш баланс - {balance}')
        bot.send_message(message.chat.id, reply_markup=generator_keyboards([f"Хлеб - {'Хлеб'}"]))

def generator_keyboards(ListNameBTN, NumberColumns = 2):
    keyboards = telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns, resize_keyboard=True)
    btn_names = [telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards


if __name__ == '__main__':
    db = main.Database()
    bot.infinity_polling()
