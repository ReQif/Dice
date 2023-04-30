import tkinter
import turtle
import random
import ttkbootstrap

window = tkinter.Tk()
window.title("Dice")
window.geometry("300x300")
window.resizable(width=False,height=False)
# window.iconbitmap("favicon.ico") Add own icon of application

canvas = tkinter.Canvas(window, width=200, height=200)
canvas.pack()
turtle = turtle.RawTurtle(canvas)
global draw

# commands

def roll_dice():
    draw.config(state="disabled")
    turtle.clear()
    random.seed()
    return random.randint(1,6)
    

def draw_dots(n):
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.pensize(1)
    turtle.color("black")
    turtle.penup()
    
    if n == 1:
        draw_dot(-5, 5)
    elif n == 2:
        draw_dot(-30, 30)
        draw_dot(30, -30)
    elif n == 3:
        draw_dot(0, 0)
        draw_dot(-30, 30)
        draw_dot(30, -30)
    elif n == 4:
        draw_dot(-30, 30)
        draw_dot(30, -30)
        draw_dot(-30, -30)
        draw_dot(30, 30)
    elif n == 5:
        draw_dot(0, 0)
        draw_dot(-30, 30)
        draw_dot(30, -30)
        draw_dot(-30, -30)
        draw_dot(30, 30)
    elif n == 6:
        draw_dot(-30, 30)
        draw_dot(30, -30)
        draw_dot(-30, 0)
        draw_dot(30, 0)
        draw_dot(-30, -30)
        draw_dot(30, 30)

def draw_dot(x, y):
    turtle.goto(x, y)
    turtle.dot(20)

def animate_dice():
    for i in range(1):
        n = roll_dice()
        draw_dots(n)
    draw.config(state="enable")
    label_dots(n)
    
def label_dots(n):
    dots_label.configure(text="Dots: " + str(n))

def exit():
    window.destroy()

# Buttons and labels
dots_label = ttkbootstrap.Label(window,text="Dots: 0")
dots_label.pack()
draw = ttkbootstrap.Button(bootstyle="success",text="Roll Dice",command=animate_dice)
draw.pack()
exitt = ttkbootstrap.Button(bootstyle="danger",text="Exit",command=exit)
exitt.place(x=150,y=280,anchor='center')
label_dots(0)
window.mainloop()
