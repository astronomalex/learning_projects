from tkinter import *
from tkinter.colorchooser import askcolor

def onLeftClick(event):
    print(event.x, event.y, event.widget)
    lab.config(text=(event.x , event.y))

def onMouseMove(event):
    print(event.x, event.y, event.widget)
    lab.config(text=(event.x , event.y))
    mes.config(text=(event.x , event.y))

def selectColor():
    (triple,hcolor) = askcolor()
    lab.config(bg=hcolor)
    butDialogue.config(bg=hcolor)
    print(triple)

labelfont = ('courier', 30,'bold')
win=Tk()
win2=Tk()
win2.geometry('+500+0')
lab=Label(win,text='test....')
lab.config(font=labelfont)
lab.config(bg='orange',fg='blue')
lab.config(height=5, width=20)
lab.bind('<Button-1>',onLeftClick)
lab.bind('<Motion>', onMouseMove)

mes=Message(win2, text='Начните водить мышкой над окном слева')

butDialogue=Button(win2,text='Выберите цвет фона', command = selectColor)

butDialogue.pack(side=BOTTOM)
mes.pack(expand=YES, fill=BOTH)
lab.pack(expand=YES,fill=BOTH)
win.mainloop()