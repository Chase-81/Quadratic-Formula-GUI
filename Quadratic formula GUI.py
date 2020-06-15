#imports all the necessary library's
from math import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#calculates discriminant and clears inputs if ticked box is ticked
def discriminant(a_value, b_value, c_value, round_num):
   try:
        a = a_value.get()
        b = b_value.get()
        c = c_value.get()

        try:
            d = round_num.get()
        except:
            d = 100

        if a and b and c != 0:

            if d < 0:
                messagebox.showerror("ERROR", "You can not round to {} decimal places".format(d))
            elif d == 0:
                value = (b ** 2) - (4 * a * c)
                discriminant_return.set(round(value, 0))
            elif d > 0:
                value = (b ** 2) - (4 * a * c)
                discriminant_return.set(round(value, d))

            elif d == 100:
                value = (b ** 2) - (4 * a * c)
                discriminant_return.set(value)

            else:
                messagebox.showerror("ERROR", "Tha wasn't an option")

            if clear_var.get() == 1:
                a_value.set("")
                b_value.set("")
                c_value.set("")
                discriminant_return.set("")
                x_negative.set("")
                x_positive.set("")
                round_num.set("")
        else:
            error_message.set("I can not calculate an equation if all inputs are 0")
   except:
       messagebox.showerror("ERROR", "You have to enter 1 real number in each entry field")
       print("HI")


#calculates roots of the equation and checks the validity
def roots(a_value, b_value, c_value, round_num):
   try:
       a = a_value.get()
       b = b_value.get()
       c = c_value.get()

       try:
           d = round_num.get()
       except:
           d = 100


       value = (b ** 2) - (4 * a * c)

       if value < 0:
           error_message.set("Your equation doesn't have any real roots")
           pass

       elif value == 0:
           if d < 0:
               pass
           elif d < 0:
               result = ((-b) + sqrt(value)) / (2 * a)
               x_positive.set(round(result, 0))

           elif d > 0:
               result = ((-b) + sqrt(value)) / (2 * a)
               x_positive.set(round(result, d))

           elif d == 100:
               result = ((-b) + sqrt(value)) / (2 * a)
               x_positive.set(result)



       elif value > 0:
           if d < 0:
               pass
           elif d == 0:
               result_positive = ((-b) + sqrt(value)) / (2 * a)
               result_negative = ((-b) - sqrt(value)) / (2 * a)
               x_positive.set(round(result_positive, 0))
               x_negative.set(round(result_negative, 0))
               error_message.set("")
           elif d > 0:
               result_positive = ((-b) + sqrt(value)) / (2 * a)
               result_negative = ((-b) - sqrt(value)) / (2 * a)
               x_positive.set(round(result_positive, d))
               x_negative.set(round(result_negative, d))
               error_message.set("")

           elif d == 100:
               result_positive = ((-b) + sqrt(value)) / (2 * a)
               result_negative = ((-b) - sqrt(value)) / (2 * a)
               x_positive.set(result_positive)
               x_negative.set(result_negative)
               error_message.set("")

           else:
               pass
   except:
       pass

#Clears all values
def clear_all():
    a_value.set("")
    b_value.set("")
    c_value.set("")
    discriminant_return.set("")
    x_positive.set("")
    x_negative.set("")
    round_num.set("")


#Creates window and input and output frames
root = Tk()
root.title("Quadratic Formula Solver")

input_frame = ttk.LabelFrame(root, text="Inputs")
input_frame.grid(row=2, column=0, sticky="NSEW")

control_frame = ttk.LabelFrame(root, text="Controls")
control_frame.grid(row=3, column=0, sticky="NESW")

output_frame = ttk.LabelFrame(root, text="Output")
output_frame.grid(row=4, column=0, sticky="NSEW")

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
round_num = IntVar()
round_num.set("")


#GUI layout code
statement = ttk.Label(root, text="This calculator can solve quadratic equations in the form ax^2 + bx + c\nEnter the values for a, b, and c")
statement.grid(row=0, column=0, sticky="NSEW")

#Entry labels and entry fields
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

round_label = Label(input_frame, text="Enter the value to round answer: ")
round_label.grid(row=3, column=0)

round_entry = ttk.Entry(input_frame, textvariable=round_num)
round_entry.grid(row=3, column=1)

#Buttons and checkbutton
entry_button = ttk.Button(control_frame, text="Submit", command=lambda:[discriminant(a_value, b_value, c_value, round_num), roots(a_value, b_value, c_value, round_num)])
entry_button.grid(row= 0, column=0)

clear = ttk.Checkbutton(control_frame, text="Clear when submitted", variable=clear_var)
clear.grid(row=0, column=1)

clear_button = ttk.Button(control_frame, text="Clear all", command=clear_all)
clear_button.grid(row=0, column=2)

#Output code
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

#loops through each item in each frame and applies spacing
for widget in root.winfo_children():
    widget.grid(padx=5, pady=5)

for widget in input_frame.winfo_children():
   widget.grid(padx=10, pady=10)

for widget in control_frame.winfo_children():
    widget.grid(padx=10, pady=10)

for widget in output_frame.winfo_children():
    widget.grid(padx=10, pady=10)


mainloop()
