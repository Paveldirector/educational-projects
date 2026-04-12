a = int(input())
if 0<=a<=36:
    if a==0:
        print('зеленый')
    else:
        if a%2==0 and 1<=a<=10:
            print('черный')
        elif not a%2==0 and 1<=a<=10:
            print('красный')
        if a%2==0 and 11<=a<=18:
            print('красный')
        elif not a%2==0 and 11<=a<=18:
            print('черный')
        if a%2==0 and 19<=a<=28:
            print('черный')
        elif not a%2==0 and 19<=a<=28:
            print('красный')
        if a%2==0 and 29<=a<=36:
            print('красный')
        elif not a%2==0 and 29<=a<=36:
            print('черный')
else:
    print('ошибка ввода')