from tkinter import *

root = Tk()

a = DoubleVar()
b = IntVar()

def number(x, y):
    print(round(x.get(), y.get()))



entry = Entry(root, textvariable=a)
entry.grid(row=0, column=0)

entry2 = Entry(root, textvariable=b)
entry2.grid(row=1, column=0)

button = Button(root, text="Click Me", command=lambda:[number(a, b)])
button.grid(row=2, column=0)

label = Label(root, textvariable=a)
label.grid(row=3, column=0)

mainloop()
