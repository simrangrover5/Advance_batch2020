
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


img = tk.PhotoImage(file="newcert1.png")

l1 = tk.Label(root,image=img)
l1.pack()

root.mainloop()
