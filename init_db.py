import sqlite3

# Подключаемся к базе (файл создастся автоматически)
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Создаём таблицу products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')

# Добавляем товары
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("apple", 100))
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("banana", 80))
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("cherry", 150))

# Сохраняем изменения
conn.commit()

# Проверяем, что добавилось
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
print("Товары в базе данных:")
for row in rows:
    print(row)

# Закрываем соединение
conn.close()