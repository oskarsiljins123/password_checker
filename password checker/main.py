#importing SQLite in order to be able to use it to develop the databses that will store the bad passwords as well as save the new unsecre passwords developed by the user
import sqlite3

#importing tkinter in order to be able to use it to develop the GUI for the password checker application
import tkinter as tk

#creating a connection to the database that will contain the bad passwords and creating a cursor to execute commands that will interact with that specific database
connection = sqlite3.connect("badpasswords.db")
badpasswords_cursor = connection.cursor()

#creating anothewr connection to the database that will contain the common injection patterns and creating a cursor to execute commands that will interact with that specific database
connection = sqlite3.connect("injection.db")
injection_cursor = connection.cursor()

#cretating a table in the badpasswords database that will contain the bad passwords in a single column called password
badpasswords = """ CREATE TABLE IF NOT EXISTS
badpasswords(password text)"""
badpasswords_cursor.execute(badpasswords)

#inserting a list of common bad passwords into the badpasswords table in the badpasswords database
badpasswords_cursor.execute('INSERT INTO badpasswords (password) VALUES ("password"), ("123456"), ("123456789"), ("qwerty"), ("abc123"), ("football"), ("monkey"), ("letmein"), ("shadow"), ("master"), ("666666"), ("qwertyuiop"), ("123321"), ("mustang"), ("1234567"), ("12345678"), ("princess"), ("admin"), ("welcome")')

#creating a table in the injection database that will contain the common injection patterns in a single column called injections
injection_db = """ CREATE TABLE IF NOT EXISTS
dangerous(injections text)"""
injection_cursor.execute(injection_db)

#inserting a list of common injection patterns into the dangerous table in the injection database
injection_cursor.execute('''INSERT INTO dangerous (injections) VALUES ("' OR '1'='1'; DROP TABLE users;"), ("eval()"),("; cat /etc/passwd")''')

#creating the GUI for the password checker application using tkinter
root = tk.Tk()

#adding a title to the GUI window
root.title("Password Checker")

#setting the dimentions of the GUI window
root.geometry("600x800")

#adding a label to the GUI window that prompts the user to enter a password
lable = tk.Label(root, text="Enter a password", font=("Arial", 30))
lable.place(x=150, y=30)


textbox = tk.Entry(root, font=("Arial", 30),show="*")
textbox.place(x=150, y=100, width=300, height=50)

output_box = tk.Text(root, font=("Arial", 10), height=10, width=90)
output_box.place(x=0, y=300)

def run():
    pass_rate = 0
    common_advice = 0
    length_advice = 0
    special_advice = 0
    capital_advice = 0

    output_box.delete("1.0", tk.END)  # Clear the output box before displaying new results

    
    password = textbox.get()

    #retrieving the list of injections from the dangerous table in the injection database and storing them in a list called injection_list
    injection_cursor.execute("SELECT injections FROM dangerous")
    injection_list = [row[0] for row in injection_cursor.fetchall()]  

    if password in injection_list:
        output_box.insert(tk.END, "Your input is dangerous please enter a different one\n")
    else:
        pass_rate += 20

        #retrieving the list of bad passwords from the badpasswords table in the badpasswords database and storing them in a list called badpasswords_list
        badpasswords_cursor.execute("SELECT password FROM badpasswords")
        badpasswords_list = [row[0] for row in badpasswords_cursor.fetchall()]  

        if password in badpasswords_list:
            common_advice += 1
        else:
            pass_rate += 20

        leanth = len(password)

        if leanth < 12:
            length_advice = 1
        else:
            pass_rate += 20

        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
        if any(char in special_characters for char in password):
            pass_rate += 20
        else:
            special_advice += 1

        capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if any(char in capital_letters for char in password):
            pass_rate += 20
        else:
            capital_advice += 1

        output_box.insert(tk.END, f"Your password is rated at {pass_rate}%\n")

        if common_advice == 1:
            output_box.insert(tk.END, "Your password is too common. Please choose a different password.\n")
        if length_advice == 1:
            output_box.insert(tk.END, "Your password is too short. Please choose a different password.\n")
        if special_advice == 1:
            output_box.insert(tk.END, "Your password does not contain enough special characters. Please choose a different password.\n")
        if capital_advice == 1:
            output_box.insert(tk.END, "Your password does not contain enough capital letters. Please choose a different password.\n")






button = tk.Button(root, text="Check Password", font=("Arial", 30), command=run)
button.place(x=150, y=200)

root.mainloop()