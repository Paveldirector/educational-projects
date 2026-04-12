import sqlite3 

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY,
               name TEXT,
               price INTEGER
               )
               ''')

cursor.execute("INSERT INTO products (name,price) VALUES (?,?)", ("apple", 100))
cursor.execute("INSERT INTO products (name,price) VALUES (?,?)", ("banana", 80))
cursor.execute("INSERT INTO products (name,price) VALUES (?,?)", ("cherry", 150))

conn.commit()

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

def big_price(rows):
    spisok = []
    for id, n, p in rows:
        if p > 90:
            if n not in spisok:
                spisok.append(n)
    return spisok

print(big_price(rows))

cursor.execute("SELECT name FROM products WHERE price > 90")
expensive_names = [row[0] for row in cursor.fetchall()]
print(expensive_names)  # ['apple', 'cherry']

conn.close()