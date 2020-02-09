"""A simple drawing program based on Tkinter and Turtle."""
import turtle
from sys import exit as end
from tkinter import Tk, Frame, Button, Spinbox, TOP, filedialog
import tkinter.messagebox as box
from random import choice
from tkinter.colorchooser import askcolor

# Version 2.1.1

SETTINGS = Tk()
SETTINGS.title("Settings")
SETTINGS.resizable(False, False)
SETTINGS.geometry("380x380")
SETTINGS.configure(bg="black")

COLOURS = ("red", "orange", "yellow", "green", "blue", "purple", "black")
JIM = turtle.Turtle()
JIM.speed(0)
JIM.shape("circle")


def choose_colour():
    """Bring up a colour choosing screen."""
    try:
        (triple, hexstr) = askcolor(title="Colour")
        JIM.color(hexstr)
    except TypeError:
        pass


def random_colour():
    """Choose a random colour from a small tuple."""
    JIM.color(choice(COLOURS))


COLOUR_FRAME = Frame(SETTINGS, bg="black")
CHANGE_COLOUR_BUTTON = Button(COLOUR_FRAME, command=choose_colour,
                              fg="white", bg="gray", text="Choose Colour")
RANDOM_COLOUR_BUTTON = Button(COLOUR_FRAME, command=random_colour,
                              text="Random Colour", bg="gray", fg="white")


CHANGE_COLOUR_BUTTON.grid(column=2, row=1, pady=5, padx=10)
RANDOM_COLOUR_BUTTON.grid(column=3, row=1, padx=10, pady=5)
COLOUR_FRAME.pack(side=TOP)


def erasor():
    """Easy way to make the turtle an erasor.

    Make the pen a decent size, changes the colour of the turtle
    to an erasor pink, and changes the pen colour to white
    """
    JIM.pensize(10)
    JIM.color("#e75480")
    JIM.pencolor("white")


ERASOR_BUTTON = Button(SETTINGS, command=erasor, text="Erasor", fg="white", bg="gray")
ERASOR_BUTTON.pack(side=TOP)


def submit_pensize():
    """Update the pen size from the spinbox."""
    JIM.pensize(int(PENSIZE_SB.get()))


PENSIZE_FRAME = Frame(SETTINGS, bg="black")
PENSIZE_SB = Spinbox(PENSIZE_FRAME, from_=1, to=50, width=5)
SUBMIT_PENSIZE_BUTTON = Button(PENSIZE_FRAME, command=submit_pensize, bg="gray",
                               fg="white", text="Pensize")

PENSIZE_SB.grid(column=1, row=1)
SUBMIT_PENSIZE_BUTTON.grid(column=2, row=1, padx=5, pady=10)
PENSIZE_FRAME.pack(side=TOP)


def export():
    """Export the file."""
    filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                 filetypes=(("ps files", "*.ps"), ("all files", "*.*")))
    box.showinfo("Export to another file type", "You can use a program "
                                                "called Ghostscript to convert the file.")


EXPORT_FRAME = Frame(SETTINGS)
EXPORT_BUTTON = Button(EXPORT_FRAME, bg="gray", fg="white", text="Export", command=export)
END_PROGRAM_BUTTON = Button(EXPORT_FRAME, command=end, bg="red", fg="black", text="End Program")

EXPORT_BUTTON.grid(column=1, row=1, padx=10, pady=15)
END_PROGRAM_BUTTON.grid(column=2, row=1, padx=15, pady=15)
EXPORT_FRAME.pack(side=TOP)

flag = 0


def up():
    """Move the turtle a set distance up."""
    JIM.setheading(90)
    JIM.forward(100)


def down():
    """Move the turtle a set distance down."""
    JIM.setheading(270)
    JIM.forward(100)


def left():
    """Move the turtle a set distance left."""
    JIM.setheading(180)
    JIM.forward(100)


def right():
    """Move the turtle a set distance right."""
    JIM.setheading(0)
    JIM.forward(100)


def dragging(x, y):
    """Pull the turtle around to draw."""
    JIM.ondrag(None)
    # makes the turtle follow the mouse
    JIM.goto(x, y)
    # makes function recursive
    JIM.ondrag(dragging)


def clear(x, y):
    """Clear the canvas."""
    JIM.clear()


def change(x, y):
    """Lift the turtle's pen up easily with the right mouse button."""
    global flag
    if flag == 1:
        flag = 0
        JIM.pendown()
    else:
        JIM.penup()
        flag += 1


turtle.listen()
# 1 is left mouse button, 2 is middle, and 3 is right
JIM.ondrag(dragging)
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
