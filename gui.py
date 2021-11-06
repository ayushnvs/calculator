from tkinter import *

print("Starting GUI...")

root = Tk()
root.title("Ishani's Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def calcs():
    pass

def clear():
    e.delete(0, END)

def Del():
    current = e.get()
    clear()
    e.insert(0, current[:len(current)-1])

def button_click(number):
    current = e.get()
    clear()
    e.insert(0, str(current) + str(number))

button_1 = Button(root, text="1", padx=35, pady=24, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=35, pady=24, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=35, pady=24, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=35, pady=24, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=35, pady=24, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=35, pady=24, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=35, pady=24, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=35, pady=24, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=35, pady=24, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=35, pady=24, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=33, pady=24, command=lambda: add())
button_equal = Button(root, text="=", padx=34, pady=24, command=lambda: button_click())
button_del = Button(root, text="del", padx=30, pady=22, command=lambda: Del())
button_clear = Button(root, text="Clear", padx=69, pady=24, command=lambda: clear())

credit = Label(root, text="Made by Ayush Mishra")
credit.grid(row=6, column=0, columnspan=3)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4, column=0)
button_del.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=0)

root.mainloop()