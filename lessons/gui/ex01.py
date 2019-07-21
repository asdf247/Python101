import tkinter as tk

# Create blank window
root = tk.Tk()

# Create elements for the window
w = tk.Label(root, text="Hello Tkinter!")

# Pack them
w.pack()

# Run window
root.mainloop()