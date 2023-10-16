import tkinter as tk
import sqlite3
import random
from tkinter import *
from tkinter import messagebox
import os






#SETUP FONTS AND DATABASE

UIFont = ("Arial", 12)

db = sqlite3.connect('database.db')
cursor = db.cursor()

try:
  if os.path.exists("database.db"):
    pass
except Exception as e:
  os.mknod("database.db")

try:
  cursor.execute("SELECT * FROM database")
  print("Checking for database... database exists!")
except:
  cursor.execute("CREATE TABLE database (id, fn, ln, username, password)")
  print("Database does not exist, created new one")








#LOG IN PANEL

root = Tk()
root.geometry("400x200")
root.config(bg='#050505')

root.title("Login")

user = Label(root, text="Username ", font=UIFont)
user.grid(row=0, column=0)
user.config(bg='#050505')
user.config(fg='#FFFFFF')

password = Label(root, text="Password ", font=UIFont)
password.grid(row=1, column=0)
password.config(bg='#050505')
password.config(fg='#FFFFFF')







# FUNCTIONS FUNCTIONS FUNCTIONS

def account_created():
  messagebox.showinfo("Account created", "Account created")

  # ------------------------------------------


def yas():
  print("WORKED!")

# ------------------------------------------


def login():
  global username
  global password
  username = userlogin.get()
  password = paswdlogin.get()

  cursor.execute(
      f"SELECT * FROM database WHERE username = '{username}' AND password = '{password}'"
  )
  result = cursor.fetchone()

  if result:
    creategui()

# ------------------------------------------


def add_data_to_db(fn, ln, username, password):
  global randid
  randid = random.randint(100000, 999999)

  cursor = db.cursor()
  cursor.execute(
      f"INSERT INTO database VALUES ('{randid}', '{fn}', '{ln}', '{username}', '{password}')"
  )
  cursor.close()
  db.commit()

  cursor = db.cursor()  # Open a new cursor and print the updated rows
  cursor.execute('SELECT * FROM database')
  rows = cursor.fetchall()  #fetches entire teable
  for row in rows:  #intervals each row
    print(row)

  account_created()

  # ------------------------------------------


def createacc():
  root = Tk()
  root.geometry("400x200")
  root.config(bg='#050505')

  root.title("Create account")

  user = Label(root, text="First name ", font=UIFont)
  user.grid(row=0, column=0)
  user.config(bg='#050505')
  user.config(fg='#FFFFFF')

  password = Label(root, text="Last name ", font=UIFont)
  password.grid(row=1, column=0)
  password.config(bg='#050505')
  password.config(fg='#FFFFFF')

  user = Label(root, text="Username ", font=UIFont)
  user.grid(row=2, column=0)
  user.config(bg='#050505')
  user.config(fg='#FFFFFF')

  password = Label(root, text="Password ", font=UIFont)
  password.grid(row=3, column=0)
  password.config(bg='#050505')
  password.config(fg='#FFFFFF')

  global fncreate
  fncreate = Entry(root, textvariable=e1)
  fncreate.grid(row=0, column=1)
  fncreate.config(bg='#101010')
  fncreate.config(fg='#FFFFFF')

  global lncreate
  lncreate = Entry(root, textvariable=e2)
  lncreate.grid(row=1, column=1)
  lncreate.config(bg='#101010')
  lncreate.config(fg='#FFFFFF')

  global usercreate
  usercreate = Entry(root, textvariable=e3)
  usercreate.grid(row=2, column=1)
  usercreate.config(bg='#101010')
  usercreate.config(fg='#FFFFFF')

  global paswdcreate
  paswdcreate = Entry(root, textvariable=e4)
  paswdcreate.grid(row=3, column=1)
  paswdcreate.config(bg='#101010')
  paswdcreate.config(fg='#FFFFFF')

  createacc_button = Button(
      root,
      text="Create account",
      command=lambda: add_data_to_db(fncreate.get(), lncreate.get(), usercreate.get(), paswdcreate.get()),
      font=UIFont)
  createacc_button.grid(row=4, column=0)
  createacc_button.config(bg='#183D2E')
  createacc_button.config(fg='#D2FCEC')

  # ------------------------------------------


def creategui():
  root = Tk()
  root.geometry("400x200")
  root.config(bg='#050505')

  root.title("GUI")

  cursor.execute(f"SELECT fn FROM database WHERE username = '{username}'")
  firstname = str(cursor.fetchone())

  messagebox.showinfo("Welcome", f"Welcome {firstname[2:-3]}")

  # ------------------------------------------






#POST

lgn_button = Button(root, text="Login", command=lambda: login(), font=UIFont)
lgn_button.grid(row=4, column=0)
lgn_button.config(bg='#183D2E')
lgn_button.config(fg='#D2FCEC')

createacc_button = Button(root, text="Create new account", command=lambda: createacc(), font=UIFont)
createacc_button.grid(row=4, column=1)
createacc_button.config(bg='#101010')
createacc_button.config(fg='#FFFFFF')

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()

bullet = "\u2022"  #specifies bullet character

userlogin = Entry(root, textvariable=e1)
userlogin.grid(row=0, column=1)
userlogin.config(bg='#101010')
userlogin.config(fg='#FFFFFF')

paswdlogin = Entry(root, textvariable=e2, show=bullet)
paswdlogin.grid(row=1, column=1)
paswdlogin.config(bg='#101010')
paswdlogin.config(fg='#FFFFFF')

root.mainloop()
