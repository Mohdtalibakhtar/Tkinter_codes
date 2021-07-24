from tkinter import *
root=Tk()
root.geometry("644x455")

scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

# list=Listbox(root, yscrollcommand=scroll.set)
# for i in range(500):
#     list.insert(END, f"Item {i}")

text=Text(root, yscrollcommand=scroll.set)
text.pack(fill=BOTH)
scroll.config(command=text.yview)
root.mainloop()