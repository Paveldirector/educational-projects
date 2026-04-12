num = input()  # вводим как строку
n = 0
length = len(num)
for i in range(length):
    n += int(num[i]) * 2 ** (length - 1 - i)
print(n)
print(int('1AF2', 16))