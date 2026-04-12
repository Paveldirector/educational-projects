# объявление функции
def get_last_index(data, value):
    if value in data:
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                return i
    return 'ERROR!'
# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))