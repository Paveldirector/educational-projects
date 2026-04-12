import sqlite3
import os
print("Текущая папка:", os.getcwd())
# 1. Создай базу и таблицу
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        UNIQUE(name,age)       
    )
''')

# 2. Добавь данные
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()

# 3. Прочитай данные
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# 4. Преврати кортежи в словари (ты это уже умеешь!)
users = [{"id": row[0], "name": row[1], "age": row[2]} for row in rows]
print(users)

conn.close()