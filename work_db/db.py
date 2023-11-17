import sqlite3

connect = sqlite3.connect("work_db/shop.db")
cursor = connect.cursor()
# persons = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(50), 
        price INTEGER ,
        count INTEGER                     
    )                          
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS persons(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(50), 
        surname VARCHAR(50) ,
        work VARCHAR(50)                     
    )                          
""")

# with open("work_db\\script.sql", 'r') as f:
#     cursor.executescript(f.read())

# product2 = ["MacBookPro17", 2354, 20]

product_list = [
    # ['Samsung Galaxy S90', 300, 100],
    # ['Lenovo R34', 200, 15]
]

cursor.executemany("INSERT INTO products(name, price, count) VALUES (?, ?, ?)", product_list)
connect.commit()
with open("script2.sql", 'r') as f:
    cursor.executescript(f.read())
# cursor.execute("INSERT INTO persons(name, surname, work) VALUES ('Vladimir','Sobov', 'Helper')")
# connect.commit()

cursor.execute("SELECT * FROM products")
# cursor.execute("SELECT * FROM categories")

products = cursor.fetchall()
print(products)

cursor.close()
connect.close()