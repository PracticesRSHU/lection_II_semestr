#DDL SQL
"""
Cтворимо базу даних ishop.db
і таблицю сomputers, яка буде містити інформацію про товари інтернет-магазину комп’ютерної техніки. У таблиці будуть міститися такі поля:
•id - унікальний номер товару (первинний ключ)
•name - назва товару (рядок змінної довжини)
•count - кількість одиниць конкретного товару (ціле число)
•price - ціна одного екземпляру конкретного товару (дійсне число)

і таблицю users, яка буде містити інформацію про користувачів інтернет-магазину комп’ютерної техніки. У таблиці будуть міститися такі поля:
•id - унікальний номер товару (первинний ключ), автоматично запонюватиметься поле
•firstname - імя користувача (рядок змінної довжини)
•secondname - прізвище користувача (рядок змінної довжини)
•adress - адреса користувача (рядок змінної довжини)

і таблицю orders, яка буде містити інформацію про замовлення користувачами товарів інтернет-магазину комп’ютерної техніки. У таблиці будуть міститися такі поля:
•id - унікальний номер товару (первинний ключ), автоматично запонюватиметься поле
•user_id - id корстувача із таблиці users в поточному замовленні, який зробив покупку (ціле число і не NULL, є зовнішнім ключем, що зв'язується з таблицею users)
•computers_id - id товару із таблиці computers поточного замовлення (ціле число і не NULL,є зовнішнім ключем, що зв'язується з таблицею computers)
•date_order - дата замовлення (формат дати і часу DATETIME за замовчуванням буде записувати дату додавання замовлення в
  таблицю orders DEFAULT CURRENT_TIMESTAMP)
"""

import sqlite3

conn = sqlite3.connect('ishop.db')  # connection
curs = conn.cursor()

curs.execute('''CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname VARCHAR(20) NOT NULL,
            secondname VARCHAR(20) NOT NULL,
            adress VARCAHR(50) NOT NULL)''')

curs.execute('''CREATE TABLE computers(
            id INT PRIMARY KEY,
            name VARCHAR(20),
            count INT,
            price FLOAT)''')

curs.execute("""CREATE TABLE  orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INT NOT NULL,
            computers_id INT NOT NULL,
            date_order DATETIME DEFAULT CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
            FOREIGN KEY (computers_id) REFERENCES computers (id) ON DELETE CASCADE )"""
             )

conn.commit()
curs.close()
conn.close()
