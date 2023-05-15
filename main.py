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
            f"transactionType INTEGER," \
            f"transactionSite TEXT," \
            f"cost NUMERIC," \
            f"payout NUMERIC," \
            f"outcome INTEGER);" \

    c.execute(query)

    conn.commit()
    conn.close()


def main_screen():
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

    def main_frame():

        current_user_label = Label(main_window, text=current_user)
        current_user_label.pack()

        def display_table_data():
            # Clear existing rows
            entry_table.delete(*entry_table.get_children())

            # Fetch the rows from the table
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            # Populate the Treeview with the table data
            for row in rows:
                entry_table.insert('', 'end', values=row)

            # Close the connection
            conn.close()

        entry_table = Treeview(main_window, columns=("column1", "column2", "column3", "column4", "column5", "column6"))

        # format the columns
        entry_table.column("#0", width=0, stretch=NO)
        entry_table.column("column1", width=100)
        entry_table.column("column2", width=100)
        entry_table.column("column3", width=100)
        entry_table.column("column4", width=100)
        entry_table.column("column5", width=100)
        entry_table.column("column6", width=100)

        # add column headings
        entry_table.heading("column1", text="ID")
        entry_table.heading("column2", text="Transaction Type")
        entry_table.heading("column3", text="Site")
        entry_table.heading("column4", text="Amount/Wager")
        entry_table.heading("column5", text="Payout")
        entry_table.heading("column6", text="Win?")

        # pack the treeview widget
        entry_table.pack()

        # Set the table name
        table_name = current_user

        # Display the table data
        display_table_data()

        entry_frame = Frame(main_window)
        entry_frame.pack(side=RIGHT, padx=10, pady=10)

        site_label = Label(entry_frame, text="Site Used:")
        site_label.pack()
        site_field = Entry(entry_frame)
        site_field.pack()

        transaction_label = Label(entry_frame, text="Transaction Type:")
        transaction_label.pack()

        def radio_select():
            if radio.get() == 1:
                to_win_field.config(state="disabled")
                win_checkbutton.config(state="disabled")
                to_win_field.delete(0, END)
                print("1")
            elif radio.get() == 2:
                to_win_field.config(state="disabled")
                win_checkbutton.config(state="disabled")
                to_win_field.delete(0, END)
                print("2")
            elif radio.get() == 3:
                to_win_field.config(state="normal")
                win_checkbutton.config(state="normal")
                print("3")

        radio = IntVar()
        radio_button_frame = Frame(entry_frame)
        radio_button_frame.pack()
        radio_button_deposit = Radiobutton(radio_button_frame, text="Deposit", variable=radio, value=1,
                                           command=radio_select)
        radio_button_deposit.pack(side="left")
        radio_button_withdrawal = Radiobutton(radio_button_frame, text="Withdrawal", variable=radio, value=2,
                                              command=radio_select)
        radio_button_withdrawal.pack(side="left")
        radio_button_bet = Radiobutton(radio_button_frame, text="Bet", variable=radio, value=3, command=radio_select)
        radio_button_bet.pack(side="left")

        def num_only(text):
            if text.isdigit() or text == "":
                return True
            else:
                return False

        no = (entry_frame.register(num_only), '%P')

        cost_label = Label(entry_frame, text="Amount:")
        cost_label.pack()
        cost_field = Entry(entry_frame, validate="key", validatecommand=no)
        cost_field.pack()

        to_win_label = Label(entry_frame, text="To Win:")
        to_win_label.pack()
        to_win_field = Entry(entry_frame, validate="key", validatecommand=no)
        to_win_field.pack(pady=(0, 10))

        win = IntVar()

        win_checkbutton = Checkbutton(entry_frame, text="Winning Slip?", variable=win, onvalue=1, offvalue=2)
        win_checkbutton.pack()

        def submit():

            transact_type = ""
            site = site_field.get()
            transact = radio.get()
            if transact == 1:
                transact_type = "Deposit"
            elif transact == 2:
                transact_type = "Withdrawal"
            elif transact == 3:
                transact_type = "Bet"
            outcome_str = ""
            if str(win_checkbutton.cget('state')) == "disabled":
                outcome_str = ""
            else:
                if win.get() == 1:
                    outcome_str = "Yes"
                elif win.get() == 2:
                    outcome_str = "No"
            cost = cost_field.get()
            if str(to_win_field.cget('state')) == "disabled":
                pay = 0
            else:
                pay = to_win_field.get()

            data = (transact_type, site, cost, pay, outcome_str)
            conn = sqlite3.connect("users.db")
            c = conn.cursor()

            query = f"INSERT INTO {current_user} (transactionType, transactionSite, cost, payout, outcome)" \
                    f"VALUES (?,?,?,?,?)" \

            c.execute(query, data)

            conn.commit()
            conn.close()

            display_table_data()
            current_amount_field.config(text=str(total_amount()))
            profit_label_field.config(text=str(profit_loss()))

        submit_button = Button(entry_frame, text="Add", command=submit)
        submit_button.pack(pady=10)

        button_frame = Frame(main_window)
        button_frame.pack(side=RIGHT, padx=10)

        def total_amount():
            conn = sqlite3.connect("users.db")
            c = conn.cursor()

            c.execute(f"select sum(payout) from {current_user} WHERE outcome = 'Yes'")
            value1 = c.fetchone()[0]

            c.execute(f"SELECT sum(cost) from {current_user} WHERE transactionType = 'Deposit'")
            value2 = c.fetchone()[0]

            c.execute(f"SELECT sum(cost) from {current_user} WHERE transactionType = 'Withdrawal'")
            value3 = c.fetchone()[0]

            c.execute(f"SELECT sum(cost) from {current_user} WHERE transactionType = 'Bet'")
            value4 = c.fetchone()[0]

            c.close()

            if value1 is None:
                value1 = 0
            if value2 is None:
                value2 = 0
            if value3 is None:
                value3 = 0
            if value4 is None:
                value4 = 0

            value5 = value1+value2-value3-value4
            return value5

        def profit_loss():
            conn = sqlite3.connect("users.db")
            c = conn.cursor()

            c.execute(f"SELECT sum(cost) from {current_user} WHERE transactionType = 'Deposit'")
            value1 = c.fetchone()[0]
            print(value1)

            c.execute(f"SELECT sum(cost) from {current_user} WHERE transactionType = 'Withdrawal'")
            value2 = c.fetchone()[0]
            print(value2)
            c.close()

            if value1 is None:
                if value2 is None:
                    return 0
                else:
                    return value2
            elif value2 is None:
                if value1 is None:
                    return 0
                else:
                    return -1 * value1
            else:
                value3 = value2 - value1
                print(value3)
                return value3

        def delete():
            selected_row = entry_table.focus()

            if selected_row:
                data = entry_table.item(selected_row)
                values = data['values']
                entry_id = values[0]

                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                query = f"DELETE FROM {current_user} WHERE id = ?"

                cursor.execute(query, (entry_id,))
                conn.commit()
                conn.close()

                print("Row", entry_id, "deleted successfully")

            display_table_data()
            current_amount_field.config(text=str(total_amount()))
            profit_label_field.config(text=str(profit_loss()))

        delete_button = Button(button_frame, text="Delete Entry", command=delete)
        delete_button.pack()

        label_frame = Frame(main_window)
        label_frame.pack(side=LEFT)

        current_amount_label = Label(label_frame, text="Amount in accounts:")
        current_amount_label.pack()
        current_amount_field = Label(label_frame, text=str(total_amount()))
        current_amount_field.pack()

        profit_label = Label(label_frame, text="Total Profit/Loss:")
        profit_label.pack()
        profit_label_field = Label(label_frame, text=str(profit_loss()))
        profit_label_field.pack()

        print(profit_loss())
        print(total_amount())

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
            main_frame()

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


main_screen()
