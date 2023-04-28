import sqlite3
from tkinter import *
from tkinter import ttk
from sqlite3 import *


def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
            );
    """)

    conn.commit()
    conn.close()


def login_screen():
    login_window = Tk()
    login_window.geometry("300x250")
    login_window.title("Login")

    user_label = Label(login_window, text="Username:")
    user_label.pack()
    user_field = Entry(login_window)
    user_field.pack()
    password_label = Label(login_window, text="Password:")
    password_label.pack()
    password_field = Entry(login_window)
    password_field.pack()

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
            print("Successful login")

    login_button = Button(login_window, text="Login", command=login)
    login_button.pack(pady=10)

    register_button = Button(login_window, text="Make New Account", command=register_screen)
    register_button.pack()

    def check_tables():
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        c.execute("SELECT * FROM users")
        users = c.fetchall()

        for user in users:
            print(user)

        conn.close()

    check_button = Button(login_window, text="Check Tables", command=check_tables)
    check_button.pack(pady=10)

    login_window.mainloop()


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

    register_button = Button(register_window, text="Register", command=register)
    register_button.pack(pady=10)

    register_window.mainloop()


login_screen()
