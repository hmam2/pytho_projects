from tkinter import *
window =Tk() #instantiate an instance of a window
 
window.title('the first window')

window.geometry("420x420")

icon = PhotoImage(file = 'images.png')
window.iconphoto(True,icon)
window.mainloop() # place window on the computer screen .listen to events 
window.config(background= "Blue")
#GUI WINDOWS 

#widjets  : GUI elements = buttons,textboxs,lables,image
#widows : searves as a container to hold o contain these widjets 
