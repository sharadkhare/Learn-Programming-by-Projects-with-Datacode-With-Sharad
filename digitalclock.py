# Digital Clock with Python
# In this section, I will show you how to create a digital clock using python. This is a simple task to get started with the Tkinter library in Python, which is a built-in package that comes with Python. Tkinter has some cool features that can be used to build simple apps.

from tkinter import Label, Tk, font
import time
app_window = Tk()
app_window.title("Digital Clock by Sharad Khare")
app_window.geometry("420x150")
app_window.resizable(1,1)
text_font = ("Boulder", 70, 'bold')
background = "#f2bc07"
foreground = "#363634"
border_width = 25

label = Label(app_window, font = text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)
    
digital_clock()
app_window.mainloop()