# Task : Random Password Generator
# Create a program that generates a random
# password of a user-defined length.

import tkinter as tk
from tkinter import *
import random
import string
import pyperclip
from tkinter.font import Font

root = tk.Tk()
root.title("PASSWORD GENERATOR")
root.config(bg="black")
root.geometry("400x400")
root.resizable(0, 0)

def generate_password():
    password = ''
    length = pass_len.get()
    if length < 4:
        pass_str.set("Length should be at least 4")
    else:
        for _ in range(length):
            password += random.choice(string.ascii_letters + string.digits)
        pass_str.set(password)

def copy_password():
    pyperclip.copy(pass_str.get())

# Styling
root.config(bg="#A1EEBD")

heading = tk.Label(root, text='PASSWORD GENERATOR', font=('Times New Roman', 18, 'bold', 'italic', 'underline'), fg='black', bg='white', relief=SOLID, bd = 5)
heading.place(relwidth=1)

pass_label = tk.Label(root, text='PASSWORD LENGTH', font=('Times New Roman', 12, 'bold'), bg="#8ADAB2", fg = 'blue')
pass_label.place(x = 120 , y = 45)

pass_len = tk.IntVar()
length = tk.Spinbox(root, from_=4, to_=32, textvariable=pass_len, bg='Pink', width=25, relief=tk.RIDGE, font=Font(family='Helvetica', size=11, weight='bold'))
length.place(x = 85 , y = 80)

pass_str = tk.StringVar()

generate_button = tk.Button(root, text="GENERATE PASSWORD", command=generate_password, bg='brown', fg='white', font=('Arial', 10, 'bold'))
generate_button.place(x = 120 , y = 120)

password_entry = tk.Entry(root, textvariable=pass_str, font=('Times New Roman', 12), bd=3, bg='lightblue', width=30, relief=tk.RIDGE)
password_entry.place(x = 65 , y = 160)

copy_button = tk.Button(root, text='COPY TO CLIPBOARD', command=copy_password, bg='#2196f3', fg='white', font=('Arial', 10, 'bold'))
copy_button.place(x = 125 , y = 200)

app_label = tk.Label(root, text='App', font=('Times New Roman', 20, 'bold'), fg='Red' ,bg = '#A1EEBD')
app_label.pack(side=tk.BOTTOM)

root.mainloop()