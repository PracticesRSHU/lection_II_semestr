import sqlite3

conn = sqlite3.connect('ishop.db')
curs = conn.cursor()
# ПРОПУЩЕНИЙ ФРАГМЕНТ КОДУ
curs.execute("UPDATE сomputers  SET price=price-price*0.2 WHERE count>7")
conn.commit()
curs.close()
conn.close()
