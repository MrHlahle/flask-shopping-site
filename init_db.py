import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL
    )
''')

# Check if products already exist
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany('''
        INSERT INTO products (name, description, price) VALUES (?, ?, ?)
    ''', [
        ('T-Shirt', 'Comfortable cotton t-shirt', 20.00),
        ('Sneakers', 'Stylish running sneakers', 75.00),
        ('Hat', 'Classic baseball cap', 15.00)
    ])
    print("Sample products inserted.")
else:
    print("Products already exist. Skipping insert.")

conn.commit()
conn.close()
