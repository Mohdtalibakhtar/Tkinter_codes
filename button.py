from tkinter import *

root=Tk()

root.geometry("500x500")
def textchange():
    print("Tkinter")

def tk():
    print("yes I know")

def guys():
    print("Hi")

def print2():
    print("Yes Printed")

b1 = Button(borderwidth=6, fg="orange", text="Hello", command=textchange)
b1.pack(side=LEFT, padx=2, anchor="nw")

b2=Button(borderwidth=6, fg="green", text="This is Tkinter", command=tk)
b2.pack(side=LEFT, padx=2, anchor="nw")

b3=Button(borderwidth=6, fg="blue", text="Hello Guys", command=guys)
b3.pack(side=LEFT, padx=2, anchor="nw")

b4 = Button(borderwidth=6, fg="red", text="Print now", command=print2)
b4.pack(side=LEFT, padx=2, anchor="nw")

root.mainloop()