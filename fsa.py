import random
import time
player={
    'name':'player',
    'hp':5,
    'dmg':1,
}

boss={
    'name':'Ворон',
    'hp':10,
    'dmg':1,
}
locate=['мрачный','светлый','старый']
loc=["дом","лес","особняк"]
player['name']=input("Введите имя вашего игрока: ")

def fight(player,boss):
    while player['hp']>0 and boss['hp']>0:
        time.sleep(2)
        dam=random.randint(1,5) * player['dmg']
        boss['hp']-=dam
        print(f'Вы нанесли {dam} урона!')

while True:
    print(f'Добро пожаловать в игру, {player["name"]}!')
    time.sleep(2)
    print(f'Вы попдаете в {random.choice(locate)} {random.choice(loc)}...')
    print(f'Перед вами появляется босс {boss["name"]}')
    fight(player,boss)
    break







