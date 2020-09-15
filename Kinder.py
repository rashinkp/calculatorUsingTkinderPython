from tkinter import *

window = Tk()
window.geometry("245x270")
window.title("RAX")
window.config(bg='gray')




number = 0

button1 = Button(text="1", width=4, height=2, bg="red", fg='green', command=number)
button2 = Button(text="2", width=4, height=2, bg="red", fg='green', command=number)
button3 = Button(text="3", width=4, height=2, bg="red", fg='green', command=number)
button4 = Button(text="4", width=4, height=2, bg="red", fg='green', command=number)
button5 = Button(text="5", width=4, height=2, bg="red", fg='green', command=number)
button6 = Button(text="6", width=4, height=2, bg="red", fg='green', command=number)
button7 = Button(text="7", width=4, height=2, bg="red", fg='green', command=number)
button8 = Button(text="8", width=4, height=2, bg="red", fg='green', command=number)
button9 = Button(text="9", width=4, height=2, bg="red", fg='green', command=number)
button0 = Button(text="0", width=4, height=2, bg="red", fg='green', command=number)
button_equla = Button(text="=", width=4, height=2, bg="red", fg='green', command=number)
button_plus = Button(text="+", width=4, height=2, bg="red", fg='green', command=number)
button_sub = Button(text="-", width=4, height=2, bg="red", fg='green', command=number)
button_multi = Button(text="x", width=4, height=2, bg="red", fg='green', command=number)
button_divition = Button(text="/", width=4, height=2, bg="red", fg='green', command=number)
button_dote = Button(text=".", width=4, height=2, bg="red", fg='green', command=number)
button_clear = Button(text="C", width=4, height=2, bg="red", fg='green', command=number)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_equla.grid(row=5, column=0)
button_sub.grid(row=2, column=3)
button_multi.grid(row=3, column=3)
button_divition.grid(row=4, column=3)
button_plus.grid(row=1, column=3)
button_dote.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

label = Label(window, text=number, bg='green', fg='blue')
label.grid(row=0, column=0)




window.mainloop()
