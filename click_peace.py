from tkinter import *

window = Tk()
window.geometry('300x200')
window.title("Peace Clicker")

count = 0
def count_peace():
    global count
    count += 1
    label ["text"] = "you clicked " + str(count) + " times."

btn = Button(window, text = "click Peace", padx = '40', pady = '40', font = ("ink free", '20'), bg = "black", fg = "white", command = count_peace)
btn.pack()

label = Label(window, text = "you clicked ?", fg = "black", font = ("ink free", '20'), pady = '15')
label.pack()

window.mainloop()