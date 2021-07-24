from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("644x455")
msg=messagebox
def order():
    msg.showinfo("Your order", f"Your order for {var.get()} is comfirm")

head=Label(text="Choose Your Dish", font="comicsansms 15 bold")
head.pack()

var=StringVar()
var.set("Radio")
radio=Radiobutton(root, text="Dosa", pady=5, variable=var, value="Dosa").pack(anchor="w")
radio=Radiobutton(root, text="Idli", pady=5, variable=var, value="Idli").pack(anchor="w")
radio=Radiobutton(root, text="Vada", pady=5, variable=var, value="Vada").pack(anchor="w")
radio=Radiobutton(root, text="Sambhar", pady=5, variable=var, value="Sambhar").pack(anchor="w")

Button(text="Submit", command=order).pack()
root.mainloop()