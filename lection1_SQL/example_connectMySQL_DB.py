#потрібно в терміналі  інсталювати:
# pip install mysql-connector-python

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="password", db="shop_internet")
curs=con.cursor()
curs.execute("SELECT * FROM users")
result = curs.fetchall()
print(result)
curs.close()
con.close()
