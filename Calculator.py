from tkinter import *
root=Tk()
root.geometry("450x550")
root.title("My Calculator")
def click(event):
    global scval
    text= event.widget.cget("text")
    print(text)
    if text== "=":
        if scval.get().isdigit():
            value=int(scval.get())
        else:
            value=eval(screen.get())

        scval.set(value)
        screen.update()
    elif text== "C":
        scval.set("")
    else: 
        scval.set(scval.get()+text)
        screen.update()

scval=StringVar()
scval.set("")
screen=Entry(root, textvar=scval, font="lucida 35 bold")
screen.pack(fill=X,pady= 10, padx=10)

f1=Frame(root, bg="grey")
b= Button(f1,bg="orange" ,text="9", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=20)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange",  text="8", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange", text="7", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b= Button(f1,bg="orange", text="6", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(root, bg="grey")
b=Button(f1,bg="orange",  text="5", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange", text="4", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b= Button(f1,bg="orange", text="3", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange",  text="2", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(root, bg="grey")

b=Button(f1,bg="orange", text="1", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b= Button(f1,bg="orange" ,text="0", font="lucida 30 bold")
b.pack(side=LEFT, padx=6, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange",  text="C", font="lucida 28 bold", pady=5)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange", text="=", font="lucida 30 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f1.pack()


f1=Frame(root, bg="grey")
b= Button(f1,bg="orange" ,text="*", font="lucida 30 bold")
b.pack(side=RIGHT, padx=6, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange",  text="/", font="lucida 28 bold", pady=5)
b.pack(side=RIGHT, padx=10, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange", text="-", font="lucida 35 bold")
b.pack(side=RIGHT, padx=14, pady=10)
b.bind("<Button-1>", click)

b=Button(f1,bg="orange", text="+", font="lucida 30 bold")
b.pack(side=RIGHT, padx=18, pady=10)
b.bind("<Button-1>", click)
f1.pack()
root.mainloop()