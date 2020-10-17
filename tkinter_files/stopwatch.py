
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()  #root window creation
root.configure(bg="gray")
root.title("MyWindow")
root.iconbitmap("myicon.ico")  #give ico file in this function 
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
root.wm_minsize(w,h)
#root.wm_maxsize(600,600)
root.resizable(0,0)
run = False
c = 66600
def counter():
    global run,c
    if run:
        d = datetime.fromtimestamp(c)
        l2.configure(text=d.strftime("%X"))
        c += 1
        l2.after(1000,counter)

def start():
    
    global run
    run = True
    b1['state'] = "disabled"
    b2['state'] = "normal"
    b3['state'] = "normal"
    counter()
    
def reset():
    
    global run,c
    c = 66600
    run = False
    d = datetime.fromtimestamp(c)
    l2.configure(text=d.strftime("%X"))
    b3['state'] = "disabled"
    b2['state'] = "normal"
    b1['state'] = "normal"
    
def stop():
    global run,c
    run = False
    b2['state'] = "disabled"
    b1['state'] = "normal"
    b3['state'] = "normal"

l1 = tk.Label(root,text="WELCOME TO STOPWATCH!!!",fg="black",bg="gray",font=(None,24,"italic"))
l1.pack()
l2 = tk.Label(root,text="",bg="gray",fg="black",font=("sans serif",20))
l2.pack(pady=(15,0))

b1 = tk.Button(root,text="START",bg="black",fg="gray",height=1,width=10,command=start,font=(None,15))
b1.pack(fill="x")
b2 = tk.Button(root,text="STOP",bg="black",fg="gray",height=1,width=10,command=stop,font=(None,15))
b2.pack(fill="x")
b3 = tk.Button(root,text="RESET",bg="black",fg="gray",height=1,width=10,command=reset,font=(None,15))
b3.pack(fill="x")

root.mainloop()
