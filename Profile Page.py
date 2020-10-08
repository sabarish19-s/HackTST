import tkinter as tk
from tkinter import ttk
window1 = tk.Tk()
window1.title('Login')
window1.geometry("550x600")
#making the combo box
a=tk.StringVar()
Username = ttk.Combobox(window1,width = 30,textvariable = a)
Username['Username'] = ()
Userpass=()
#space for typing in password
password = StringVar() #Password variable
passEntry = Entry(, textvariable=password, show='*').place(relx=0.5, rely=0.35, anchor='center')