from tkinter import *

start_root=Tk()

#format width x height
start_root.geometry("733x434")

#formal width,height
# start_root.minsize(200,600)
# start_root.maxsize(700,700)

user=Label(text="PyCharm Community Edition")
user2=Label(text="+ Start a new project")
user.pack()
user2.pack()
start_root.mainloop()


