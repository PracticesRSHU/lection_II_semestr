import tkinter as tk
# import tkinter.ttk as ttk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.createNotebook()

    def init_main(self):
        # Example main menu widget Menu with cascsade and command
        # --------------------------------
        # mainbar = tk.Menu(root)
        # tablemenu = tk.Menu(mainbar, tearoff=0)
        # tablemenu.add_command(label="Users",command=self.view_records_users)
        # tablemenu.add_command(label="Computers", command=self.view_records_computers)
        # tablemenu.add_command(label="Order")
        # # tablemenu.add_separator()
        # tablemenu.add_command(label="Exit", command=self.quit)
        # mainbar.add_cascade(label='Таблиці', menu=tablemenu)
        # --------------------------------

        mainbar = tk.Menu(root)
        mainbar.add_cascade(label="Таблиця Users", command=self.view_records_users)
        mainbar.add_cascade(label="Таблиця Computers ", command=self.view_records_computers)
        mainbar.add_cascade(label="Таблиця Order")
        mainbar.add_cascade(label="Exit", command=self.quit)
        root.config(menu=mainbar)

        toolbar = tk.Frame(bg='gray', bd=4)
        toolbar.pack(fill=tk.X)
        # button add
        self.add_img = tk.PhotoImage(file="image_btn/add.png")
        add_button = tk.Button(toolbar, text="Додати запис", background="gray",
                               command=self.open_add_dialog, image=self.add_img)
        add_button.pack(side=tk.LEFT)
        # button edit
        self.edit_img = tk.PhotoImage(file="image_btn/edit.png")
        edit_button = tk.Button(toolbar, text="Додати запис", background="gray",
                                command=self.open_edit_dialog, image=self.edit_img)
        edit_button.pack(side=tk.LEFT)

        # button delete
        self.delete_img = tk.PhotoImage(file="image_btn/delete.png")
        delete_button = tk.Button(toolbar, text="Видалити запис", background="gray",
                                  command=self.delete_records, image=self.delete_img)
        delete_button.pack(side=tk.LEFT)

    # using Notebook
    # ---------------------------------
    def createNotebook(self):
        self.myNotebook = ttk.Notebook(root)
        self.myNotebook.pack(fill=tk.X)
        self.frameComputers = tk.Frame(self.myNotebook, width=640, height=200)
        # self.frameComputers.pack(fill=tk.X)
        self.frameUsers = tk.Frame(self.myNotebook, width=640, height=200)
        # self.frameUsers.pack(fill=tk.X)
        self.treeComp = ttk.Treeview(self.frameComputers, columns=('id', "name", "count", "price"), height=15,
                                     show="headings")
        self.treeUsers = ttk.Treeview(self.frameUsers, columns=('id', "firstname", "secondname", "adress"), height=15,
                                      show="headings")
        self.table_computers()
        self.table_users()

    def addNotebookComputers(self):
        self.myNotebook.add(self.frameComputers, text="Computers")
        self.myNotebook.select(self.myNotebook.index(self.frameComputers))

    def addNotebookUsers(self):
        self.myNotebook.add(self.frameUsers, text="Users")
        self.myNotebook.select(self.myNotebook.index(self.frameUsers))
        # self.myNotebook.select(1)

    # function for open dialog
    # ---------------------------------------------------------------
    def open_add_dialog(self):
        WindowInputDialogComp()

    def open_edit_dialog(self):
        WindowEditDialogComp()

    # function CRUD operations with table "computers "
    def view_records_computers(self):
        data=self.db.selectAllComputers()
        self.addNotebookComputers()
        for i in self.treeComp.get_children():
            self.treeComp.delete(i)
        # [self.treeComp.delete(i) for i in self.treeComp.get_children()]
        for row in data:
            self.treeComp.insert('', 'end', values=row)

    def records_computers(self, name, count, price):
        self.db.input_data_computers(name, count, price)
        self.view_records_computers()

    def update_computers(self, name, count, price,id):
        self.db.update_data_computers(name, count, price,id)
        self.view_records_computers()

    def delete_records(self):
        for selected_record in self.treeComp.selection():
            self.db.delete_data_computers(self.treeComp.set(selected_record, '#1'))
        self.view_records_computers()


    #CRUD operation for users table
    def view_records_users(self):
        data = self.db.selectAllUsers()
        for i in self.treeUsers.get_children():
            self.treeUsers.delete(i)
        self.addNotebookUsers()
        for row in data:
            self.treeUsers.insert('', 'end', values=row)
#create table TeeView
    def table_computers(self):
        self.treeComp.column("id", width=30, anchor=tk.CENTER)
        self.treeComp.column("name", width=160, anchor=tk.CENTER)
        self.treeComp.column("count", width=70, anchor=tk.CENTER)
        self.treeComp.column("price", width=70, anchor=tk.CENTER)

        self.treeComp.heading("id", text="id")
        self.treeComp.heading("name", text='Наіменування товару')
        self.treeComp.heading("count", text='Кількість')
        self.treeComp.heading("price", text='Ціна')
        self.treeComp.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(self, command=self.treeComp.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeComp.configure(yscrollcommand=scrollbar.set)


    def table_users(self):
        self.treeUsers.column("id", width=30, anchor=tk.CENTER)
        self.treeUsers.column("firstname", width=160, anchor=tk.CENTER)
        self.treeUsers.column("secondname", width=70, anchor=tk.CENTER)
        self.treeUsers.column("adress", width=70, anchor=tk.CENTER)

        self.treeUsers.heading("id", text="id")
        self.treeUsers.heading("firstname", text='Імя')
        self.treeUsers.heading("secondname", text='Прізвище')
        self.treeUsers.heading("adress", text='Адреса')
        self.treeUsers.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(self, command=self.treeComp.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeComp.configure(yscrollcommand=scrollbar.set)


class WindowInputDialogComp(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_input()
        self.db = db
        self.view = app

    def init_input(self):
        self.title = "Додати товар"
        self.geometry("400x200+170+170")
        self.resizable(False, False)

        label_name = tk.Label(self, text="Назва товару")
        label_name.place(x=20, y=20)
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x=120, y=20)

        label_count = tk.Label(self, text="Кількість")
        label_count.place(x=20, y=60)
        self.entry_count = tk.Entry(self)
        self.entry_count.place(x=120, y=60)

        label_price = tk.Label(self, text="Вартість")
        label_price.place(x=20, y=100)
        self.entry_price = tk.Entry(self)
        self.entry_price.place(x=120, y=100)

        btn_cancel = ttk.Button(self, text="Відмінити", command=self.destroy)
        btn_cancel.place(x=100, y=140)

        def add_date(event):
            self.view.records_computers(self.entry_name.get(),
                                        self.entry_count.get(),
                                        self.entry_price.get())
            self.entry_name.delete(0, 'end')
            self.entry_count.delete(0, 'end')
            self.entry_price.delete(0, 'end')

        btn_add = ttk.Button(self, text="Додати")
        btn_add.place(x=250, y=140)
        btn_add.bind("<Button-1>", add_date)


class WindowEditDialogComp(WindowInputDialogComp):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.veiw = app
        self.indexItem=self.view.treeComp.set(self.view.treeComp.selection()[0], column='#1')
        self.default_value()

    def init_edit(self):
        self.title = "Редагування"
        btn_edit = ttk.Button(self, text="Редагувати")
        btn_edit.place(x=250, y=140)
        btn_edit.bind("<Button-1>", lambda event:self.view.update_computers(self.entry_name.get(),
                                        self.entry_count.get(),
                                        self.entry_price.get(),
                                        self.indexItem))

    def default_value(self):
        print(self.view.treeComp.set(self.view.treeComp.selection()[0], column='#1'))
        self.db.curs.execute("""SELECT * FROM computers WHERE id=?""",(self.indexItem,))
        result = self.db.curs.fetchone()
        print(result)
        self.entry_name.insert(0, result[1])
        self.entry_count.insert(0, result[2])
        self.entry_price.insert(0, result[3])


class DB():
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

        self.curs.execute("""CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INT NOT NULL,
            computers_id INT NOT NULL,
            date_order DATETIME DEFAULT CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (computers_id) REFERENCES computers (id) )""")
        self.conn.commit()
        # self.curs.close()
        # self.conn.close()

    #CRUD operation with table 'computers'
    def selectAllComputers(self):
        self.curs.execute("""SELECT * FROM computers""")
        return self.curs.fetchall()

    def input_data_computers(self, name, count, price):
        self.curs.execute("""INSERT INTO computers (name, count, price) VALUES(?, ?, ?)""",
                          (name, count, price))
        self.conn.commit()

    def update_data_computers(self,name,count,price,id):
        self.curs.execute("""UPDATE computers SET name=?, count=?, price=? WHERE id=?""",
                             (name, count, price,id))
        self.conn.commit()

    def delete_data_computers(self, id):
        self.curs.execute("""DELETE FROM computers WHERE id=?""",(id,))
        self.conn.commit()

    #CRUD operation with table 'users'
    def selectAllUsers(self):
        self.curs.execute("""SELECT * FROM users""")
        return self.curs.fetchall()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Магазин компютерної техніки")
    root.geometry("650x450")
    root.resizable(False, False)
    root.mainloop()
