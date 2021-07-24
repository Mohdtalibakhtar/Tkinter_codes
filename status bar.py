from tkinter import *
root=Tk()
root.geometry("644x455")

def upload():
    import time
    statusvar.set("Uploading")
    status.update()
    time.sleep(3)
    statusvar.set("Ready")

statusvar=StringVar()
statusvar.set("Ready")
status=Label(root, textvariable=statusvar, anchor="w")
status.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()
root.mainloop()