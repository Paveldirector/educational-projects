from random import sample
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
neod = 'il1Lo0O'

def slojnost(cifr, low_l, up_l, punct, neo):
    chars = ''
    if cifr == '+':
        chars += digits
    if low_l == '+':
        chars += lowercase_letters
    if up_l == '+':
        chars += uppercase_letters
    if punct == '+':
        chars += punctuation
    if neo == '+':
        for i in neod:
            if i in chars:
                chars = chars.replace(i,'')
    return chars

def generate_password(kol_vo, length, chars):
    for _ in range(kol_vo):
        (print(''.join(sample(chars, length))) )
    return 'Все пароли сгенерированы.'

kol_vo = int(input('Сколько паролей сгенерировать? '))
length = int(input('\nКакой длинны? '))
cifr = input(f'\nВключать в него {digits}? +/-')
low_l = input(f'\nВключать в него {lowercase_letters}? +/-')
up_l = input(f'\nВключать в него {uppercase_letters}? +/-')
punct = input(f'\nВключать в него {punctuation}? +/-')
neo = input(f'\nИсключать неоднозначные символы {neod} ? +/-')

chars = slojnost(cifr, low_l, up_l, punct, neo)

generate_password(kol_vo, length, chars)

