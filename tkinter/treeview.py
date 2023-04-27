from tkinter import * 
from tkinter import ttk 
import tkinter as tk 
from random import choice



window = tk.Tk()
fisrt_name = ["Ahmed","Mohammed","Ibrahem", "Fuad","Naser","Marah","Hamam"]
last_name = ["hellp","ibrahem","Ahmed","Khaled","Mahmmoud","Shreef","Ibrahem"]
window.geometry("600x400")
threeview = ttk.Treeview(window,columns=("First", "Last", "email"),show="headings")
threeview.heading("First", text= "First name")
threeview.heading("Last", text= "Last name")
threeview.heading("email", text= "Email")

for i in range(100) : 
    first = choice(fisrt_name)
    last  = choice(last_name)
    email = f"{first}{last}@gmail.com"
    data =(first,last,email)
    threeview.insert(parent="",index=0,values=data,)
threeview.pack(fill= "both",expand="True")


#delete iteams 
def deltet_func(_):
    for i in threeview.selection():
        threeview.delete(i)
threeview.bind("<Delete>",deltet_func)
window.mainloop()


def deltet_func(_):
    for i in threeview.selection():
        threeview.delete(i)
threeview.bind("<Backspace>",deltet_func)
window.mainloop()

#selecion 
def selection():
    for i in threeview.selection():
        print(threeview.item(i)["values"])
threeview.bind("<<TreeviewSelect>>",selection)