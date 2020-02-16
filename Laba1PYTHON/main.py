import tkinter as tk
import random
from tkinter import ttk
from tkinter import Menu
from tkinter import *

# Create instance
win = tk.Tk()

# Add a title
win.title("GUI Python")
# Gets the requested values of the height and widht.
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(win.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
win.geometry("500x300+{}+{}".format(positionRight, positionDown))

# Disable resizing the GUI by passing in False/False
win.resizable(False, False)


# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()


# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)


def laba1():
    def tchange(event):
        txt = entry_1.get()
        win.title(txt)

    def ran(event):
        a = [1, 2, 3, 4, 5, 6]
        b = random.choice(a)
        lab3["text"] = "Вам випало ", b
        lab3["height"] = "5"

    def hello(event):
        lab2["text"] = "Hello world!"
        lab2["bg"] = "yellow"
        lab2["fg"] = "blue"

    tabControl = ttk.Notebook(win)  # Create Tab Control

    tab1 = ttk.Frame(tabControl)  # Create a tab

    tabControl.add(tab1, text='Завдання 1')  # Add the tab

    lab1 = Label(tab1, text="Моя перша програма!", font=67, width=45, height=2, bg="yellow", fg="blue")
    b1 = Button(tab1, text="Закрити")
    lab1.grid(row=0, column=2)
    b1.grid(row=1, column=2)
    b1.bind("<Button-1>")

    tab2 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab2, text='Завдання 2')  # Make second tab visible
    lab2 = Label(tab2, width=45, height=5, font=67)
    lab2.grid()
    b3 = Button(tab2, text="Привiтання", width=28, height=8)
    b4 = Button(tab2, text="Закрити", width=28, height=8)
    b3.grid(sticky=W)
    b4.grid(row=1, sticky=E)
    b3.bind("<Button-1>", hello)

    tab3 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab3, text='Завдання 3')  # Make second tab visible
    lab3 = Label(tab3, text="Киньте кубик", width=45, height=2, font=67, bg="yellow", fg="blue")
    lab3.grid()
    b5 = Button(tab3, text="Кинути кубик", height=8, width=45)
    b5.grid()
    b5.bind("<Button-1>", ran)

    tab4 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab4, text='Завдання 4')  # Make second tab visible
    lab4 = Label(tab4, text="Введiть новий заголовок:", width=45, height=2, font=67, bg="yellow", fg="blue")
    lab4.grid()
    entry_1 = Entry(tab4)
    entry_1.grid()
    b6 = Button(tab4, text="Змiнити заголовок", height=8, width=50)
    b6.grid()
    b6.bind("<Button-1>", tchange)

    tabControl.pack(expand=1, fill="both")  # Pack to make visible


# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Лаба 1", command=laba1)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="Tasks", menu=file_menu)

# Add another Menu to the Menu Bar and an item

# ======================
# Start GUI
# ======================
win.mainloop()
