from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root=Tk()
root.geometry("644x700")
root.title("Untitled-Notepad")

def Newfile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)
def Open():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    root.title(os.path.basename(file)+ " -Notepad")
    TextArea.delete(1.0,END)
    f= open(file, "r")
    TextArea.insert(1.0, f.read())
    f.close()

def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + " - Notepad")
        print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def Cut():
    TextArea.event_generate(("<<Cut>>"))
def Copy():
    TextArea.event_generate(("<<Copy>>"))
def Paste():
    TextArea.event_generate(("<<Paste>>"))
def About():
    showinfo("Notepad", "Notepad by Talib")


scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

TextArea=Text(root, font="lucida 13", yscrollcommand=scroll.set)
file=None
TextArea.pack(expand=TRUE, fill=BOTH)
scroll.config(command=TextArea.yview)
menubar=Menu(root)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=Newfile)
filemenu.add_command(label="Open", command=Open)
filemenu.add_command(label="Save", command=Save)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

Editmenu=Menu(menubar, tearoff=0)
Editmenu.add_command(label="Cut", command=Cut)
Editmenu.add_command(label="Copy", command=Copy)
Editmenu.add_command(label="Paste", command=Paste)
menubar.add_cascade(label="Edit", menu=Editmenu)

helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
root.mainloop()