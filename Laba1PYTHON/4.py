from tkinter import *


def tchange(event):
    txt = entry_1.get()
    root.title(txt)


root = Tk()
root.title("Hello World!!!!!!")
label_1 = Label(root, width=40, height=2, text="Введiть новий заголовок:")
label_1.pack()
entry_1 = Entry(root)
entry_1.pack()
button_1 = Button(root, text="Змiнити заголовок")
button_1.pack()
button_1.bind("<Button-1>", tchange)

root.mainloop()
