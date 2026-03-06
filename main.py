import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World")
root.geometry("300x200")

# Create a label with "hello world!"
label = tk.Label(root, text="hello world!", font=("Arial", 20))
label.pack(expand=True)

# Run the application
root.mainloop()
