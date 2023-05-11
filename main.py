import sqlite3
from tkinter import *
from tkinter.ttk import *
from sqlite3 import *

current_user = ""


def check_database():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table'")

    tables = c.fetchall()

    for table in tables:
        print(table[0])

    conn.close()


def create_users_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
            );
    """)

    conn.commit()
    conn.close()


def drop_users_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
            DROP TABLE users
        """)

    conn.commit()
    conn.close()


def create_user_table(user_name):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    query = f"CREATE TABLE {user_name} (" \
            f"id INTEGER PRIMARY KEY AUTOINCREMENT," \
            f"transactionSite TEXT" \
            f"transactionType INTEGER" \
            f"outcome INTEGER" \
            f"cost NUMERIC" \
            f"payout NUMERIC);" \

    c.execute(query)

    conn.commit()
    conn.close()


def login_screen():

    main_window = Tk()
    main_window.title("Login")

    login_frame = Frame(main_window)
    login_frame.pack(padx=10, pady=10)

    user_label = Label(login_frame, text="Username:")
    user_label.pack()
    user_field = Entry(login_frame)
    user_field.pack()
    password_label = Label(login_frame, text="Password:")
    password_label.pack()
    password_field = Entry(login_frame)
    password_field.pack(pady=(0, 10))

    def main_screen():

        current_user_label = Label(main_window, text=current_user)
        current_user_label.pack()

        entry_table = Treeview(main_window)
        entry_table["columns"] = ("column1", "column2", "column3", "column4", "column5")

        # format the columns
        entry_table.column("#0", width=0, stretch=NO)
        entry_table.column("column1", width=100)
        entry_table.column("column2", width=100)
        entry_table.column("column3", width=100)
        entry_table.column("column4", width=100)
        entry_table.column("column5", width=100)

        # add column headings
        entry_table.heading("column1", text="Transaction Type")
        entry_table.heading("column2", text="Site")
        entry_table.heading("column3", text="Amount/Wager")
        entry_table.heading("column4", text="Payout")
        entry_table.heading("column5", text="Win?")

        # add data to the table
        entry_table.insert("", END, text="Row 1", values=("Deposit", "Prize Picks", "20", "", ""))
        entry_table.insert("", END, text="Row 1", values=("Entry", "Prize Picks", "10", "250", "Yes"))
        entry_table.insert("", END, text="Row 1", values=("Entry", "Prize Picks", "10", "50", "No"))
        entry_table.insert("", END, text="Row 1", values=("Withdrawal", "Prize Picks", "260", "", ""))

        # pack the treeview widget
        entry_table.pack()

        create_entry_button = Button(main_window, text="Add Entry", command=add_entry)
        create_entry_button.pack(pady=10)

    def login():
        username = user_field.get()
        password = password_field.get()

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        c.execute("""
            SELECT * FROM users WHERE username=? AND password=?;
        """, (username, password))
        existing_user = c.fetchone()

        conn.close()

        if existing_user is not None:
            main_window.title("Bet Tracker")
            login_frame.destroy()
            global current_user
            current_user = username
            print("Successful Login!")
            main_screen()
            
    login_button = Button(login_frame, text="Login", command=login)
    login_button.pack(pady=(0, 10))

    register_button = Button(login_frame, text="Make New Account", command=register_screen)
    register_button.pack(pady=(0, 10))

    def check_tables():
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        c.execute("SELECT * FROM users")
        users = c.fetchall()

        for user in users:
            print(user)

        conn.close()
        check_database()

    check_button = Button(login_frame, text="Check Tables", command=check_tables)
    check_button.pack(pady=(0, 10))

    login_frame.pack(expand=True, fill='both', padx=50, pady=50)

    main_window.mainloop()


def register_screen():
    register_window = Tk()
    register_window.geometry("300x250")
    register_window.title("Login")

    user_label = Label(register_window, text="Create Username:")
    user_label.pack()
    user_field = Entry(register_window)
    user_field.pack()
    password_label = Label(register_window, text="Create Password:")
    password_label.pack()
    password_field = Entry(register_window)
    password_field.pack()

    def register():
        username = user_field.get()
        password = password_field.get()

        conn = sqlite3.connect("users.db")

        c = conn.cursor()

        c.execute("""
            INSERT INTO users (username, password) VALUES (?,?);
        """, (username, password))

        conn.commit()
        conn.close()

        create_user_table(username)
        check_database()
        print("Registration Successful!")

    register_button = Button(register_window, text="Register", command=register)
    register_button.pack(pady=10)

    register_window.mainloop()


def add_entry():
    entry_window = Tk()
    entry_window.geometry("300x250")
    entry_window.title("Login")

    user_label = Label(entry_window, text="Create Username:")
    user_label.pack()
    user_field = Entry(entry_window)
    user_field.pack()
    password_label = Label(entry_window, text="Create Password:")
    password_label.pack()
    password_field = Entry(entry_window)
    password_field.pack()

    def add():

        site = "Prize Picks"
        transaction_type = 0
        outcome = 0
        cost = 20.00
        payout = 100.00

        conn = sqlite3.connect("users.db")

        c = conn.cursor()

        c.execute("""
                INSERT INTO username (transactionSite, transactionType, outcome, cost, payout) VALUES (?,?,?,?,?);
            """, (site, transaction_type, outcome, cost, payout))

        conn.commit()
        conn.close()

        check_database()
        print("Add Entry Successful!")

    register_button = Button(entry_window, text="Register", command=add)
    register_button.pack(pady=10)

    entry_window.mainloop()


login_screen()

