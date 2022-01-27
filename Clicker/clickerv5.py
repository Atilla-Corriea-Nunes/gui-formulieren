import tkinter
import random
from tkinter import *
import time

lastButtonWas = "nothing"
wonitem = ""
counter = 0

def autoClicker():
    global counterx
    if cb.get() == 0:
        pass
    else:
        if lastButtonWas == "up":
            counter += 1
            l.configure(text=counter)
        elif lastButtonWas == "down":
            counter -= 1
            l.configure(text=counter)
    window.after(200,autoClicker)

def multiplyOrDevide(event):
    global counter, lastButtonWas
    if lastButtonWas == "up":
        counter *= 4
        l.configure(text=counter)
    elif lastButtonWas == "down":
        counter /= 3
        l.configure(text=counter)
    pass

def makeyellow(event):
    window.configure(bg="yellow")

def changeback(event):
    if counter >= 1:
        window.configure(bg="green")
    elif counter == 0:
        window.configure(bg="grey")
    elif counter <= -1:
        window.configure(bg="red")
        

def countUp():
    global counter, lastButtonWas
    counter += 1
    lastButtonWas = "up"
    l.configure(text=counter)
    if counter >= 1:
        window.configure(bg="green")
    elif counter == 0:
        window.configure(bg="grey")
    elif counter <= -1:
        window.configure(bg="red")
    cb2['state'] = tkinter.NORMAL
    cb2.configure(text="Autoclicker")

def countEventUp(event):
    countUp()

def countEventDown(event):
    countDown()

def countDown():
    global counter, lastButtonWas
    counter -= 1
    lastButtonWas = "down"
    l.configure(text=counter)
    if counter >= 1:
        window.configure(bg="green")
    elif counter == 0:
        window.configure(bg="grey")
    elif counter <= -1:
        window.configure(bg="red")
    cb2['state'] = tkinter.NORMAL
    cb2.configure(text="Autoclicker")



window = tkinter.Tk()
window.configure(bg="grey")
window.geometry("520x300")

u = tkinter.Button(window)
u.configure(text="Up", command=countUp,padx=140, pady=12)


l = tkinter.Label(text=counter, padx=145, pady=12)
l.bind("<Enter>", makeyellow)
l.bind("<Leave>", changeback)
l.bind("<Double-Button-1>", multiplyOrDevide)
window.bind("<Up>", countEventUp ) 
window.bind("<+>", countEventUp)
window.bind("<Down>", countEventDown)
window.bind("-", countEventDown)
window.bind("<space>", multiplyOrDevide)



cb = tkinter.IntVar()
cb2 = tkinter.Checkbutton(window,text="Autoclicker locked",variable=cb, onvalue=1,offvalue=0, command=window.after(200,autoClicker), state=tkinter.DISABLED)

d = tkinter.Button(window)
d.configure(text="Down",command=countDown,padx=132, pady=12)

u.grid(row=0, column=0, pady=25, padx=20)
l.grid(row=1,column=0, pady=25, padx=20)
cb2.grid(row=1, column=1, pady=25, padx=20)
d.grid(row= 2, column=0, pady=25, padx=20)

window.title("Clicker")

window.mainloop()