import tkinter
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk 

def submit ():
    if combo.get() == iteams[0]:
        try:
            mile = entry_int.get()
        except UnboundLocalError:
            frame_entry.delete(0, END)
            frame_entry.insert(0, 0)
            output_string.set("Error")
        except tkinter.TclError:
            frame_entry.delete(0, END)
            frame_entry.insert(0, 0)
            output_string.set("Erorr")
        else:
            mile = entry_int.get()
            meter_out = mile * 1.609
            output_string.set(f"Miles to Meter \n {meter_out}M")
            label.config(text="Units convert", fg="white")
    elif combo.get() == iteams[1]:
        try:
            mile = entry_int.get()
        except UnboundLocalError:
            frame_entry.delete(0, END)
            frame_entry.insert(0, 0)
            output_string.set("Error")
        except tkinter.TclError:
            frame_entry.delete(0, END)
            frame_entry.insert(0, 0)
            output_string.set("Error")
        else:
            mile = entry_int.get()
            km_out = mile * 1.61
            output_string.set(f"Miles to kielometer \n {km_out}Km")
            label.config(text="Units convert", fg="white")
    elif combo.get() == iteams[2]:
        try:
            mile = entry_int.get()
        except UnboundLocalError:
            frame_entry.delete(0, END)
            frame_entry.insert(0, 0)
            output_string.set("Error")
        except tkinter.TclError :
            frame_entry.delete(0, END)
            frame_entry.insert(0, 0)
            output_string.set("Error")
        else:
            mile = entry_int.get()
            inch_out = mile * 63.360
            output_string.set(f"Miles to inch \n {inch_out}inch")
            label.config(text="Units convert", fg="white")

window = ttk.Window(themename="darkly")
window.title("Units convertor")
window.geometry("380x150")

label = tk.Label(master=window, text="Units convert", font="Arial 18 bold", fg="blue")
label.pack()
frame = tk.Frame(master=window, )
frame.pack()
entry_int = tk.IntVar()
frame_entry = ttk.Entry(master=frame, textvariable=entry_int)
frame_entry.pack(side="left", padx=5)
iteams = ("mile to meter","mile to kielometer ","inch")
combo_value = ttk.StringVar(value=iteams[0])
combo = ttk.Combobox(frame,values=iteams,textvariable=combo_value)
combo.pack(side="left",padx=5)

submit_button = ttk.Button(window,text="submit",width=20,command=submit)
submit_button.pack(pady=10)

output_string = tk.StringVar()
outbut_label = tk.Label(master=window, textvariable=output_string, font="Arial 16 bold")
outbut_label.pack()


window.mainloop()