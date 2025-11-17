import tkinter as tk

def calculate_addition():
    val1 = e1.get()
    val2 = e2.get()

    try:
        num1 = int(val1)
        num2 = int(val2)
    except ValueError:
        print("Please enter valid numbers!")
        return

    total = num1 + num2
    print("Answer:", total)

def calculate_multiplication():
    val1 = e1.get()
    val2 = e2.get()

    try:
        num1 = int(val1)
        num2 = int(val2)
    except ValueError:
        print("Please enter valid numbers!")
        return

    total = num1 * num2
    print("Answer:", total)


root = tk.Tk()
root.title("Input GUI")
root.geometry("300x100")

tk.Label(root, text="First Number").grid(row=0)
tk.Label(root, text="Second Number").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(root, text='Add', command=calculate_addition).grid(row=3, column=0)
tk.Button(root, text='Multiply', command=calculate_multiplication).grid(row=3, column=1)


root.mainloop()