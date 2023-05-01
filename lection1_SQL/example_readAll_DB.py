import sqlite3
import pandas as pd
#приклад використання модуля os для роботи з файлами
# import os
# db_file=os.getcwd()+'\ishop.db' #отримати повний шлях до файла бази даних
# print(db_file)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(BASE_DIR, 'ishop.db')
# print(my_file)

# conn = sqlite3.connect('ishop.db')
# curs = conn.cursor()
# curs.execute('''SELECT * FROM сomputers ''')
# conn.commit()
# rows = curs.fetchall()
# print(len(rows))
# for row in rows:
#     print("id: ", row[0]," marka: ", row[1]," count: ", row[2], " price: ",row[3])
# curs.close()
# conn.close()

#вибірка з однієї таблиці
# conn = sqlite3.connect(db_file)
# curs = conn.cursor()
# curs.execute("DELETE FROM сomputers WHERE price>11000")
# conn.commit()
# curs.close()
# conn.close()

pd.options.display.max_columns=10

# вибірка з кількох таблиць
conn = sqlite3.connect('ishop.db')
curs = conn.cursor()
curs.execute('''SELECT  o.id, o.date_order, u.secondname, c.name,c.price FROM  orders as o 
                JOIN users as u ON u.id=o.user_id 
                JOIN computers as c ON c.id=o.computers_id ;''')
# print(pd.read_sql('''SELECT  o.id, o.date_order, u.secondname, c.name,c.price FROM  orders as o
#                 JOIN users as u ON u.id=o.user_id
#                 JOIN computers as c ON c.id=o.computers_id
#                 WHERE o.id=2;''',conn))
# conn.commit()
rows = curs.fetchall()
print(len(rows))
print(rows)
for row in rows:
    print("id order: ", row[0], "date: ",row[1], "users: ",row[2], "product: ", row[3]," price: ",row[4])
curs.close()
conn.close()

# вибірка з таблиці users
# conn = sqlite3.connect('ishop.db')
# curs=conn.cursor()
# curs.execute("SELECT * FROM users")
# result_users=curs.fetchmany(2)
# print(result_users)
# curs.close()
# conn.close()
