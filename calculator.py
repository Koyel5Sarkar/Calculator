import tkinter as tk

def update_preview(event=None):
    text = display.get()
    if not text or text[-1] in "+-*/.":
        preview.config(text="")
        return
    try:
        preview.config(text=str(eval(text)))
    except:
        preview.config(text="")

def add(char):
    display.insert(tk.END, char)
    update_preview()

def clear():
    display.delete(0, tk.END)
    preview.config(text="")

def equals():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        preview.config(text="")
    except:
        preview.config(text="Error")

def backspace():
    current = display.get()
    if current:
        display.delete(len(current)-1, tk.END)
        update_preview()


root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")

btn_font = ("Arial", 14)

# Display
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=0)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=(5, 0))

preview = tk.Label(root, font=("Arial", 12), fg="gray", anchor="e")
preview.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5)

# Buttons layout
buttons = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("+", 5, 2),
]

for text, r, c in buttons:
    tk.Button(
        root,
        text=text,
        font=btn_font,
        command=lambda t=text: add(t)
    ).grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

# Special buttons
clear_button=tk.Button(root, text="C", font=btn_font, bg="red", fg="white",
          command=clear).grid(row=6, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)

equal_button=tk.Button(root, text="=", font=btn_font,
          command=equals).grid(row=6, column=2, columnspan=2, sticky="nsew", padx=2, pady=2)

del_button=tk.Button(root,text="DEL", font=btn_font, bg="grey",command=backspace).grid(row=5,column=3,sticky="nsew",padx=2,pady=2)

# Grid configuration
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
