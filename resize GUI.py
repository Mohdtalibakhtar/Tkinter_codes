from tkinter import *
root=Tk()

root.geometry("250x200")

root.title("GUI Resizer")
head=Label(root, text="GUI Resizer", font="comicsansms 11 bold")
head.grid(pady=15, padx=15)
def func():
    widthv=widthval.get()
    heightv=heightval.get()
    print(f"You write width {widthv} and height {heightv}")
    root.geometry(f"{widthv}x{heightv}")

width=Label(root, text="Enter Width")
width.grid()

height=Label(root, text="Enter Height")
height.grid()

widthval=Entry(root)
widthval.grid(row=1,column=3)

heightval=Entry(root)
heightval.grid(row=2,column=3)

submit=Button(root, text="Submit", command=func)
submit.grid(row=3, column=3,pady=10)
root.mainloop()
