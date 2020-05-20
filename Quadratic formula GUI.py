#imports all the necessary library's
from math import *
from tkinter import *
from tkinter import ttk

#calculates discriminant and clears inputs if ticked box is ticked
def discriminant():
   global a_value, b_value, c_value
   a = a_value.get()
   b = b_value.get()
   c = c_value.get()
   value = (b ** 2) - (4 * a * c)
   discriminant_return.set(value)

   if clear_var.get() == 1:
       a_value.set("")
       b_value.set("")
       c_value.set("")
       discriminant_return.set("")
       x_negative.set("")
       x_positive.set("")

#calculates roots of the equation and checks the validity
def roots():
   global a_value, b_value, c_value
   a = a_value.get()
   b = b_value.get()
   c = c_value.get()
   value = (b ** 2) - (4 * a * c)

   if value == 0:
       result = ((-b) + sqrt(value)) / (2 * a)
       x_positive.set(result)
       error_message.set("")
   elif value > 0:
       result_positive = ((-b) + sqrt(value)) / (2 * a)
       result_negative = ((-b) - sqrt(value)) / (2 * a)
       x_positive.set(result_positive)
       x_negative.set(result_negative)
       error_message.set("")
   else:
       error_message.set("Error: The discriminant is less than zero, there are no real roots for this equation.")

root = Tk()
root.title("Quadratic Formula Solver")

statement = ttk.Label(root, text="This calculator can solve quadratic equations in the form ax^2 + bx + c\nEnter the values for a, b, and c")
statement.grid(row=0, column=0, sticky="NSEW")

input_frame = ttk.LabelFrame(root, text="Inputs")
input_frame.grid(row=2, column=0, sticky="NSEW")

#variables of program
a_value = DoubleVar()
a_value.set("")
b_value = DoubleVar()
b_value.set("")
c_value = DoubleVar()
c_value.set("")
discriminant_return = DoubleVar()
discriminant_return.set("")
clear_var = IntVar()
clear_var.set(0)
x_positive = DoubleVar()
x_positive.set("")
x_negative = DoubleVar()
x_negative.set("")
error_message = StringVar()



photo_label = Label(root)
photo_label.grid(row=1, column=0, sticky="NSEW")

a_label = ttk.Label(input_frame, text="Enter value for a:")
a_label.grid(row=0, column=0)

a_entry = ttk.Entry(input_frame, textvariable=a_value)
a_entry.grid(row=0, column=1)

b_label = ttk.Label(input_frame, text="Enter value for b:")
b_label.grid(row=1, column=0)

b_entry = ttk.Entry(input_frame, textvariable=b_value)
b_entry.grid(row=1, column=1)

c_label = ttk.Label(input_frame, text="Enter value for c:")
c_label.grid(row=2, column=0)

c_entry = ttk.Entry(input_frame, textvariable=c_value)
c_entry.grid(row=2, column=1)

entry_button = Button(input_frame, text="Submit", command=lambda:[discriminant(), roots()])
entry_button.grid(row= 3, column=0)

clear = ttk.Checkbutton(input_frame, text="Clear when submitted", variable=clear_var)
clear.grid(row=3, column=1)

output_frame = ttk.LabelFrame(root, text="Output")
output_frame.grid(row=3, column=0, sticky="NSEW")

discriminant_label = ttk.Label(output_frame, text="Discriminant: ")
discriminant_label.grid(row=0, column=0)

discriminant_value = ttk.Label(output_frame, textvariable=discriminant_return)
discriminant_value.grid(row=0, column=1)

x_label = ttk.Label(output_frame, text="Value for x1:")
x_label.grid(row=1, column=0)

x_value_positive = ttk.Label(output_frame, textvariable=x_positive, text=",")
x_value_positive.grid(row=1, column=1)

x_label2 = ttk.Label(output_frame, text="Value for x2:")
x_label2.grid(row=2, column=0)

x_value_negative = ttk.Label(output_frame, textvariable=x_negative)
x_value_negative.grid(row=2, column=1)

error_message_label = ttk.Label(output_frame, textvariable=error_message)
error_message_label.grid(row=3, column=0)

for widget in input_frame.winfo_children():
   widget.grid(padx=10, pady=10)

mainloop()
