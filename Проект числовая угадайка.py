from random import *
print('Добро пожаловать в числовую угадайку!')
gr = int(input('Введите границу: '))

def is_valid(n, gr):
    return 0<n<=gr

def play_game(gr):
    z = randint(1, gr)
    total = 0
    while True:
        n = int(input('Введите число: '))
        
        if not is_valid(n, gr):
            print(f'А может быть, всё-таки введём целое число от 1 до {gr}?')
            continue
        
        total += 1
        
        if n < z:
            print('Ваше число МЕНЬШЕ загаданного, попробуйте еще разок.')
        elif n > z:
            print('Ваше число БОЛЬШЕ загаданного, попробуйте еще разок.')
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', total)
            break

while True:
    play_game(gr)
    start = input('Сыграть еще +/-? ')
    if start != '+':
        print('До свидания.')
        break