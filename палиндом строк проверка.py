# объявление функции
def is_palindrome(text):
    text = text.lower()
    text = text.replace(' ','')
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace('!','')
    text = text.replace('?','')
    text = text.replace('-','')
    txtr = text[::-1]
    return text == txtr

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))