"""⚛⛮ POWERED BY||SALEH AMO||DIGITAL_CLOCK CLOCK⚛ β"""
from tkinter import Label, Tk 
import time
app_window = Tk() 
app_window.title("Digital Clock||SALEH AMOO") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

text_font= ("Boulder", 36, 'bold')
background = "#87CEFA"
foreground= "#191970"
border_width = 41

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()