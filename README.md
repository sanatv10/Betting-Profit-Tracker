# 2520-ProfitTracker
This is a desktop application that allows you to enter transactions you have made on sports betting apps and will keep track of
the total money you have left to wager as well as your profit and losses.

## Table of Contents
- Project Description
- Installation
- Usage

## Project Description
This project is written in Python and utilizes the sqlite and tkinter libraries. SQLite is used to keep track of users and keep track
of all user added entries. Tkinter is used for the GUI. When starting up the app there is a login page that allows you to either log in to 
an existing account or create a new account. Once an account is created and log in is successful the main window is made up of a
table with all entries as well as a pane that has fields that allow you to enter the details of a new entry. The profit/loss and money that
has accumulated in all accounts will be calculated from the values present in the table.

## Installation
Installation is pretty straight forward as this project uses libraries that are already included in Python. Just download the code provided
in this github repository and run it in an ide of your choice. When running the code first run createTable.py to initialize the users table,
then run main.py. For example, if running in terminal enter the following commands:

python3 createTable.py

python3 main.py

The first command will create the users.db file, and the second command will run the program.

## Usage
The intended use of this program are for people who sports gamble. The login screen will be the first to come up upon running the program,
this is where you will be able to either make an account or login. If you are making account just enter your wanted user and password then 
submit and login with those same credentials. Upon logging in you will be presented with a table and 3 frames. The table shows all of the
entries that you have added and should be empty for new users. The bottom left frame is werw you will be able to add new entries and it 
takes the following information: the website used, the type of transaction(withdrawal, deposit, or bet), the amount of said transaction,
and if the transaction type is a bet you will also have to enter the potential winnings and whether or not the bet won or loss. There is
also a delete feature that allows you to select rows to delete from the table. The amount you have in your accounts and your current
profit/loss will be displayed on the bottom left of the window.
