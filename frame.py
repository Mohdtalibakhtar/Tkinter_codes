from tkinter import *
root=Tk()
root.geometry("500x500")
f1=Frame(root,bg="Blue", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2=Frame(root,bg="BLUE", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP,fill="x")

lable=Label(f1,text="Tkinter")
lable.pack(pady=200)
lable2=Label(f2,text="Welcome to Python")
lable2.pack()
root.mainloop()