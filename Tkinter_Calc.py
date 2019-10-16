
import tkinter as tk

window = tk.Tk()

def HandleClick(btnval):
    val = 0
    if btnval == '=':
        val = eval(exp.get())
    elif btnval == 'c':
        val = ''
    else:
        val = exp.get() + btnval
    exp.set(val)

exp = tk.StringVar()

tk.Label(window, textvariable=exp).grid(row=0, column=0, columnspan=3)
# handleclick is now wrapped in another function which is lambda which takes no input, if a lambda function takes input then its syntax is like = lambda x: print(2*x)
tk.Button(window, text='7', width=5, height=2, command=lambda: HandleClick('7')).grid(row=1, column=0)
tk.Button(window, text='8', width=5, height=2, command=lambda: HandleClick('8')).grid(row=1, column=1)
tk.Button(window, text='9', width=5, height=2, command=lambda: HandleClick('9')).grid(row=1, column=2)
tk.Button(window, text='/', width=5, height=2, command=lambda: HandleClick('/')).grid(row=1, column=3)
tk.Button(window, text='4', width=5, height=2, command=lambda: HandleClick('4')).grid(row=2, column=0)
tk.Button(window, text='5', width=5, height=2, command=lambda: HandleClick('5')).grid(row=2, column=1)
tk.Button(window, text='6', width=5, height=2, command=lambda: HandleClick('6')).grid(row=2, column=2)
tk.Button(window, text='*', width=5, height=2, command=lambda: HandleClick('*')).grid(row=2, column=3)
tk.Button(window, text='1', width=5, height=2, command=lambda: HandleClick('1')).grid(row=3, column=0)
tk.Button(window, text='2', width=5, height=2, command=lambda: HandleClick('2')).grid(row=3, column=1)
tk.Button(window, text='3', width=5, height=2, command=lambda: HandleClick('3')).grid(row=3, column=2)
tk.Button(window, text='-', width=5, height=2, command=lambda: HandleClick('-')).grid(row=3, column=3)
tk.Button(window, text='.', width=5, height=2, command=lambda: HandleClick('.')).grid(row=4, column=0)
tk.Button(window, text='0', width=5, height=2, command=lambda: HandleClick('0')).grid(row=4, column=1)
tk.Button(window, text='=', width=5, height=2, command=lambda: HandleClick('=')).grid(row=4, column=2)
tk.Button(window, text='+', width=5, height=2, command=lambda: HandleClick('+')).grid(row=4, column=3)
tk.Button(window, text='c', width=5, height=2, command=lambda: HandleClick('c')).grid(row=0, column=3)


window.mainloop()