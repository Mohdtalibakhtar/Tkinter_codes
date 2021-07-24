from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry("644x500")
msg=tkinter.messagebox

#Create function which will execute when submit button will be pressed
def func():
    print(f"You entered length {slider.get()}")
    print(f"You choose width {slider2.get()}")
    lengthval=slider.get()         #Get the value of slider in a variable
    widthval=slider2.get()
    root.geometry(f"{lengthval}x{widthval}")


#Create a slider for length
length=Label(root, text="Length").pack()
slider=Scale(root,from_=0, to=1000, orient=HORIZONTAL, tickinterval=500)
slider.pack()

#Create a slider for width
width=Label(root, text="Enter width").pack()
slider2=Scale(root,from_=0, to=1000, orient=HORIZONTAL, tickinterval=500)
slider2.pack()

#Create button to submit
Button(root, text="Submit", command=func).pack(pady=10)
root.mainloop()