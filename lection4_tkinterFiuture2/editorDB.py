import tkinter as tk
# import tkinter.ttk as ttk
# або так:
from tkinter import ttk
import tkinter.messagebox as dialogWin
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.toolbar_disable()
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
        mainbar.add_cascade(label="Таблиця Order", command=self.view_records_orders)
        mainbar.add_cascade(label="Exit", command=self.quit)
        root.config(menu=mainbar)

        self.toolbar = tk.Frame(bg='gray', bd=8)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # button add
        self.add_img = tk.PhotoImage(file="image_btn/add.png")
        add_button = tk.Button(self.toolbar, text="Додати", background="gray",
                               command=self.open_add_dialog, image=self.add_img, compound=tk.TOP)
        add_button.pack(side=tk.LEFT)
        # button edit
        self.edit_img = tk.PhotoImage(file="image_btn/edit.png")
        edit_button = tk.Button(self.toolbar, text="Редагувати", background="gray",
                                command=self.open_edit_dialog, image=self.edit_img,compound=tk.TOP)
        edit_button.pack(side=tk.LEFT)

        # button delete
        self.delete_img = tk.PhotoImage(file="image_btn/delete.png")
        delete_button = tk.Button(self.toolbar, text="Видалити", background="gray",
                                  command=self.delete_records, image=self.delete_img,compound=tk.TOP)
        delete_button.pack(side=tk.LEFT)

        # button close current table
        self.closetab_img = tk.PhotoImage(file="image_btn/close.png")
        self.closetab_button = tk.Button(self.toolbar, text="Закрити вкладку", background="gray",
                                         command=self.closeCurrentTabNotebook, image=self.closetab_img, compound=tk.TOP)
        self.closetab_button.pack(side=tk.LEFT)

        # button info
        self.info_img = tk.PhotoImage(file="image_btn/info_order.png")
        info_button = tk.Button(self.toolbar, text="Інформація order", background="gray",
                                  command=self.view_full_info_order, image=self.info_img,compound=tk.TOP)
        info_button.pack(side=tk.LEFT)

    # using Notebook
    # ---------------------------------
    def createNotebook(self):
        self.myNotebook = ttk.Notebook(self)
        self.myNotebook.pack(padx=10, fill=tk.BOTH)
        #добавимо подію, коли переходитимо між вкладками, то щоб оновлювалися   дані в таблицях, особливо,
        # якщо відбулося каскадне видалення
        self.myNotebook.bind("<<NotebookTabChanged>>", self.refreshCurrentTabNotebook)
        self.frameComputers = tk.Frame(self.myNotebook, width=640, height=300)
        self.frameUsers = tk.Frame(self.myNotebook, width=640, height=300)
        self.frameOrders = tk.Frame(self.myNotebook, width=640, height=300)
        self.treeComp = ttk.Treeview(self.frameComputers, columns=('id', "name", "count", "price"), height=15,
                                     show="headings")
        self.treeUsers = ttk.Treeview(self.frameUsers, columns=('id', "firstname", "secondname", "adress"), height=15,
                                      show="headings")
        self.treeOrders = ttk.Treeview(self.frameOrders, columns=('id', "user_id", "computers_id", "date_order"), height=15,
                                      show="headings")
        self.table_computers()
        self.table_users()
        self.table_orders()

    def addNotebookComputers(self):
        self.toolbar_able()
        self.myNotebook.add(self.frameComputers, text="Computers")
        # зробити активною (видимою, вибраною) вкладку із фреймом, що відображає таблицю Computers
        self.myNotebook.select(self.myNotebook.index(self.frameComputers))

    def addNotebookUsers(self):
        self.toolbar_able()
        self.myNotebook.add(self.frameUsers, text="Users")
        # зробити активною (видимою, вибраною) вкладку із фреймом, що відображає таблицю Users
        self.myNotebook.select(self.myNotebook.index(self.frameUsers))
        # print(self.myNotebook.tabs().index(self.myNotebook.select()))

    def addNotebookOrders(self):
        self.toolbar_able()
        self.myNotebook.add(self.frameOrders, text="Orders")
        # зробити активною (видимою, вибраною) вкладку із фреймом, що відображає таблицю Users
        self.myNotebook.select(self.myNotebook.index(self.frameOrders))
        # print(self.myNotebook.tabs().index(self.myNotebook.select()))

    def closeCurrentTabNotebook(self):
        # визначення номера активної вкладки
        currentTab = self.myNotebook.tabs().index(self.myNotebook.select())
        # print(currentTab)
        if currentTab > 0:
            print(self.myNotebook.tab(currentTab))
            self.myNotebook.forget(currentTab)
        elif currentTab == 0:
            self.toolbar_disable()
            self.myNotebook.forget(currentTab)

    def refreshCurrentTabNotebook(self,event):
        if len(self.myNotebook.tabs())!=0:
            # визначення номера активної вкладки
            currentTab = self.myNotebook.tabs().index(self.myNotebook.select())
            # в залежності від вибрано вкладки виконувати викли діалогового вікна
            if self.myNotebook.tab(currentTab)["text"] == "Computers":
                self.view_records_computers()
            elif self.myNotebook.tab(currentTab)["text"] == "Users":
                self.view_records_users()
            elif self.myNotebook.tab(currentTab)["text"] == "Orders":
                self.view_records_orders()

    # зробити кнопки в toolbar не активними - кнопки не доступні
    def toolbar_disable(self):
        for btn in self.toolbar.children.values():
            btn['state'] = "disable"

    # зробити кнопки в toolbar активними - кнопки доступні
    def toolbar_able(self):
        for btn in self.toolbar.children.values():
            btn['state'] = "active"

    # function for open dialog
    # ---------------------------------------------------------------
    def open_add_dialog(self):
        # визначення номера активної вкладки
        currentTab = self.myNotebook.tabs().index(self.myNotebook.select())
        # в залежності від вибрано вкладки виконувати викли діалогового вікна
        if self.myNotebook.tab(currentTab)["text"] == "Computers":
            WindowInputDialogComp()
        elif self.myNotebook.tab(currentTab)["text"] == "Users":
            WindowInputDialogUser()
        elif self.myNotebook.tab(currentTab)["text"] == "Orders":
            WindowInputDialogOrder()

        # print(self.myNotebook.tabs().index(self.myNotebook.select()))
        # print(self.myNotebook.tabs())
        # print(self.myNotebook.tab(0))
        # print(self.myNotebook.tab(1))
        # print(self.myNotebook.tab(0).values())
        # print(self.myNotebook.tab(1).items())

    def open_edit_dialog(self):
        # визначення номера активної вкладки
        currentTab = self.myNotebook.tabs().index(self.myNotebook.select())
        # print(len(self.treeUsers.selection()))
        # в залежності від вибрано вкладки виконувати викли діалогового вікна
        if self.myNotebook.tab(currentTab)["text"] == "Computers":
            if len(self.treeComp.selection()) != 0:
                WindowEditDialogComp()
            else:
                dialogWin.showwarning("Повідомлення", "Не вибрано жодного запису!")
        elif self.myNotebook.tab(currentTab)["text"] == "Users":
            if len(self.treeUsers.selection()) != 0:
                WindowEditDialogUser()
            else:
                dialogWin.showwarning("Повідомлення", "Не вибраного жоного запису!")
        elif self.myNotebook.tab(currentTab)["text"] == "Orders":
            if len(self.treeOrders.selection()) != 0:
                WindowEditDialogOrder()
            else:
                dialogWin.showwarning("Повідомлення", "Не вибраного жоного запису!")


    def delete_records(self):
        # визначення номера активної вкладки
        currentTab = self.myNotebook.tabs().index(self.myNotebook.select())
        # в залежності від вибрано вкладки виконувати викли діалогового вікна
        if self.myNotebook.tab(currentTab)["text"] == "Computers":
            if len(self.treeComp.selection()) != 0:
                self.delete_records_computers()
            else:
                dialogWin.showwarning("Повідомлення", "Не вибрано жодного запису!")
        elif self.myNotebook.tab(currentTab)["text"] == "Users":
            if len(self.treeUsers.selection()) != 0:
                self.delete_records_users()
            else:
                dialogWin.showwarning("Повідомлення", "Не вибраного жоного запису!")
        elif self.myNotebook.tab(currentTab)["text"] == "Orders":
            if len(self.treeOrders.selection()) != 0:
                self.delete_records_orders()
            else:
                dialogWin.showwarning("Повідомлення", "Не вибраного жоного запису!")



    # function CRUD operations with table "computers "
    def view_records_computers(self):
        data = self.db.selectAllComputers()
        # self.table_computers()
        self.addNotebookComputers()
        for i in self.treeComp.get_children():
            self.treeComp.delete(i)
        for row in data:
            self.treeComp.insert('', 'end', values=row)

    def records_computers(self, name, count, price):
        self.db.input_data_computers(name, count, price)
        self.view_records_computers()

    def update_computers(self, name, count, price, id):
        self.db.update_data_computers(name, count, price, id)
        self.view_records_computers()

    def delete_records_computers(self):
        for selected_record in self.treeComp.selection():
            self.db.delete_data_computers(self.treeComp.set(selected_record, '#1'))
        self.view_records_computers()

    # CRUD operation for users table
    def view_records_users(self):
        data = self.db.selectAllUsers()
        for i in self.treeUsers.get_children():
            self.treeUsers.delete(i)

        self.addNotebookUsers()
        # self.table_users()
        for row in data:
            self.treeUsers.insert('', 'end', values=row)

    def records_users(self, firstname, secondname, adress):
        self.db.input_data_users(firstname, secondname, adress)
        self.view_records_users()

    def update_users(self, firstname, secondname, adress, id):
        self.db.update_data_users(firstname, secondname, adress, id)
        self.view_records_users()

    def delete_records_users(self):
        for selected_record in self.treeUsers.selection():
            self.db.delete_data_users(self.treeUsers.set(selected_record, '#1'))
        self.view_records_users()

        # function CRUD operations with table "orders"

    def view_records_orders(self):
        data = self.db.selectAllOrders()
        self.addNotebookOrders()
        for i in self.treeOrders.get_children():
            self.treeOrders.delete(i)
        for row in data:
            self.treeOrders.insert('', 'end', values=row)

    def records_orders(self, user_id, computers_id):
        self.db.input_data_orders(user_id, computers_id)
        self.view_records_orders()

    def update_order(self, user_id, computers_id,date_order, id):
        self.db.update_data_orders(user_id, computers_id, date_order, id)
        self.view_records_orders()

    def delete_records_orders(self):
        for selected_record in self.treeOrders.selection():
            self.db.delete_data_orders(self.treeOrders.set(selected_record, '#1'))
        self.view_records_orders()


    def view_full_info_order(self):
        if len(self.treeOrders.selection())!=0:
            for selected_record in self.treeOrders.selection():
                data=self.db.full_info_order(self.treeOrders.set(selected_record, '#1'))
                info=" Дата замовлення: {}\n Прізвище замовника: {}\n" \
                     " Назва товару: {}\n Ціна товару: {} ".format(data[1],data[2],data[3],data[4])
                # print(data)
                dialogWin.showinfo("Order"+str(data[0]), info)
        else:
            dialogWin.showwarning("Повідомлення", "Не вибрано жодного запису в таблиці Orders!")


    # create table TeeView for Computers
    def table_computers(self):
        self.treeComp.column("id", width=50, anchor=tk.CENTER)
        self.treeComp.column("name", width=260, anchor=tk.CENTER)
        self.treeComp.column("count", width=100, anchor=tk.CENTER)
        self.treeComp.column("price", width=100, anchor=tk.CENTER)

        self.treeComp.heading("id", text="id")
        self.treeComp.heading("name", text='Наіменування товару')
        self.treeComp.heading("count", text='Кількість')
        self.treeComp.heading("price", text='Ціна')
        self.treeComp.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(self.frameComputers, command=self.treeComp.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeComp.configure(yscrollcommand=scrollbar.set)

    # create table TeeView for Users
    def table_users(self):
        self.treeUsers.column("id", width=50, anchor=tk.CENTER)
        self.treeUsers.column("firstname", width=260, anchor=tk.CENTER)
        self.treeUsers.column("secondname", width=100, anchor=tk.CENTER)
        self.treeUsers.column("adress", width=100, anchor=tk.CENTER)

        self.treeUsers.heading("id", text="id")
        self.treeUsers.heading("firstname", text='Імя')
        self.treeUsers.heading("secondname", text='Прізвище')
        self.treeUsers.heading("adress", text='Адреса')
        self.treeUsers.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(self.frameUsers, command=self.treeUsers.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeComp.configure(yscrollcommand=scrollbar.set)

    # create table TeeView for Users
    def table_orders(self):
        self.treeOrders.column("id", width=50, anchor=tk.CENTER)
        self.treeOrders.column("user_id", width=260, anchor=tk.CENTER)
        self.treeOrders.column("computers_id", width=100, anchor=tk.CENTER)
        self.treeOrders.column("date_order", width=100, anchor=tk.CENTER)

        self.treeOrders.heading("id", text="id")
        self.treeOrders.heading("user_id", text='user_id')
        self.treeOrders.heading("computers_id", text='computers_id')
        self.treeOrders.heading("date_order", text='date_order')
        self.treeOrders.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(self.frameOrders, command=self.treeOrders.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeOrders.configure(yscrollcommand=scrollbar.set)


#DIALOG
# dialogwindows for computers
#-------------------------------------------------------------------------------------------------------
class WindowInputDialogComp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_input()
        self.db = db
        self.view = app

    def init_input(self):
        self.title("Додати товар")
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
        # для того, щоб дія відбувалася, як під час події натиснення на кнопку лівою клавішею миші,
        # так і при натисненні на клавішу Enter клавіатури, можна метод bind застосувати кілька
        # разів до одного і того ж віджета - в даному випадку кнопки
        btn_add.bind("<Button-1>", add_date)
        btn_add.bind("<Return>", add_date)

        self.grab_set()
        self.focus_set()

class WindowEditDialogComp(WindowInputDialogComp):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.veiw = app
        self.indexItem = self.view.treeComp.set(self.view.treeComp.selection()[0], column='#1')
        self.default_value()

    def init_edit(self):
        # self.title = "Редагування" - це не вірний синтаксис
        self.title("Редагування")
        btn_edit = ttk.Button(self, text="Редагувати")
        btn_edit.place(x=250, y=140)
        btn_edit.bind("<Button-1>", lambda event: self.view.update_computers(self.entry_name.get(),
                                                                             self.entry_count.get(),
                                                                             self.entry_price.get(),
                                                                             self.indexItem))
        btn_edit.bind("<Enter>", lambda event: self.view.update_computers(self.entry_name.get(),
                                                                             self.entry_count.get(),
                                                                             self.entry_price.get(),
                                                                             self.indexItem))
        self.grab_set()
        self.focus_set()

    def default_value(self):
        # print(self.view.treeComp.set(self.view.treeComp.selection()[0], column='#1'))
        self.db.curs.execute("""SELECT * FROM computers WHERE id=?""", (self.indexItem,))
        result = self.db.curs.fetchone()
        self.entry_name.insert(0, result[1])
        self.entry_count.insert(0, result[2])
        self.entry_price.insert(0, result[3])


# dialogwindows for users
class WindowInputDialogUser(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_input()
        self.db = db
        self.view = app

    def init_input(self):
        self.title("Додати нового корситувача")
        self.geometry("400x200+170+170")
        self.resizable(False, False)

        label_firstname = tk.Label(self, text="Імя")
        label_firstname.place(x=20, y=20)
        self.entry_firstname = tk.Entry(self)
        self.entry_firstname.place(x=120, y=20)

        label_secondname = tk.Label(self, text="Прізвище")
        label_secondname.place(x=20, y=60)
        self.entry_secondname = tk.Entry(self)
        self.entry_secondname.place(x=120, y=60)

        label_adress = tk.Label(self, text="Адреса")
        label_adress.place(x=20, y=100)
        self.entry_adress = tk.Entry(self)
        self.entry_adress.place(x=120, y=100)

        btn_cancel = ttk.Button(self, text="Відмінити", command=self.destroy)
        btn_cancel.place(x=100, y=140)
        self.grab_set()
        self.focus_set()

        def add_date(event):
            self.view.records_users(self.entry_firstname.get(),
                                    self.entry_secondname.get(),
                                    self.entry_adress.get())
            self.entry_firstname.delete(0, 'end')
            self.entry_secondname.delete(0, 'end')
            self.entry_adress.delete(0, 'end')

        btn_add = ttk.Button(self, text="Додати")
        btn_add.place(x=250, y=140)
        btn_add.bind("<Button-1>", add_date)
        btn_add.bind("<Return>", add_date)


class WindowEditDialogUser(WindowInputDialogUser):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.veiw = app
        self.indexItem = self.view.treeUsers.set(self.view.treeUsers.selection()[0], column='#1')
        self.default_value()

    def init_edit(self):
        self.title("Редагування")
        btn_edit = ttk.Button(self, text="Редагувати")
        btn_edit.place(x=250, y=140)
        btn_edit.bind("<Button-1>", lambda event: self.view.update_users(self.entry_firstname.get(),
                                                                         self.entry_secondname.get(),
                                                                         self.entry_adress.get(),
                                                                         self.indexItem))
        btn_edit.bind("<Return>", lambda event: self.view.update_users(self.entry_firstname.get(),
                                                                         self.entry_secondname.get(),
                                                                         self.entry_adress.get(),
                                                                         self.indexItem))
        self.grab_set()
        self.focus_set()


    def default_value(self):
        # print(self.indexItem)
        self.db.curs.execute("""SELECT * FROM users WHERE id=?""", (self.indexItem,))
        result = self.db.curs.fetchone()
        # print(result)
        self.entry_firstname.insert(0, result[1])
        self.entry_secondname.insert(0, result[2])
        self.entry_adress.insert(0, result[3])

# # dialogwindows for users
# class WindowInputDialogUser(tk.Toplevel):
#     def __init__(self):
#         super().__init__()
#         self.init_input()
#         self.db = db
#         self.view = app
#
#     def init_input(self):
#         self.title("Додати нового замовника")
#         self.geometry("400x200+170+170")
#         self.resizable(False, False)
#
#         label_firstname = tk.Label(self, text="Імя")
#         label_firstname.place(x=20, y=20)
#         self.entry_firstname = tk.Entry(self)
#         self.entry_firstname.place(x=120, y=20)
#
#         label_secondname = tk.Label(self, text="Прізвище")
#         label_secondname.place(x=20, y=60)
#         self.entry_secondname = tk.Entry(self)
#         self.entry_secondname.place(x=120, y=60)
#
#         label_adress = tk.Label(self, text="Адреса")
#         label_adress.place(x=20, y=100)
#         self.entry_adress = tk.Entry(self)
#         self.entry_adress.place(x=120, y=100)
#
#         btn_cancel = ttk.Button(self, text="Відмінити", command=self.destroy)
#         btn_cancel.place(x=100, y=140)
#
#         def add_date(event):
#             self.view.records_users(self.entry_firstname.get(),
#                                     self.entry_secondname.get(),
#                                     self.entry_adress.get())
#             self.entry_firstname.delete(0, 'end')
#             self.entry_secondname.delete(0, 'end')
#             self.entry_adress.delete(0, 'end')
#
#         btn_add = ttk.Button(self, text="Додати")
#         btn_add.place(x=250, y=140)
#         btn_add.bind("<Button-1>", add_date)
#         btn_add.bind("<Return>", add_date)
#
#         self.grab_set()
#         self.focus_set()

# dialogwindows for orders
class WindowInputDialogOrder(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_input()
        self.db = db
        self.view = app

    def init_input(self):
        self.title("Додати нове замовлення")
        self.geometry("400x200+170+170")
        self.resizable(False, False)

        label_user_id = tk.Label(self, text="user_id")
        label_user_id.place(x=20, y=20)
        self.entry_user_id = tk.Entry(self)
        self.entry_user_id.place(x=120, y=20)

        label_computers_id = tk.Label(self, text="computers_id")
        label_computers_id.place(x=20, y=60)
        self.entry_computers_id = tk.Entry(self)
        self.entry_computers_id.place(x=120, y=60)

        btn_cancel = ttk.Button(self, text="Відмінити", command=self.destroy)
        btn_cancel.place(x=100, y=140)
        #функція для обробки події кнопки
        def add_date(event):
            self.view.records_orders(self.entry_user_id.get(),
                                   self.entry_computers_id.get())
            self.entry_user_id.delete(0, 'end')
            self.entry_computers_id.delete(0, 'end')

        btn_add = ttk.Button(self, text="Додати")
        btn_add.place(x=250, y=140)
        btn_add.bind("<Button-1>", add_date)
        btn_add.bind("<Return>", add_date)

        self.grab_set()
        self.focus_set()

class WindowEditDialogOrder(WindowInputDialogOrder):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.indexItem = self.view.treeOrders.set(self.view.treeOrders.selection()[0], column='#1')
        self.default_value()

    def init_edit(self):
        self.title("Редагування")
        label_date_order = tk.Label(self, text="date_order")
        label_date_order.place(x=20, y=100)
        self.entry_date_order = tk.Entry(self)
        self.entry_date_order.place(x=120, y=100)

        btn_edit = ttk.Button(self, text="Редагувати")
        btn_edit.place(x=250, y=140)
        btn_edit.bind("<Button-1>", lambda event: self.view.update_order(self.entry_user_id.get(),
                                                                         self.entry_computers_id.get(),
                                                                         self.entry_date_order.get(),
                                                                         self.indexItem))
        btn_edit.bind("<Return>", lambda event: self.view.update_order(self.entry_user_id.get(),
                                                                         self.entry_computers_id.get(),
                                                                         self.entry_date_order.get(),
                                                                         self.indexItem))
        self.grab_set()
        self.focus_set()


    def default_value(self):
        # print(self.indexItem)
        self.db.curs.execute("""SELECT * FROM orders WHERE id=?""", (self.indexItem,))
        result = self.db.curs.fetchone()
        self.entry_user_id.insert(0, result[1])
        self.entry_computers_id.insert(0, result[2])
        self.entry_date_order.insert(0, result[3])


#DATA BASE
#------------------------------------------------------------------------------------------------
class DB():
    def __init__(self):
        self.conn = sqlite3.connect('ishop.db')  # connection
        self.curs = self.conn.cursor()
        #відкриваємо дозвіл на  каскадне видалення з декількох таблиць
        self.curs.execute("PRAGMA foreign_keys=ON")

        self.curs.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname VARCHAR(20) NOT NULL,
            secondname VARCHAR(20) NOT NULL ,
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
            date_order DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users (id) ON  DELETE CASCADE,
            FOREIGN KEY (computers_id) REFERENCES computers (id) ON  DELETE CASCADE)""")
        self.conn.commit()

    # перестрахуємо себе і,коли програма закриється, то закриємо зєднання з базою даних
    def __del__(self):
        self.curs.close()
        self.conn.close()

    # CRUD operation with table 'computers'
    def selectAllComputers(self):
        self.curs.execute("""SELECT * FROM computers""")
        return self.curs.fetchall()

    def input_data_computers(self, name, count, price):
        self.curs.execute("""INSERT INTO computers (name, count, price) VALUES(?, ?, ?)""",
                          (name, count, price))
        self.conn.commit()

    def update_data_computers(self, name, count, price, id):
        self.curs.execute("""UPDATE computers SET name=?, count=?, price=? WHERE id=?""",
                          (name, count, price, id))
        self.conn.commit()

    def delete_data_computers(self, id):
        self.curs.execute("""DELETE FROM computers WHERE id=?""", (id,))
        self.conn.commit()

    # CRUD operation with table 'users'
    def selectAllUsers(self):
        self.curs.execute("""SELECT * FROM users""")
        return self.curs.fetchall()

    def input_data_users(self, firstname, secondname, adress):
        self.curs.execute("""INSERT INTO users (firstname, secondname, adress) VALUES(?, ?, ?)""",
                          (firstname, secondname, adress))
        self.conn.commit()

    def update_data_users(self, firstname, secondname, adress, id):
        self.curs.execute("""UPDATE users SET firstname=?, secondname=?, adress=? WHERE id=?""",
                          (firstname, secondname, adress, id))
        self.conn.commit()

    def delete_data_users(self, id):
        self.curs.execute("""DELETE FROM users WHERE id=?""", (id,))
        self.conn.commit()

    # CRUD operation with table 'users'
    def selectAllOrders(self):
        self.curs.execute("""SELECT * FROM orders""")
        return self.curs.fetchall()

    def input_data_orders(self, user_id, computers_id):
        self.curs.execute("""INSERT INTO orders (user_id, computers_id) VALUES(?, ?)""",
                          (user_id, computers_id))
        self.conn.commit()

    def update_data_orders(self, user_id, computers_id, date_order,id):
        self.curs.execute("""UPDATE orders SET user_id=?, computers_id=?, date_order=? WHERE id=?""",
                          (user_id, computers_id, date_order,id))
        self.conn.commit()

    def delete_data_orders(self, id):
        self.curs.execute("""DELETE FROM orders WHERE id=?""", (id,))

    def full_info_order(self,id):
        self.curs.execute('''SELECT  orders.id, orders.date_order, users.secondname, computers.name,computers.price 
                            FROM  orders
                            JOIN users ON users.id=orders.user_id 
                            JOIN computers ON computers.id=orders.computers_id 
                            WHERE orders.id=?;''',(id,))
        return self.curs.fetchone()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Магазин компютерної техніки")
    root.geometry("650x450")
    root.resizable(False, False)
    root.mainloop()