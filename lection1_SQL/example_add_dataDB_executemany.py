import sqlite3

list_product=[(3, 'NoteX', 7, 7970.20),
              (4, 'Sumsung', 3, 11780.90),
              (5, 'Note7X', 4, 9970.20)]
# безпечний спосіб додавання даних - використовуючи заповнювач у вигляді ?:
conn = sqlite3.connect('ishop.db')
curs = conn.cursor()
# curs.executemany('INSERT INTO сomputers (id, name, count, price) VALUES(?, ?, ?, ?)', list_product)
ins = 'INSERT INTO computers (id, name, count, price) VALUES(?, ?, ?, ?)'
curs.executemany(ins, list_product)
conn.commit()
curs.close()
conn.close()


