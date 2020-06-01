from tkinter import *
root = Tk()

global v

def validate(v, inp):
   global value
   if inp.isdigit():
       print(v)
       return True
   elif inp == "":
       print(inp)
       return False
   else:
       print(inp)
       return False

value = DoubleVar



entry1 = Entry(root, textvariable=value)
entry1.grid(row=0, column=0)

reg = root.register(validate)
entry1.config(validate="key", validatecommand=(reg, "%v", "%P"))

label1 = Label(root, text=value)
label1.grid(row=1, column=0)


mainloop()
