from tkinter import *
import tkinter as tk 
from tkinter import ttk
window = tk.Tk()
window.geometry("800x800")
#canves : 
canve = tk.Canvas(window,bg = "white")
canve.grid(row=0,column=0)

#canve.create_rectangle((left,top,right,bottom))
canve.create_rectangle((50,20,200,200))


#canve.create_polygon((x1,y1,x2,y2,x3,y3))
#canve.create_polygon((50,20,120,200,200,20),fill="blue")

#canve.create_oval((left,top,right,bottom))
canve.create_oval((50,20,200,200),fill= "yellow")


#canve.create_line((start_x, start_y, end_x , end_y))
canve.create_line((50, 20, 200 , 200),fill= "red")


canve.create_text((122,220),text="the first canve",font="Arial 16 bold",fill = "green")

canve.create_arc((50,20,200,200),fill = "red", start = 45 , extent = 140, style = tk.PIESLICE)
 
window.mainloop() 