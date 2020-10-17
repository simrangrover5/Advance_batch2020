
import tkinter as tk
from tkinter import messagebox
from random import choice

root = tk.Tk()  #root window creation
root.configure(bg="black")
root.title("MyWindow")
root.iconbitmap("myicon.ico")  #give ico file in this function 
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
root.wm_minsize(w,h)
#root.wm_maxsize(600,600)
root.resizable(0,0)
run = False
def on_enter(event):
    global run
    run = False
    change()
    
def on_leave(event):
    global run
    run = True
    change()

def get_color():
    c = "#"
    l = ['1','2','3','4','5','6','a','b','c','d','e','f']
    for i in range(6):
        c += choice(l)
    return c

def change():
    global run
    if run == True:
        c = get_color()
        l2.configure(fg=c)
        l2.after(1000,change)

def start():
    global run
    run = True
    l1.configure(text="STARTED!!!!")
    change()


l1 = tk.Label(root,text="WELCOME!!!",fg="white",bg="black",font=(None,24,"italic"))
l1.pack()
l2 = tk.Label(root,text="COLORS",bg="black",fg="red",font=("sans serif",30))
l2.pack(pady=(15,0))

b1 = tk.Button(root,text="START",bg="black",fg="gray",height=1,width=10,command=start,font=(None,15))
b1.pack(fill="x")


l2.bind("<Enter>",on_enter)
l2.bind("<Leave>",on_leave)

root.mainloop()
