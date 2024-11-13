import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    """)
for i in range(1, 5):
    cursor.execute('INSERT OR REPLACE INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)',
                   (f'{i}', f'Продукт {i}', f'Описание {i}', i * 100))

    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    connection.close()
    return prod


# connection.commit()
# connection.close()
