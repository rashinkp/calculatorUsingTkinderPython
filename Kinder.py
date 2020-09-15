from tkinter import *

window = Tk()
window.geometry("245x270")
window.title("RAX")
window.config(bg='gray')

calcultor_display = Label()


def digit(var):
    print(var)


button1 = Button(window, text="1", commant=digit(1))

button1.grid(row=1, column=0)
button1.pack()
calcultor_display.pack()

window.mainloop()
