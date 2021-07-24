from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry("644x500")
msg=tkinter.messagebox
def func():
    print("Hello")
    msg.showinfo("Hello", "Im here to help")
def box():
    ans= msg.askyesno("Save", "Want to save file")
    if ans:
        print("You enter yes")
    else:
        print("No")

mainmenu=Menu(root)

menu2=Menu(mainmenu, tearoff=0)
menu2.add_command(label="New File", command=box)
menu2.add_command(label="Open File", command=func)
menu2.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=menu2)

menu3=Menu(mainmenu, tearoff=0)
menu3.add_command(label="Save As", command=func)
menu3.add_cascade(label="Save", command=box)
# root.config(menu=mainmenu)
mainmenu.add_cascade(label="Save", menu=menu3)

helpmenu=Menu(mainmenu)
helpmenu.add_command(label="Help", command=func)
mainmenu.add_cascade(label="Help", menu=helpmenu)

root.mainloop()