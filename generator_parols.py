import random
def generate_password(lenght, chars):
    password=" "
    for i in range(lenght):
        password += random.choice(chars)
    return password
passwords=int(input('введите количество паролей: '))
for i in range(passwords):
    print('Символы и буквы, которые возможны в пароле: ')
    digits="0123456789"
    lowercase_letters='abcdefghijklmnopqrstuvwxyz'
    uppcase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuacion="~!@$^&*_-`"
    print('Цифры: ',digits)
    print('Буквы нижнего регистра: ',lowercase_letters)
    print('Буквы вернего регистра: ',uppcase_letters)
    print('Специальные символы: ',punctuacion)
    chars=""
    lengh=int(input('Введите длину пароля: '))
    di=input('Добавить цифры?\n1-да\n2-нет\n')
    if di=='1':
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
    print('ваш пароль готов: ',generate_password(lengh,chars))
    print('Спасибо, что использовали наш генератор паролей!')

