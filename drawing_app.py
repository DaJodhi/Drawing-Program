import turtle
from sys import exit as end
from tkinter import *
import tkinter.messagebox as box
from random import choice
from tkinter import filedialog
from tkinter.colorchooser import *

settings = Tk()
settings.title("Settings")
settings.resizable(False, False)
settings.geometry("380x380")
settings.configure(bg="black")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
jim = turtle.Turtle()
jim.speed(0)
jim.shape("circle")


def choose_colour():
    try:
        (triple, hexstr) = askcolor(title="Colour")
        jim.color(hexstr)
    except TypeError:
        pass


def random_colour():
    jim.color(choice(colors))


colour_frame = Frame(settings, bg="black")
change_colour_button = Button(colour_frame, command=choose_colour, fg="white", bg="gray", text="Choose Colour")
random_colour_button = Button(colour_frame, command=random_colour, text="Random Colour", bg="gray", fg="white")


change_colour_button.grid(column=2, row=1, pady=5, padx=10)
random_colour_button.grid(column=3, row=1, padx=10, pady=5)
colour_frame.pack(side=TOP)


def erasor():
    jim.pensize(10)
    jim.color("#e75480")
    jim.pencolor("white")


erasor_button = Button(settings, command=erasor, text="Erasor", fg="white", bg="gray")
erasor_button.pack(side=TOP)


def submit_pensize():
    jim.pensize(int(pensize_sb.get()))


pensize_frame = Frame(settings, bg="black")
# only lets you choose numbers
pensize_sb = Spinbox(pensize_frame, from_=1, to=50, width=5)
submit_pensize_button = Button(pensize_frame, command=submit_pensize, bg="gray", fg="white", text="Pensize")

pensize_sb.grid(column=1, row=1)
submit_pensize_button.grid(column=2, row=1, padx=5, pady=10)
pensize_frame.pack(side=TOP)


def export():
    filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("ps files", "*.ps"), ("all files", "*.*")))
    box.showinfo("Export to another file type", "You can use a program called Ghostscript to convert the file.")


export_frame = Frame(settings)
export_button = Button(export_frame, bg="gray", fg="white", text="Export", command=export)
end_program_button = Button(export_frame, command=end, bg="red", fg="black", text="End Program")

export_button.grid(column=1, row=1, padx=10, pady=15)
end_program_button.grid(column=2, row=1, padx=15, pady=15)
export_frame.pack(side=TOP)

x1 = 0


def up():
    jim.setheading(90)
    jim.forward(100)


def down():
    jim.setheading(270)
    jim.forward(100)


def left():
    jim.setheading(180)
    jim.forward(100)


def right():
    jim.setheading(0)
    jim.forward(100)


def dragging(x, y):
    jim.ondrag(None)
    # makes the turtle follow the mouse
    jim.goto(x, y)
    # makes function recursive
    jim.ondrag(dragging)


def clear(x, y):
    jim.clear()


def change(x, y):
    global x1
    if x1 == 1:
        x1 = 0
        jim.pendown()
    else:
        jim.penup()
        x1 += 1


turtle.listen()
# anywhere on the turtle screen, onclick is only on the turtle
# 1 is left mouse button, 2 is middle, and 3 is right
jim.ondrag(dragging)
turtle.onscreenclick(dragging, 1)
turtle.onscreenclick(clear, 2)
turtle.onscreenclick(change, 3)
turtle.onkey(up, "w")
turtle.onkey(down, "s")
turtle.onkey(left, "a")
turtle.onkey(right, "d")
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.mainloop()
