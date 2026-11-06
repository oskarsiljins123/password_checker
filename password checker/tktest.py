import tkinter as tk

root = tk.Tk()

root.title("Password Checker")

root.geometry("600x800")

lable = tk.Label(root, text="Enter a password", font=("Arial", 30))
lable.place(x=150, y=30)

textbox = tk.Entry(root, font=("Arial", 30),show="*")
textbox.place(x=150, y=100, width=300, height=50)

def run():
    password = textbox.get()
    print(password)

button = tk.Button(root, text="Check Password", font=("Arial", 30), command=run)
button.place(x=150, y=200)


root.mainloop()
