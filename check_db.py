import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

print("Products:")
for row in rows:
    print(row)

conn.close()
