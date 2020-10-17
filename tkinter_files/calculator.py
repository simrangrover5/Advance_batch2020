
import tkinter as tk
from tkinter import messagebox
from random import choice

root = tk.Tk()  #root window creation
root.configure(bg="gray")
root.title("MyWindow")
root.iconbitmap("myicon.ico")  #give ico file in this function 
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
root.wm_minsize(w,h)
#root.wm_maxsize(600,600)
root.resizable(0,0)


f1 = tk.Frame(root,bg="gray")
f1.pack()

var = tk.StringVar()
e1 = tk.Entry(f1,font=(None,24),textvariable=var)
e1.pack()

f2 = tk.Frame(root,bg="gray")
f2.pack()

def back():
    e = e1.get()
    var.set(e[:-1])

def clear():
    var.set(" ")
n = 0
for r in range(4):
    for c in range(3):
        if r == 0 and c == 0:
            b1 = tk.Button(f2,text="<<",height=5,width=15,font=(None,12),command=back)
            b1.grid(row=r,column=c)
        elif r == 0 and c == 1:
            b1 = tk.Button(f2,text=n,height=5,width=15,font=(None,12))
            b1.grid(row=r,column=c)
            n += 1
        elif r == 0 and c == 2:
            b1 = tk.Button(f2,text="clr",height=5,width=15,font=(None,12),command=clear)
            b1.grid(row=r,column=c)
        else:
            b1 = tk.Button(f2,text=n,height=5,width=15,font=(None,12))
            b1.grid(row=r,column=c)
            n += 1
root.mainloop()
