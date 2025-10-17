import tkinter as tk

# Function to update expression
def press(key):
    entry_text.set(entry_text.get() + str(key))

# Function to evaluate expression
def equalpress():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("Error")

# Function to clear
def clear():
    entry_text.set("")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry_text = tk.StringVar()

# Input field
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 18), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=equalpress)
    else:
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: press(t))
    b.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=23, height=2, font=("Arial", 14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()