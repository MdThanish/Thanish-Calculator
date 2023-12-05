import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Thanish Calculator")  # Update the title

# Entry widget for input and display
entry = tk.Entry(window, width=20, font=('Arial', 24), bd=10, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=6, height=3, font=('Arial', 14), command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Special case for '=' button
tk.Button(window, text='=', width=6, height=3, font=('Arial', 14), command=calculate).grid(row=5, column=3)

# Special case for 'C' button
tk.Button(window, text='C', width=6, height=3, font=('Arial', 14), command=clear_entry).grid(row=5, column=0)

# Adjust the window size
window.geometry("400x600")  # Change the size as needed

try:
    # Run the main loop
    window.mainloop()
except KeyboardInterrupt:
    print("Program stopped by user")
    window.destroy()
