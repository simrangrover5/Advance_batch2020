
import tkinter as tk
import pymysql as sql
from tkinter import messagebox

root = tk.Tk()  #root window creation
root.configure(bg="black")
root.title("MyWindow")
root.iconbitmap("myicon.ico")  #give ico file in this function 
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
root.wm_minsize(w+100,h+100)
#root.wm_maxsize(600,600)
root.resizable(0,0)

f1 = tk.Frame(root,bg="gray")
f1.pack(ipadx=200,ipady=200,pady=(50,0))

f2 = tk.Frame(root,bg="gray")

def login():
    f1.forget()
    f2.pack(ipadx=200,ipady=200,pady=(50,0))

def signup():
    pass

b3 = tk.Button(f1,text="LOGIN",fg="white",bg="black",font=[None,20,"italic"],command=login)
b4 = tk.Button(f1,text="SIGNUP",fg="white",bg="black",font=[None,20,"italic"],command=signup)

b3.place(rely=0.5,relx=0.1)
b4.place(rely=0.5,relx=0.6)


l2 = tk.Label(f2,text="Enter your name : ",bg="black",fg="white",font=["monospace",24])
l2.grid(row=1,column=0)

var = tk.StringVar()

e1 = tk.Entry(f2,font=[None,25,"italic"],fg="gray",textvariable=var)
e1.grid(row=1,column=1)

l3 = tk.Label(f2,text="Enter your password : ",bg="black",fg="white",font=["monospace",24])
l3.grid(row=2,column=0)

var1 = tk.StringVar()

e2 = tk.Entry(f2,font=[None,25,"italic"],fg="gray",textvariable=var1,show="*")
e2.grid(row=2,column=1)


def getentry():
    db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch7_15")
    cursor = db.cursor()
    user = e1.get()
    passwd = e2.get()
    cmd = f"select * from user where username='{user}'"
    cursor.execute(cmd)
    d = cursor.fetchone()
    var.set("")
    var1.set("")
    if d:
        messagebox.showinfo("INFO","WELCOME")
    else:
        messagebox.showerror("ERROR","USER DOES NOT EXIST")
def getf1():
    f2.forget()
    f1.pack(ipadx=200,ipady=200,pady=(50,0))

b1 = tk.Button(f2,text="SUBMIT",fg="yellow",bg="black",font=[None,15,"italic"],command=getentry)
b1.grid(row=3,column=1,columnspan=2,pady=50)

b2 = tk.Button(f2,text="BACK<<<",fg="yellow",bg="black",font=[None,15,"italic"],command=getf1)
b2.grid(row=3,column=4,columnspan=2,pady=50)

root.mainloop()
