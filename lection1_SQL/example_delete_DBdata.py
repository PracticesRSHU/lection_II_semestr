import sqlite3

conn = sqlite3.connect('ishop.db')
curs = conn.cursor()
curs.execute("DELETE FROM сomputers  WHERE id=4")
conn.commit()
curs.close()
conn.close()
