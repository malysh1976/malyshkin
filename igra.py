import random
words=['солнце','снегирь',"ковров","куб"]


def get_ask():
    return random.choice(words)

def play(word):
    print('Я загадал слово, попробуй его отгадать!')
    word_ask="_"*len(word)
    hp=6
    win=False
    print(f"загаданное слово:{word_ask}")
    while not win and hp>0:
        ask=input('Введите букву:'.lower())


        if ask in word:
            print('Отличная работа, буква',ask,'присутствует в слове!')
            word_as_list=list(word_ask)
            indices=[i for i in range(len(word)) if word[i]==ask]
            for index in indices:
                word_as_list[index]=ask
                word_ask=''.join(word_as_list)
                if "_" not in word_ask:
                    win=True
        else:
            hp-=1
            print(f'буквы {ask} нет в слове. Осталось {hp} попыток ')
        print(word_ask)
again='д'
while again.lower()=='д':
    word=get_ask()
    play(word)
    again=input('Играем еще раз? (д = да,н = нет):')        
