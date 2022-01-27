import tkinter
from tkinter import *
from turtle import width
y = 0
x = 0
z = 1
currentcolor = "black"

window = tkinter.Tk()

for a in range (0,10):
    if z == 0:
        z = 1
    else:
        z = 0
    for b in range (0,10):
        if z == 0:
            currentcolor = "black"
            z = 1
        else:
            currentcolor = "white"
            z = 0
        canvastile = tkinter.Canvas(window,width=50,height=50,bg=currentcolor)
        canvastile.grid(row=y, column=x)
        x +=1
    x = 0
    y +=1


window.mainloop()