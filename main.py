from tkinter import *
from tkinter import ttk


def login_window():
    window = Tk()
    window.geometry("300x250")
    window.title("Login")

    user_label = Label(window, text="Username:")
    user_label.pack()
    user_field = Entry(window)
    user_field.pack()
    password_label = Label(window, text="Username:")
    password_label.pack()
    password_field = Entry(window)
    password_field.pack()

    login_button = Button(window, text="Login", command=login)
    login_button.pack(pady=10)

    register_button = Button(window, text="Register", command=register)
    register_button.pack()

    window.mainloop()


def login():
    print("login success")


def register():
    print("Continue to registration")


login_window()
