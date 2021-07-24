from tkinter import *

root=Tk()
root.geometry("500x400")
root.title("Canvas")
can_widget=Canvas(root)
can_widget.pack()

can_widget.create_line(0,300,400,0)
can_widget.create_line(0,0,400,300)

can_widget.create_rectangle(3,5,200,200)
can_widget.create_text(100,100, text="Canvas tkinter")
root.mainloop()