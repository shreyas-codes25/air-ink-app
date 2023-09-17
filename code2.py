import tkinter as tk
from tkinter import ttk

# Define functions for button clicks
def button1_clicked():
    print("Button 1 was clicked!")
    
def button2_clicked():
    print("Button 2 was clicked!")

# Create the GUI window
root = tk.Tk()

# Set the window title and size
root.title("Two-Button GUI")
root.geometry("300x100")

# Create a style for the buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))

# Create the buttons
button1 = ttk.Button(root, text="Button 1", command=button1_clicked)
button2 = ttk.Button(root, text="Button 2", command=button2_clicked)

# Add the buttons to the window
button1.pack(side="left", padx=10, pady=10)
button2.pack(side="right", padx=10, pady=10)

# Run the GUI loop
root.mainloop()