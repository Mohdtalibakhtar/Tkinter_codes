from tkinter import *

root=Tk()
root.geometry("500x500")

def submit():
    print(f"{nameval.get(), phoneval.get(), genderval.get(), foodservice.get()}")
    with open ("records.txt", "a") as f:
        f.write(f"{nameval.get(), phoneval.get(), genderval.get(), foodservice.get()}\n")

head=Label(text="Welcome to form", font="comicsansms 15 bold", pady=20).grid(row=0, column=1)

#Creating Text
name=Label(text="Name")
phone=Label(text="Phone Number")
gender=Label(text="Gender")

#packing text
name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)

#Variable of text field
nameval=StringVar()
phoneval=StringVar()
genderval=StringVar()
foodservice=IntVar()

#create textfield
nameentry=Entry(root, textvariable=nameval)
phoneentry=Entry(root, textvariable=phoneval)
genderentry=Entry(root, textvariable=genderval)

#packing text field
nameentry.grid(row=1, column=2)
phoneentry.grid(row=2, column=2)
genderentry.grid(row=3, column=2)

#checkbox
food= Checkbutton(root, text="Want to add meal ?", variable=foodservice)
food.grid(row=4, column=2)

#submit
b1= Button(text="Submit", command=submit)
b1.grid(row=5, column=2)

root.mainloop()