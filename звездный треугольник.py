# объявление функции
def draw_triangle():
    height = 8
    width = 15
    for i in range(height):
        spaces = (width - (2 * i + 1)) // 2
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)


# основная программа
draw_triangle()  # вызов функции