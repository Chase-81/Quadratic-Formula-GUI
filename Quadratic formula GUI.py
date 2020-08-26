# imports all the necessary library's
from math import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

y_value_list = []
x_value_list = []
# calculates discriminant and clears inputs
def discriminant(a_value, b_value, c_value, round_num):
   try:
        a = a_value.get()
        b = b_value.get()
        c = c_value.get()

        zero_value = a + b + c

        try:
            d = round_num.get()
        except:
            d = 100

        if zero_value != 0:

            if d < 0:
                messagebox.showerror("ERROR", "You can not round to {} decimal places".format(d))
                discriminant_return.set("")
                x_positive.set("")
                x_negative.set("")
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
        else:
            error_message.set("I can not calculate an equation if all inputs are 0")
   except:
       messagebox.showerror("ERROR", "You have to enter one real number in entry field a, b and c.\nIf nothing is entered in the rounding field the results are not rounded.")

# calculates roots of the equation and checks the validity
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

           elif d == 0:
               result = ((-b) + sqrt(value)) / (2 * a)
               x_positive.set(round(result,0))



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

# Clears all values
def clear_all():
    global root, x_value_list, y_value_list
    a_value.set("")
    b_value.set("")
    c_value.set("")
    discriminant_return.set("")
    x_positive.set("")
    x_negative.set("")
    round_num.set("")
    error_message.set("")
    plt.close()
    x_value_list = []
    y_value_list =[]

def graph(a_value, b_value, c_value, discriminant, round_num):
    global y_value_list, x_value_list

    try:
        a = a_value.get()
        b = b_value.get()
        c = c_value.get()
        d = discriminant.get()
        y_value_list = []
        x_value_list = []
        plt.close()
        print("1")

        i=-5

        while i < 5:
            y_value_list.append((a*(i**2)) + (b*i) + c)
            x_value_list.append(i)
            i += 0.5

        if d > 0:
            print("2")
            x_1 = x_positive.get()
            x_2 = x_negative.get()
            plt.grid(b=True, which='major', color='#666666', linestyle=':')
            plt.axhline(y=0, color="#737373", linestyle="--")
            plt.axvline(x=0, color="#737373", linestyle="--")
            plt.annotate('({},{})'.format(x_1,0), xy=(x_1, 0), xytext=(3, -5))
            plt.annotate('({},{})'.format(x_2,0), xy=(x_2, 0), xytext=(-3, 10))
            plt.plot(x_value_list,y_value_list)
            plt.show()

        elif d == 0:
            print(d)
            x_1 = x_positive.get()
            plt.grid(b=True, which='major', color='#666666', linestyle=':')
            plt.axhline(y=0, color="#737373", linestyle="--")
            plt.axvline(x=0, color="#737373", linestyle="--")
            plt.annotate('({},{})'.format(x_1,0), xy=(x_1, 0), xytext=(3, -5))
            plt.plot(x_value_list,y_value_list)
            plt.show()

        elif d < 0:
            print("4")
            plt.grid(b=True, which='major', color='#666666', linestyle=':')
            plt.axhline(y=0, color="#737373", linestyle="--")
            plt.axvline(x=0, color="#737373", linestyle="--")
            plt.plot(x_value_list,y_value_list)
            plt.show()

        else:
            print("Fail")
    except:
        print("test")


# Creates window and input and output frames
root = Tk()
root.title("Quadratic Formula Solver")

input_frame = ttk.LabelFrame(root, text="Inputs")
input_frame.grid(row=2, column=0, sticky="NSEW")

control_frame = ttk.LabelFrame(root, text="Controls")
control_frame.grid(row=3, column=0, sticky="NESW")

output_frame = ttk.LabelFrame(root, text="Output")
output_frame.grid(row=4, column=0, sticky="NSEW")

# variables of program
a_value = DoubleVar()
a_value.set("")
b_value = DoubleVar()
b_value.set("")
c_value = DoubleVar()
c_value.set("")
discriminant_return = DoubleVar()
discriminant_return.set("")
x_positive = DoubleVar()
x_positive.set("")
x_negative = DoubleVar()
x_negative.set("")
error_message = StringVar()
round_num = IntVar()
round_num.set("")
start_slider_var = DoubleVar()
end_slider_var = DoubleVar()


# GUI layout code
statement = ttk.Label(root, text="This calculator can solve quadratic equations in the form ax^2 + bx + c\nEnter the values for a, b, and c")
statement.grid(row=0, column=0, sticky="NSEW")

# Entry labels and entry fields
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


# Buttons
entry_button = ttk.Button(control_frame, text="Submit", command=lambda:[discriminant(a_value, b_value, c_value, round_num), roots(a_value, b_value, c_value, round_num), graph(a_value, b_value, c_value, discriminant_return, round_num)])
entry_button.grid(row=0, column=0)

root.bind('<Return>', lambda event=None: entry_button.invoke())

clear_button = ttk.Button(control_frame, text="Clear all", command=clear_all)
clear_button.grid(row=0, column=1)

root.bind('<Delete>', lambda event=None: clear_button.invoke())


# Output code
discriminant_label = ttk.Label(output_frame, text="Discriminant: ")
discriminant_label.grid(row=0, column=0)

discriminant_value = ttk.Label(output_frame, textvariable=discriminant_return)
discriminant_value.grid(row=0, column=1)

x_label = ttk.Label(output_frame, text="Value for x1:")
x_label.grid(row=1, column=0)

x_value_positive = ttk.Label(output_frame, textvariable=x_positive)
x_value_positive.grid(row=1, column=1)

x_label2 = ttk.Label(output_frame, text="Value for x2:")
x_label2.grid(row=2, column=0)

x_value_negative = ttk.Label(output_frame, textvariable=x_negative)
x_value_negative.grid(row=2, column=1)

error_message_label = ttk.Label(output_frame, textvariable=error_message)
error_message_label.grid(row=3, column=0)

# loops through each item in each frame and applies spacing
for widget in root.winfo_children():
    widget.grid(padx=5, pady=5)

for widget in input_frame.winfo_children():
   widget.grid(padx=10, pady=10)

for widget in control_frame.winfo_children():
    widget.grid(padx=10, pady=10)

for widget in output_frame.winfo_children():
    widget.grid(padx=10, pady=10)

mainloop()
