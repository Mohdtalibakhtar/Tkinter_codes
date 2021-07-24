from tkinter import *
from PIL import Image, ImageTk
user_root=Tk()

user_root.geometry("500x500")
# photo=PhotoImage(file="1.JPG")
#for jpg images

image=Image.open("1.JPG")
photo=ImageTk.PhotoImage(image)
user_title=Label(text="Hello this is me")

user_lable=Label(image=photo)
user_title.pack()
user_lable.pack()

user_root.mainloop()