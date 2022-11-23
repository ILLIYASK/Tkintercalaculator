import tkinter


window=tkinter.Tk()
window.geometry('800x650')
window.title('Calculator'.center(230))
window.config(bg='black')
lb=tkinter.Label(window,height=9,width=105,text='this is label',bg='#d8dee8',anchor="se")
lb.place(x=30,y=30,)
window.mainloop()