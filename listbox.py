from tkinter import *
root=Tk()
root.geometry("644x544")
root.title("List Box")

def add():
    global i
    lb.insert(ACTIVE,f"{i}")
    i+=1
i=1
lb=Listbox(root)
lb.pack()
lb.insert(END, "Hello")

Button(root, text="Insert Item", command=add).pack()
root.mainloop()