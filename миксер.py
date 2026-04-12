a,b = input(), input()
if (a=='красный'or a=='синий' or a=='желтый') and (b=='красный'or b=='синий' or b=='желтый'):
    if a==b:
        print(a)
    elif a=='красный' and b=='синий' or b=='красный' and a=='синий':
        print('фиолетовый')
    elif a=='красный' and b=='желтый' or b=='красный' and a=='желтый':
        print('оранжевый')
    elif a=='желтый' and b=='синий' or b=='желтый' and a=='синий':
        print('зеленый')
else:
    print('ошибка цвета')