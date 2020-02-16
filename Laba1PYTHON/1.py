from tkinter import *


def closer(event):
    root.destroy()


root = Tk()

label_1 = Label(root, text="Моя перша програма")
label_1.grid()
b1 = Button(root, text="Закрити")
b1.grid(row=1)
b1.bind("<Button-1>", closer)
root.mainloop()
