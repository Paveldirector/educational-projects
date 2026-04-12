# Импортируем нужные библиотеки
from fastapi import FastAPI, Body
from contextlib import asynccontextmanager  # для lifespan
import asyncpg

# Параметры подключения к PostgreSQL (внутри Docker Compose)
DATABASE_URL = "postgresql://myuser:mypassword@db:5432/mydb"

# 1. СНАЧАЛА функция подключения к БД
async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    return conn

# 2. ПОТОМ lifespan, который её использует
@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = await get_db()  #
    await conn.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')
    await conn.close()
    yield

# 3. ПОТОМ создаём приложение
app = FastAPI(lifespan=lifespan)

# ========== ЭНДПОИНТЫ ==========

# 1. Главная страница (проверка что сервер работает)
@app.get("/")
def home():
    return {"message": "API работает с PostgreSQL!"}

# 2. Получить все товары (GET - читаем данные)
@app.get("/products")
async def get_products(): 
    conn = await get_db()                     # await - подключаемся к БД (ждём ответа от сети)
    rows = await conn.fetch("SELECT * FROM products")
    products = [dict(row) for row in rows]    # превращаем результат в список словарей
    await conn.close()                        # закрываем БД
    return products                           # отправляем результат в браузер

# 3. Получить дорогие товары (цена > 90)
@app.get("/products/expensive")
async def get_expensive():
    conn = await get_db()
    rows = await conn.fetch("SELECT * FROM products WHERE price > 90")
    await conn.close()
    return [dict(row) for row in rows]

# 4. Получить дешёвые товары (цена < 100)
@app.get("/products/cheap")
async def get_cheap():
    conn = await get_db()
    rows = await conn.fetch("SELECT * FROM products WHERE price < 100")  # вместо ? используем $1, но тут нет параметров
    await conn.close()
    return [dict(row) for row in rows]

# 5. Получить один товар по его ID (например: /products/3)
@app.get("/products/{product_id}")
async def get_product(product_id: int):       # product_id приходит из адреса
    conn = await get_db()
    # $1 - это место для подстановки значения (в PostgreSQL вместо ?)
    row = await conn.fetchrow("SELECT * FROM products WHERE id = $1", product_id)
    await conn.close()
    
    if row is None:                           # если товара с таким ID нет
        return {"error": "Товар не найден"}
    
    return dict(row)

# 6. ДОБАВИТЬ новый товар (POST - создаём данные)
@app.post("/products")
async def create_product(
    name: str = Body(...),    # Body(...) значит "обязательное поле name из тела запроса"
    price: int = Body(...)    # Body(...) значит "обязательное поле price из тела запроса"
):
    conn = await get_db()
    # Вставляем новый товар в таблицу
    # RETURNING id - возвращает ID созданной записи
    row = await conn.fetchrow(
        "INSERT INTO products (name, price) VALUES ($1, $2) RETURNING id",
        name, price
    )
    await conn.close()
    
    # Возвращаем созданный товар с его новым ID
    return {
        "id": row["id"],      # ID из PostgreSQL
        "name": name,
        "price": price
    }

# 7. УДАЛИТЬ товар (DELETE - удаляем данные)
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):    # ID товара, который хотим удалить
    conn = await get_db()
    
    # Сначала проверим, существует ли такой товар
    row = await conn.fetchrow("SELECT * FROM products WHERE id = $1", product_id)
    
    if row is None:                           # товара нет
        await conn.close()
        return {"error": f"Товар с id={product_id} не найден"}
    
    # Товар есть — удаляем его
    await conn.execute("DELETE FROM products WHERE id = $1", product_id)
    await conn.close()
    
    return {"message": f"Товар с id={product_id} удалён", "deleted": dict(row)}

# 8. ИЗМЕНИТЬ товар (PUT - обновляем данные)
@app.put("/products/{product_id}")
async def update_product(
    product_id: int,                # ID товара, который меняем (берётся из адреса)
    name: str = Body(...),          # новое название (берётся из тела запроса)
    price: int = Body(...)          # новая цена (берётся из тела запроса)
):
    conn = await get_db()
    
    # 1. Проверяем, существует ли товар с таким ID
    row = await conn.fetchrow("SELECT * FROM products WHERE id = $1", product_id)
    
    if row is None:
        await conn.close()
        return {"error": f"Товар с id={product_id} не найден"}
    
    # 2. Товар существует — обновляем его
    await conn.execute(
        "UPDATE products SET name = $1, price = $2 WHERE id = $3",
        name, price, product_id   # порядок важен: name, price, id
    )
    await conn.close()
    
    # 3. Возвращаем обновлённый товар
    return {
        "message": "Товар обновлён",
        "updated": {
            "id": product_id,
            "name": name,
            "price": price
        }
    }