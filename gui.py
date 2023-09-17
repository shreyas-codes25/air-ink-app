import tkinter as tk
import os
import Gesture_Controller as gs
import AirCanvasDemo as ac


window = tk.Tk()


def button1_click():
    ac.startApp()
    

def button2_click():
    
    gs.gestureCont()

def button3_click():
    window.destroy()


button1 = tk.Button(window, text="Air Canvas", command=button1_click)
button2 = tk.Button(window, text="Mouse Control", command=button2_click)
button3 = tk.Button(window,text="close",command=button3_click)
button1.pack()
button2.pack()
button3.pack()


window.mainloop()