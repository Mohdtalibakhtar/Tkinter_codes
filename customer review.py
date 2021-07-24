from tkinter import *
root=Tk()
root.geometry("644x480")
root.title("Customer Review")

def func():

    # rating=slider.get()
    print(f"{nameval.get()} given the rating of {slider.get()}/10")
    with open ("reviews.txt", "a") as f:
        f.write(f"{nameval.get()} has given us the rating of {slider.get()}/10. \n")

head=Label(text="Give us a Review", font="comicsansms 15 bold")
head.pack()

nameval=StringVar()
Label(text="Enter your Name").pack(pady=10)
name=Entry(root, textvariable=nameval).pack()
slider=Scale(root, from_=0, to=10, orient=HORIZONTAL)
slider.pack()

Button(root, text="Submit", command=func).pack(pady=10)
root.mainloop()