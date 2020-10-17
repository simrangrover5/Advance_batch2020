

import tkinter as tk
from random import randint
from tkinter import messagebox

root = tk.Tk()  #root window creation
root.configure(bg="gray")
root.title("MyWindow")
root.iconbitmap("myicon.ico")  #give ico file in this function 
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
root.wm_minsize(w,h)
#root.wm_maxsize(600,600)
root.resizable(0,0)

class Guess:
    def __init__(self,master):  #master = root
        self.root = master
        self.f1 = tk.Frame(master,bg="gray")
        self.f1.pack(ipadx=100,ipady=100)
        self.l1 = tk.Label(self.f1,text="GUESS ANY NUMBER BETWEEN 1 to 100",fg="black",bg="gray",font=(None,24,"italic"))
        self.l1.pack()
        self.l2 = tk.Label(self.f1,text="",bg="gray",fg="red",font=("sans serif",20))
        self.l2.pack(pady=(15,0))
        self.var = tk.StringVar()
        self.e1 = tk.Entry(self.f1,font=[None,20,"italic"],textvariable=self.var)
        self.e1.place(relx=0.3,rely=0.5)
        self.b1 = tk.Button(self.f1,text="SUBMIT",bg="black",fg="blue",height=2,width=10,command=self.check)
        self.b1.place(relx=0.8,rely=0.5)
        self.comp = 40#randint(1,100)
        self.c = 0
    
    def check(self):
        self.c += 1
        user = int(self.e1.get())
        self.var.set("")
        if self.c<=5:
            if user == self.comp:
                messagebox.showinfo("INFO",f"YOU GUESS RIGHT AFTER {self.c} GUESSES!!! CONGRATS")
                self.b1['state'] = "disabled"
                self.l2.configure(text="YOU WON")
            elif user < self.comp:
                self.l2.configure(text="THINK HIGH!!!!!")
            elif user > self.comp:
                self.l2.configure(text="THINK LOW!!!!!!")
        else:
            messagebox.showerror("ERROR",f"YOU LOSS AND THE CORRECT ANSWER IS {self.comp}")
            self.b1['state'] = "disabled"
            self.l2.configure(text="YOU LOSS")
            
obj = Guess(root)
root.mainloop()
