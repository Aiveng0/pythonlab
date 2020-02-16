from tkinter import *


def output(event):
    txt = entry1.get()

    if int(txt) < 18:
        label1["text"] = "Закройте приложение"
    else:
        label1["text"] = "Добро пожаловать"


root = Tk()
root.title("How old are you?")

entry1 = Entry(root, width=3, font=15)
b1 = Button(root, text="Check")
label1 = Label(root, width=27)

entry1.grid(row=0, column=0)
b1.grid(row=0, column=1)
label1.grid(row=0, column=2)

b1.bind("<Button-1>", output)

root.mainloop()
