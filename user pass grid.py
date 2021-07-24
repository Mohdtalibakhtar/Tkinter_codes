from tkinter import *

root=Tk()

def field():
    print(f"The value of user is {nameval.get()}")
    print(f"The value of password is {numval.get()}")
    with open("tkinter.txt", "a") as file:
     file.write(f"/nThe name is {nameval} and phone is {numval}\n")

root.geometry("500x500")

user=Label(root, text="Name")
password=Label(root, text="Phone no")
user.grid()
password.grid()

numval=StringVar()
nameval=StringVar()

userentry=Entry(root, textvariable= numval)
passentry=Entry(root, textvariable= nameval)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit", command=field).grid()

root.mainloop()