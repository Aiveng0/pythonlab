import random
from tkinter import *


def ran(event):
    a = [1, 2, 3, 4, 5, 6]
    b = random.choice(a)
    label_1["text"] = "Вам випало ", b


root = Tk()

label_1 = Label(root, text="Киньте кубик", width=15, height=3)
b1 = Button(root, text="Кинути кубик")
label_1.pack()
b1.pack()
b1.bind("<Button-1>", ran)

root.mainloop()
