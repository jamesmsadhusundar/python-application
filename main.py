from tkinter import *
from tkinter import ttk
from time import *

window = Tk() # initiate window

window.geometry("1000x400")
window.title(" PEACE !")
window.config(background="#61abaa")

icon = PhotoImage(file = 'img.png')

def update():
    time = strftime("%I:%M:%S %p")
    timelabel.config(text = time)
    timelabel.after(1000,update)

    day = strftime("%A")
    daylabel.config(text=day)

    date = strftime("%B %d, %Y")
    datelabel.config(text=date)

timelabel = Label(window, font = ("arial",21,'bold','italic'), fg = "white", bg = "#61abaa", )
timelabel.pack()

daylabel = Label(window, font = ("Ink Free",16,'bold','italic'), fg = "white", bg = "#61abaa")
daylabel.pack()

datelabel = Label(window, font = ("Ink Free",21,'bold','italic'), fg = "white", bg = "#61abaa")
datelabel.pack()

update()

window.iconphoto('true',icon)

window.mainloop() # displays the window
