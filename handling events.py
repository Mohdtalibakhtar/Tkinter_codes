from tkinter import *

root=Tk()
root.geometry("644x433")

def func(event):
    print("You clicked on the button at" , event.x, event.y)

b1= Button(root,text="Click on me")
b1.pack()

b1.bind("<Button-1>", func)
b1.bind("<Double-1>", quit)
root.mainloop()

