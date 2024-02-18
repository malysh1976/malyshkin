import telebot
from telebot import types
import alhimi
import random
bot = telebot.TeleBot('6365100027:AAESUZPeAmVhDtcAPwSGJPl7IS8LINciRIs')
promocodes=[
    "Пятерочка - СТАРТ25 (-25% на любые товары магазина)",
    "Пятерочка - СКДК (Купон -500р. на заказ любых товаров)",
    "Пятерочка - МИНУС10 (Скидка 10% на заказ доставки)",
    'OZON - POPPI2473510 (-10% при покупке картин по номерам)',
    'Яндекс Маркет - PYTV500-AF (-5% на вашу покупку по промокоду)'
]

start_keyboard = {
    'Промокоды':'codes',
    "Добавить промокод":'new_code',
}

def inline_keyboards_create(dictionary : dict, NumberColumns=1):
    keyboards = types.InlineKeyboardMarkup(row_width=NumberColumns)
    btn_names = [types.InlineKeyboardButton(text=key, callback_data=value) for key, value in dictionary.items()]
    keyboards.add(*btn_names)
    return keyboards

@bot.message_handler(commands=['start'])
def start(message):   
    user_id = message.from_user.id
    if db.get_user(user_id):
        bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=inline_keyboards_create(start_keyboard))
    else:
        db.register(str(user_id), message.from_user.username)
        bot.send_message(message.chat.id, 'Спасибо за регистрацию, Добро пожаловать!')

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    callback_data = call.data
    if callback_data == 'new_code':
        new_code(call)
    elif callback_data == 'codes':
        code_get(call)


def code_get(call):
    code = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        text=f"Ваш промокод: {random.choice(promocodes)}")    

def new_code(call):
    name= call.message.text
    bot.send_message(chat_id=call.message.chat.id,
                    text="Введите промокод:\n Образец: промокод (Описание)")
    bot.register_next_step_handler(call.message, code_name, name)

def code_name(message, name):
    price = message.text
    list_profile = [price, name]
    bot.send_message(chat_id=message.chat.id,
                        text="Введите скидку:\n ")
    
    bot.register_next_step_handler(message, skidka, list_profile)
        
        
def skidka(message, list_profile):
    skidka = message.text
    db.new_code(name=name, price=price)
    bot.send_message(chat_id=message.chat.id,
                    text="Успешно добавлено!")


if __name__ == '__main__':
    db = alhimi.Database()
    bot.infinity_polling()