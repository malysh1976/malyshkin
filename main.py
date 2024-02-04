import telebot
import random
from telebot import types

bot=telebot.TeleBot('')

keyboard=types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start(message):
    btn1=keyboard.add(types.InlineKeyboardButton('6',callback_data='line1'))
    btn2=keyboard.add(types.InlineKeyboardButton('8',callback_data='line2'))
    btn3=keyboard.add(types.InlineKeyboardButton('10',callback_data='line3'))
    bot.send_message(message.chat.id,f'Какая будет длина Вашего пароля?',reply_markup=keyboard)

def gen_password(message):
    
    digits="0123456789"
    lowercase_letters='abcdefghijklmnopqrstuvwxyz'
    uppcase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuacion="~!@$^&*_-`"
    keyboard.add(types.InlineKeyboardButton('Да',callback_data='yes'))
    keyboard.add(types.InlineKeyboardButton('Нет',callback_data='no'))
    di=bot.send_message(message.chat.id,f'Какая будет длина Вашего пароля?',reply_markup=keyboard)
    if di=='yes':
        chars+=digits
    low=input('Добавить буквы нижнего регистра?\n1-да\n2-нет\n')
    if low=='1':
        chars+=lowercase_letters
    upp=input('Добавить буквы верхнего регистра?\n1-да\n2-нет\n')
    if upp=='1':
        chars+=uppcase_letters
    sp=input('Добавить специальные символы?\n1-да\n2-нет\n')
    if sp=='1':
        chars+=punctuacion
    print('ваш пароль готов: ',gen_password(line,chars))
    print('Спасибо, что использовали наш генератор паролей!')

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data=='line1':
        line=6
    elif call.data=='line2':
        line=8
    elif call.data=='line3':
        line=10

        


        



if __name__=='__main__': 
    bot.infinity_polling()


 