from tkinter import *
from calculator import Calculator

calc = Calculator()
px, py = (30, 20)

root = Tk()
root.title("Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def working(sign):
    e.insert(0, "0")
    try:
        num = float(e.get())
    except:
        e.insert(0, "Syntax Error")
    clear()
    if calc.operation is None:
        calc.calculation = num
        calc.operation = sign
    elif calc.operation == "+":
        calc.plus(num)
        calc.operation = sign
    elif calc.operation == "-":
        calc.minus(num)
        calc.operation = sign
    elif calc.operation == "*":
        calc.multiply(num)
        calc.operation = sign
    elif calc.operation == "/":
        calc.divide(num)
        calc.operation = sign
    else:
        calc.operation = sign

def equal():
    try:
        working(calc.operation)
    except:
        e.insert(0, "Syntax Error")
    clear()
    e.insert(0, calc.calculation)
    calc.operation = "="

def clear(button_call=False):
    e.delete(0, END)
    if button_call:
        calc.calculation = 0
        calc.operation = None

def Del():
    current = e.get()
    clear()
    e.insert(0, current[:len(current)-1])

def button_click(number):
    if calc.operation == "=":
        clear()
        calc.operation = None
    current = e.get()
    clear()
    e.insert(0, str(current) + str(number))

button_1 = Button(root, text="1", padx=px, pady=py, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=px, pady=py, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=px, pady=py, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=px, pady=py, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=px, pady=py, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=px, pady=py, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=px, pady=py, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=px, pady=py, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=px, pady=py, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=px, pady=py, command=lambda: button_click(0))
button_ = Button(root, text=".", padx=px+2, pady=py, command=lambda: button_click("."))
button_add = Button(root, text="+", padx=px-4, pady=52, command=lambda: working("+"))
button_subtract = Button(root, text="-", padx=px-3, pady=py, command=lambda: working("-"))
button_multiply = Button(root, text="*", padx=px, pady=py, command=lambda: working("*"))
button_divide = Button(root, text="/", padx=px, pady=py, command=lambda: working("/"))
button_equal = Button(root, text="=", padx=px-4, pady=52, command=lambda: equal())
button_del = Button(root, text="del", padx=px-5, pady=py, command=lambda: Del())
button_clear = Button(root, text="clr", padx=px-3, pady=py, command=lambda: clear(True))

credit = Label(root, text="Made by Ayush Mishra")
credit.grid(row=6, column=0, columnspan=4)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5, column=0)
button_.grid(row=5, column=1)

button_add.grid(row=2, column=3, rowspan=2)
button_subtract.grid(row=1, column=3)
button_multiply.grid(row=1, column=2)
button_divide.grid(row=1, column=1)

button_del.grid(row=1, column=0)
button_clear.grid(row=5, column=2)
button_equal.grid(row=4, column=3, rowspan=2)

root.mainloop()