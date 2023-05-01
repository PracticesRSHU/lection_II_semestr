import sqlite3

# conn = sqlite3.connect('ishop.db')
# curs = conn.cursor()
# qt ='INSERT INTO сomputers VALUES(1, "PC", 5, 7570.50)'
# curs.execute(qt)
# curs.execute('INSERT INTO сomputers VALUES(2, "Notebook", 8, 11430.30)')
# conn.commit()
# curs.close()
# conn.close()

# безпечний спосіб додавання даних - використовуючи заповнювач у вигляді ?:
# conn = sqlite3.connect('ishop.db')
# curs = conn.cursor()
# # curs.execute('INSERT INTO сomputers (id, name, count, price) VALUES(?, ?, ?, ?)', (3, 'NoteX', 7, 7970.20))
# ins = 'INSERT INTO сomputers (id, name, count, price) VALUES(?, ?, ?, ?)'
# curs.execute(ins, (4, 'Sumsung', 3, 11780.90))
# conn.commit()
# curs.close()
# conn.close()


conn = sqlite3.connect('ishop.db')
curs = conn.cursor()
qt = 'INSERT INTO computers VALUES(1, "PC", 5, 7570.50)'
curs.execute(qt)
curs.execute('INSERT INTO computers VALUES(2, "Notebook", 8, 11430.30)')
curs.execute('INSERT INTO users (firstname, secondname,adress) VALUES("Anna", "Vakula", "Rivne")')
curs.execute('INSERT INTO users (firstname, secondname,adress) VALUES("Olga", "Ponomarenko", "Lviv")')
curs.execute("INSERT INTO orders (user_id, computers_id) VALUES(1, 2)")
curs.execute("INSERT INTO orders (user_id, computers_id) VALUES(2, 2)")
conn.commit()
curs.close()
conn.close()
