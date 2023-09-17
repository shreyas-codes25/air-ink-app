import tkinter as tk
from tkinter import ttk
import os
import Gesture_Controller as gs
import AirCanvasDemo as ac

# Define colors
BLACK = "#000000"
WHITE = "#FFFFFF"
NEON_BLUE = "#57CBE0"

window = tk.Tk()

# Define button style
style = ttk.Style()
style.configure("Neon.TButton", background=BLACK, foreground=WHITE, bordercolor=NEON_BLUE, font=("Helvetica", 14, "bold"), width=15)

def button1_click():
    ac.startApp()
    
def button2_click():
    gs.gestureCont()

def button3_click():
    window.destroy()

# Create buttons with neon style
button1 = ttk.Button(window, text="Air Canvas", command=button1_click, style="Neon.TButton")
button2 = ttk.Button(window, text="Mouse Control", command=button2_click, style="Neon.TButton")
button3 = ttk.Button(window, text="Close", command=button3_click, style="Neon.TButton")
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

window.mainloop()
