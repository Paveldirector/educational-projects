# объявление функции
def print_perm_time_call(msc_time):
    s = msc_time.split(':')
    hours = int(s[0]) + 2
    
    if hours >= 24:
        hours -= 24
    
    s[0] = f"{hours:02d}"
    
    print('Созвон будет в ', end='')
    print(':'.join(s),end='.')
# считываем данные
msc_time = input()

# вызываем функцию
print_perm_time_call(msc_time)