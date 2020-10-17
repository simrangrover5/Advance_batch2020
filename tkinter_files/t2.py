
import tkinter as tk

root = tk.Tk()  #root window creation
root.configure(bg="black")
root.title("MyWindow")
root.iconbitmap("myicon.ico")  #give ico file in this function 
w = root.winfo_screenwidth()//2
h = root.winfo_screenheight()//2
root.wm_minsize(w,h)
#root.wm_maxsize(600,600)
root.resizable(0,0)

l1 = tk.Label(root,text="WELCOME TO MY FIRST WINDOW",bg="black",fg="white",font=[None,24])
l2 = tk.Label(root,text="THIS IS MY SECOND LABEL",bg="black",fg="red",font=[None,24])

b1 = tk.Button(root,text="Button1",fg="yellow",bg="black",font=[None,15,"italic"])
b2 = tk.Button(root,text="Button2",fg="yellow",bg="black",font=[None,15,"italic"])

l2.pack(pady=(30,0))
l1.pack()

b1.pack(ipadx=50,ipady=50)
b2.pack()

root.mainloop()
