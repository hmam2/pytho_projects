import tkinter
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk 
global drawe1
def drawe (event):
    
    canve.create_oval((event.x - brush /2,event.y  - brush /2 ,event.x + brush /2 ,event.y + brush /2),fill="black")
def paint(event):
    canve.create_oval((event.x - brush/2 ,event.y  - brush /2,event.x + brush  /2,event.y + brush /2),fill="black")

    

def brush_size (event):
    global brush
    if event.delta >= 0 :
        brush +=1
    elif event.delta <=0:
        brush -= 1 
    brush = max(0,min(brush_size,50))
brush = 1
def change_screen_color(color):
    canve.config(background= color)
    
def change_screen_size(size):
    canve.config(width=size, height=size)


def delete():
    canve.delete("all")
    
window =tk.Tk()
window.geometry("600x800")
canve = tk.Canvas(window,background = "white",height=700,width=600)
canve.bind("<Button-1>",drawe)
canve.bind("<B1-Motion>", paint)
canve.bind("<MouseWheel>",brush_size)
canve.pack(expand="True",fill="both")

button_frame = Frame(window)
button_frame.pack()
small_button = Button(window, text="Small", command=lambda: change_screen_size(200),font = "Arial  12")
small_button.pack(side=LEFT,padx=5)

medium_button = Button(window, text="Medium", command=lambda: change_screen_size(400),font = "Arial  12")
medium_button.pack(side=LEFT,padx=5)

large_button = Button(window, text="Large", command=lambda: change_screen_size(700),font = "Arial  12")
large_button.pack(side=LEFT,padx=5)
    
red_button = Button(window, text="Red", command=lambda: change_screen_color("red"),font = "Arial  12")
red_button.pack(side=LEFT,padx=5)

blue_button = Button(window, text="Blue", command=lambda: change_screen_color("blue"),font = "Arial  12")
blue_button.pack(side=LEFT,padx=5)
green_button = Button(window, text="Green", command=lambda: change_screen_color("green"),font = "Arial  12")
green_button.pack(side=LEFT,padx=5)



delet_button = Button(window,text = "delete",command=delete,width=515)
delet_button.pack(side = LEFT,padx=5)
window.mainloop()