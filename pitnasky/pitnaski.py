from tkinter import *
from tkinter import messagebox
from random import randint


def findEmptyCell():
    for i in range(16):
        if field[i]["text"] == "":
            return i
    return -1


def isEnd():
    global field
    for i in range(15):
        if field[i]["text"] != str(i + 1):
            return
    messagebox.showinfo("Congratulation", "You won")
    exit(0)


def keyPress(e):
    pos = findEmptyCell()

    if e.keycode == 38:  # Up (keycode for up arrow)
        if pos < 12:
            field[pos]["text"], field[pos + 4]["text"] = field[pos + 4]["text"], field[pos]["text"]
    elif e.keycode == 40:  # Down (keycode for down arrow)
        if pos > 3:
            field[pos]["text"], field[pos - 4]["text"] = field[pos - 4]["text"], field[pos]["text"]
    elif e.keycode == 39:  # Left (keycode for left arrow)
        if pos % 4 != 0:
            field[pos]["text"], field[pos - 1]["text"] = field[pos - 1]["text"], field[pos]["text"]
    elif e.keycode == 37:  # Right (keycode for right arrow)
        if (pos + 1) % 4 != 0:
            field[pos]["text"], field[pos + 1]["text"] = field[pos + 1]["text"], field[pos]["text"]

    isEnd()


def setField():
    global field
    n = 0
    for i in range(4):
        for j in range(4):
            field.append(Label(form, width=6, height=3, font="Arial 20 bold", borderwidth=1, relief="solid"))
            field[n].grid(row=i, column=j)
            n += 1

    # Fill with numbers from 1 to 15, leaving one space empty
    k = 1
    while k < 16:
        a = randint(0, 15)
        if field[a]["text"] == "":
            field[a]["text"] = str(k)
            k += 1


form = Tk()
form.title("Game")
form.resizable(False, False)
field = []

setField()

form.bind("<Key>", keyPress)

form.mainloop()
