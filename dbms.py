import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.iconbitmap("icon.ico")
root.title("DBMS")

connection = sqlite3.connect('bennett.db')

TABLE_NAME = "student"
SLOT_ID = "slot_id"
STUDENT_NAME = "student_name"
STUDENT_ROLLNO = "student_rollno"
STUDENT_EMAIL = "student_email"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + SLOT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_ROLLNO + " TEXT, " +
                   STUDENT_EMAIL + " TEXT, " + STUDENT_PHONE + " INTEGER);")

appLabel = tk.Label(root, text="Bennett Student DBMS", fg="#06a099", width=35)
appLabel.config(font=("MicrosoftSansSerif", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

class Student:
    studentName = ""
    rollNo = ""
    email = ""
    phoneNumber = 0

    def __init__(self, studentName, rollNo, email, phoneNumber):
        self.studentName = studentName
        self.rollNo = rollNo
        self.email = email
        self.phoneNumber = phoneNumber

nameLabel = tk.Label(root, text="Enter your Name", width=40, anchor='w',font=("MicrosoftSansSerif", 13)).grid(row=1, column=0, padx=(10,0),pady=(30, 0))
rollLabel = tk.Label(root, text="Enter your Roll No", width=40, anchor='w',font=("MicrosoftSansSerif", 13)).grid(row=2, column=0, padx=(10,0))
emailLabel = tk.Label(root, text="Enter your Email Address", width=40, anchor='w',font=("MicrosoftSansSerif", 13)).grid(row=3, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter your Phone Number", width=40, anchor='w',font=("MicrosoftSansSerif", 13)).grid(row=4, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 40)
rollEntry = tk.Entry(root, width = 40)
emailEntry = tk.Entry(root, width = 40)
phoneEntry = tk.Entry(root, width = 40)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
rollEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
emailEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

def Inputs():
    global nameEntry, rollEntry, emailEntry, phoneEntry
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_ROLLNO, STUDENT_EMAIL, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    rno = rollEntry.get()
    rollEntry.delete(0, tk.END)
    email = emailEntry.get()
    emailEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_ROLLNO + ", " + STUDENT_EMAIL + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + rno + "', '" +
                       email + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

def Database():

    root.destroy()
    secondWindow = tk.Tk()
    secondWindow.iconbitmap("icon.ico")

    secondWindow.title("Database")

    appLabel = tk.Label(secondWindow, text="Bennett Student Database",fg="#06a099", width=40)
    appLabel.config(font=("MicrosoftSansSerif", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="Roll No")
    tree.heading("three", text="Email")
    tree.heading("four", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="DBID " + str(row[0]),values=(row[1], row[2],row[3], row[4]))
        i = i + 1

    tree.pack()
    
    secondWindow.mainloop()

save = tk.Button(root, text="Save", command=lambda :Inputs())
save.grid(row=5, column=0, pady=30)

dbButton = tk.Button(root, text="Database", command=lambda :Database())
dbButton.grid(row=5, column=1)

root.mainloop()