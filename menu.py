from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry("644x500")
root.title("Menubar")
tsmg=tkinter.messagebox
def func():
    print("Hello ")
    tsmg.showinfo("Help", "hello")

menubar=Menu(root)
menu=Menu(menubar)

menu.add_command(label="Hello!", command=func)
menu.add_command(label="file", command=func)
menu.add_command(label="Save", command=func)
menu.add_command(label="Quit!", command=quit)

# menubar.add_cascade(label="File", menu=menu)
menubar.add_cascade(label="File", menu=menu)
root.config(menu=menubar)
root.mainloop()

