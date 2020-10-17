
import tkinter as tk

root = tk.Tk()  #root window creation
root.configure(bg="black")
root.title("MyWindow")
root.iconbitmap("myicon.ico")  #give ico file in this function 
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
root.wm_minsize(w+100,h+100)
#root.wm_maxsize(600,600)
root.resizable(0,0)


l1 = tk.Label(root,text="WELCOME ",bg="black",fg="red",font=["monospace",24])
l1.grid(row=0,column=1,pady=50)

l2 = tk.Label(root,text="Enter your name : ",bg="black",fg="white",font=["monospace",24])
l2.grid(row=1,column=0)

var = tk.StringVar()

e1 = tk.Entry(root,font=[None,25,"italic"],fg="gray",textvariable=var)
e1.grid(row=1,column=1)


def getentry():
    n = e1.get()
    l1.config(text="WELCOME "+n.upper())
    var.set("1")

b1 = tk.Button(root,text="SUBMIT",fg="yellow",bg="black",font=[None,15,"italic"],command=getentry)
b1.grid(row=2,column=1,columnspan=2,pady=50)

root.mainloop()
