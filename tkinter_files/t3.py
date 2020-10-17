
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

f1 = tk.Frame(root)
f2 = tk.Frame(root)
f1.configure(bg="#abcdef")
f2.configure(bg="#abc123")

l1 = tk.Label(f1,text="WELCOME TO MY FIRST WINDOW",bg="#abcdef",fg="black",font=[None,24])
l2 = tk.Label(f2,text="THIS IS MY SECOND LABEL",bg="#abc123",fg="red",font=[None,24])

b1 = tk.Button(f1,text="EXIT FRAME1",fg="yellow",bg="black",font=[None,15,"italic"],command=f1.forget)
b2 = tk.Button(f2,text="EXIT FRAME2",fg="yellow",bg="black",font=[None,15,"italic"],command=f2.forget)

l2.pack()
l1.pack()

b1.pack(ipadx=30,ipady=20)
b2.pack(ipadx=30,ipady=20)

f1.pack(ipadx=150,pady=50)
f2.pack(ipadx=150,pady=50)

b3 = tk.Button(root,text="GET FRAME1",fg="yellow",bg="black",font=[None,15,"italic"],command=f1.pack)
b4 = tk.Button(root,text="GET FRAME2",fg="yellow",bg="black",font=[None,15,"italic"],command=f2.pack)
b5 = tk.Button(root,text="EXIT MAIN",fg="yellow",bg="black",font=[None,15,"italic"],command=root.destroy)

b3.pack(fill=tk.X)
b4.pack(fill=tk.X)
b5.pack(fill=tk.X)
root.mainloop()
