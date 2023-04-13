import tkinter
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk 
def convert ():
    try :
        mile = entry_int.get()
    except UnboundLocalError:
        frame_entry.delete(0,END)
        frame_entry.insert(0,"Error")
        output_string.set("")
    except tkinter.TclError:
        frame_entry.delete(0,END)
        frame_entry.insert(0,"Error")
        output_string.set("")
    else: 
        mile = entry_int.get()
        km_out = mile * 1.61
        output_string.set(f"Miles to Meter \n {km_out}Km")
        label.config(text="Units convert",fg="white")
        

def mile_to_meter():
    try :
        mile = entry_int.get()
    except UnboundLocalError:
       frame_entry.delete(0,END)
       frame_entry.insert(0,"Error")
       output_string.set("")
    except tkinter.TclError:
       frame_entry.delete(0,END)
       frame_entry.insert(0,"Error")
       output_string.set("")
    else: 
        mile = entry_int.get()
        meter_out = mile * 1.609
        output_string.set(f"Miles to Meter \n {meter_out}M")
        label.config(text="Units convert",fg="white")
        
        
            


window = ttk.Window(themename="darkly")
window.title("Units convert")
window.geometry("380x150")

label = tk.Label(master= window,text="Units convert",font= "Arial 18 bold",fg="blue")
label.pack()
frame = tk.Frame(master=window,)
frame.pack()
entry_int = tk.IntVar()
frame_entry = ttk.Entry(master=frame,textvariable=entry_int)
frame_entry.pack(side="left",padx=5)

Button_frame = ttk.Button(master=frame,text="miles to kilometer",command=convert)
Button_frame.pack(side= "left",padx=5)
meter_button = ttk.Button(master = frame,text="mile to meter",command=mile_to_meter)
meter_button.pack(side = "left")
output_string = tk.StringVar()
outbut_label = tk.Label(master=window,textvariable=output_string,font="Arial 16 bold")
outbut_label.pack()

window.mainloop()