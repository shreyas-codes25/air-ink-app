import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os
import Gesture_Controller as gs
import AirCanvasDemo as ac

# Define colors
BLACK = "#000000"
WHITE = "#FFFFFF"
NEON_RED = "#FF0000"
NEON_ORANGE = "#FFA500"
NEON_PINK = "#FF00FF"

window = tk.Tk()

# Set window properties
window.geometry("500x500-1+0")
window.title("Air Ink")
window.resizable(False, False)

# Add background image
bg_image = Image.open("C:/project/image1.jpg")
bg_image = bg_image.resize((600, 600))
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Define button style
style = ttk.Style()
style.configure("Neon.TButton", background=BLACK, foreground=NEON_RED, font=("Helvetica", 16, "bold"), width=20, height=3)
style.map("Neon.TButton", foreground=[("active", NEON_RED), ("pressed", NEON_PINK)], background=[("active", NEON_PINK), ("pressed", NEON_ORANGE)], bordercolor=[("active", NEON_ORANGE), ("pressed", NEON_RED)])

def button1_click():
    window.iconify()
    ac.startApp()

def button2_click():
    window.iconify()
    gs.gestureCont()

def button3_click():
    window.destroy()

def button4_click():
    os.startfile("C:/project/How To Use AirCanvas.pdf")
def button5_click():
    os.startfile("C:/project/How To Use Virtual Mouse.pdf")

# Create label with italic bold font
label = tk.Label(window, text="WELCOME TO AIRINK", font=("Helvetica", 20, "italic bold"), fg=NEON_RED, bg=BLACK)
label.pack(pady=20)

# Create buttons with neon style and increased width and height
button1 = ttk.Button(window, text="Air Canvas", command=button1_click, style="Neon.TButton")
button2 = ttk.Button(window, text="Virtual Mouse", command=button2_click, style="Neon.TButton")
button3 = ttk.Button(window, text="Close", command=button3_click, style="Neon.TButton")
button4 = ttk.Button(window, text="Air Canvas Tutorial", command=button4_click, style="Neon.TButton")
button5 = ttk.Button(window,text='Virtual Mouse Tutorial',command=button5_click,style='Neon.TButton')
button4.pack(pady=10)
button1.pack(pady=10)
button5.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

window.mainloop()
