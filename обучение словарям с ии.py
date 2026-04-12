students = [
    {"name": "John", "score": 85},
    {"name": "Emma", "score": 92},
    {"name": "Alex", "score": 78},
    {"name": "Sarah", "score": 88}
]

# Задание: отфильтровать, отсортировать, получить имена
# Ожидаемый результат: ["Emma", "Sarah", "John"]

# Напиши код здесь (3 строчки):
filtered = [i for i in students if i.get('score')>=80]
sorted_students = sorted(filtered,key=lambda x: x['score'],reverse=True)
result = [i['name'] for i in sorted_students]
print(result)
# ИЛИ в одну строку:
res = [i['name'] for i in sorted(filtered,key=lambda x: x['score'],reverse=True) if i.get('score')>=80]
print(res)