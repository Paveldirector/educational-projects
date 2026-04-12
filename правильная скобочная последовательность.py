# объявление функции
def is_correct_bracket(text):
    t = 0
    for i in text:
        if i == '(':
            t += 1
        elif i == ')':
            t -= 1
            if t<0:
                return False
    return t==0
               
        

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))