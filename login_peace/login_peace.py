from tkinter import *

def delete():
    name.delete(0, END)
    password.delete(0,END)

def submit():
    get_name = name.get()
    get_pin = password.get()
    print(get_name)
    print(get_pin)

window = Tk()
window.title("login peace")

icon = PhotoImage(file = 'smily.png')
window.iconphoto('true',icon)

name = Entry(window, font = ('arial', 22), bg = "black", fg = "#0722ed")
name.pack(side = LEFT)

password = Entry(window, font = ('arial', 22), bg = "black", fg = "#0722ed", show = "*")
password.pack(side = LEFT)

submit = Button(window, text = "Submit", command = submit)
submit.pack(side = RIGHT)

delete = Button(window, text = "Delete", command = delete)
delete.pack(side = RIGHT)

window.mainloop()