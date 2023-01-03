from tkinter import *

window = Tk()
window.title("This is your calculator:")

bg_color = str(input("Choose a color: "))
entry_widget = Entry(window, width=30, borderwidth=5)
entry_widget.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def button_click(number): #funcion that makes the buttons do somehting
    current = entry_widget.get()  #what is currently in the entry widget
    entry_widget.delete(0, END)
    entry_widget.insert(0,str(current) + str(number))

def button_clear(): #clear button
    entry_widget.delete(0, END)

def button_add(): #puts the first number before pressing + in memory with global variable
    first_number = entry_widget.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "addition"
    entry_widget.delete(0, END)

def button_subtract():
    first_number = entry_widget.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "subtraction"
    entry_widget.delete(0, END)

def button_multiply():
    first_number = entry_widget.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "multiplication"
    entry_widget.delete(0, END)

def button_divide():
    first_number = entry_widget.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "division"
    entry_widget.delete(0, END)

def button_equal():
    second_number = entry_widget.get()
    entry_widget.delete(0, END)
    if math == "addition":
        entry_widget.insert(0, int(second_number) + f_num)
    if math == "subtraction":
        entry_widget.insert(0, f_num - int(second_number))
    if math == "multiplication":
        entry_widget.insert(0, int(second_number) * f_num)
    if math == "division":
        entry_widget.insert(0, f_num / int(second_number))

#define buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1), bg=bg_color)
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2), bg=bg_color)
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3), bg=bg_color)
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4), bg=bg_color)
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5), bg=bg_color)
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6), bg=bg_color)
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7), bg=bg_color)
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8), bg=bg_color)
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9), bg=bg_color)
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0), bg=bg_color)


button_add = Button(window, text="+", padx=39, pady=20, command=button_add, bg=bg_color)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_equal, bg=bg_color)
button_clear = Button(window, text="CLEAR", padx=79, pady=20, command=button_clear, bg=bg_color)
button_subtract = Button(window, text="-", padx=40.5, pady=20, command=button_subtract, bg=bg_color)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_multiply, bg=bg_color)
button_divide = Button(window, text="/", padx=41, pady=20, command=button_divide, bg=bg_color)

#adding the buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

window.mainloop()
