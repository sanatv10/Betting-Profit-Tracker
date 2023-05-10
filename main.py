import sqlite3
from tkinter import *
from tkinter import ttk
from sqlite3 import *


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


def main_screen():

    main_window = Tk()
    main_window.title("Login")

    login_frame = Frame(main_window, padx=50, pady=50)
    login_frame.pack(padx=10, pady=10)

    user_label = Label(login_frame, text="Username:")
    user_label.pack()
    user_field = Entry(login_frame)
    user_field.pack()
    password_label = Label(login_frame, text="Password:")
    password_label.pack()
    password_field = Entry(login_frame)
    password_field.pack(pady=(0, 10))

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
            print("Successful Login!")

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

    login_frame.pack(expand=True, fill='both', padx=10, pady=10)

    main_frame = Frame(main_window)

    # Hide main frame initially
    main_frame.grid_remove()

    # Start with the login frame
    login_frame.grid()

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


main_screen()
