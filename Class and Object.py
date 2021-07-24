from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("544x455")

    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var, anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("Button clicked")

    def Button(self,inptext):
        Button(text=inptext, command=self.click).pack()

if __name__ == '__main__':
    window=GUI()
    window.status()
    window.Button("Click me")
    window.mainloop()
