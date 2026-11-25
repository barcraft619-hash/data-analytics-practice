
import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# 1. Показываем все записи
print("\n=== ВСЕ ПРОДАЖИ ===")

cursor.execute("SELECT * FROM sales")

for row in cursor.fetchall():
    print(row)


# 2. Товары дороже 20 000 тенге
print("\n=== ТОВАРЫ ДОРОЖЕ 20 000 ТЕНГЕ ===")

cursor.execute("""
SELECT product, price
FROM sales
WHERE price > 20000
""")

for row in cursor.fetchall():
    print(row)


# 3. Товары категории Техника
print("\n=== КАТЕГОРИЯ: ТЕХНИКА ===")

cursor.execute("""
SELECT product, category, price
FROM sales
WHERE category = 'Техника'
""")

for row in cursor.fetchall():
    print(row)


# 4. Сортировка от дорогих к дешёвым
print("\n=== СОРТИРОВКА ПО ЦЕНЕ ===")

cursor.execute("""
SELECT product, price
FROM sales
ORDER BY price DESC
""")

for row in cursor.fetchall():
    print(row)


# 5. Количество записей
print("\n=== КОЛИЧЕСТВО ЗАПИСЕЙ ===")

cursor.execute("SELECT COUNT(*) FROM sales")

count = cursor.fetchone()[0]

print("Всего записей:", count)


# 6. Количество категорий
print("\n=== КОЛИЧЕСТВО КАТЕГОРИЙ ===")

cursor.execute("""
SELECT COUNT(DISTINCT category)
FROM sales
""")

categories = cursor.fetchone()[0]

print("Всего категорий:", categories)


# Закрываем соединение
conn.close()

print("\nПроверка завершена!")
