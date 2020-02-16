from tkinter import *


def closer(event):
    root.destroy()


def hello(event):
    label_1["text"] = "Hello world!"


root = Tk()
root.title("Program2")

label_1 = Label(root, width=12, height=2)
b1 = Button(root, text="Закрити")
b2 = Button(root, text="Привiтання")
label_1.grid()
b1.grid(row=1, column=1)
b2.grid(row=1, column=0)
b1.bind("<Button-1>", closer)
b2.bind("<Button-1>", hello)

root.mainloop()
