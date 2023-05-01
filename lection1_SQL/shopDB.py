import sqlite3

#users, computers, order

class DBShop:
    def __init__(self):
        self.conn = sqlite3.connect('ishop.db')  # connection
        self.curs = self.conn.cursor()
        self.curs.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname VARCHAR(20) NOT NULL,
                    secondname VARCHAR(20) NOT NULL,
                    adress VARCAHR(50) NOT NULL)''')
        self.curs.execute('''CREATE TABLE IF NOT EXISTS computers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(20),
                    count INT,
                    price FLOAT)''')
        self.curs.execute("""CREATE TABLE IF NOT EXISTS  orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INT NOT NULL,
                    computers_id INT NOT NULL,
                    date_order DATETIME DEFAULT CURRENT_TIMESTAMP, 
                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
                    FOREIGN KEY (computers_id) REFERENCES computers (id) ON DELETE CASCADE )"""
                     )
        self.conn.commit()


    def __del__(self):
        self.curs.close()
        # self.curs.close()
        self.conn.close()

    # CRUD operations  => create, read, update(insert), delete
    # CRUD operations  read and delete  with all tables DB
    def selectAll(self,table):
        self.curs.execute(f"SELECT * FROM {table}")
        return self.curs.fetchall()

    def selectAllById(self,table, id):
        self.curs.execute(f"SELECT * FROM {table}  WHERE id=?",(id,)) # (id,)
        return self.curs.fetchall()

    def deleteData(self,table,id):
        self.curs.execute(f"DELETE FROM {table} WHERE id=?",(id,))
        self.conn.commit()

    # CRUD operations  => update(insert) for table users
    def inputDataUsers(self, firstname, secondname, adress):
        self.curs.execute("INSERT INTO users (firstname, secondname, adress) VALUES (?,?,?)",(firstname, secondname, adress))
        self.conn.commit()

    def updateDataUsers(self,firstname, secondname, adress, id):
        self.curs.execute("UPDATE users  SET firstname=?, secondname=?, adress=? WHERE id=?;",
                          (firstname, secondname, adress,id))
        self.conn.commit()

    # CRUD operations  => update(insert) for table computers

    # CRUD operations  => update(insert) for table order



shopDataBase=DBShop()
listUsers=shopDataBase.selectAll("users")
print(listUsers)
userInfo=shopDataBase.selectAllById("users",2)
print(userInfo)
# shopDataBase.inputDataUsers("Lilya","Majdanovich","Lviv")
print(shopDataBase.selectAll("users"))
shopDataBase.updateDataUsers(userInfo[0][1],userInfo[0][2],'Kiyv',userInfo[0][0])
print(shopDataBase.selectAll("users"))
shopDataBase.deleteData("users",8)
print(shopDataBase.selectAll("users"))