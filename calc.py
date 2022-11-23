import tkinter

# window

window=tkinter.Tk()
window.geometry('800x700')
window.title('Calculator'.center(230))
window.config(bg='black')

# label

lb=tkinter.Label(window,height=7,width=105,text='this is label',bg='white',anchor="se")
lb.place(x=30,y=30,)


# control buttons

buttce=tkinter.Button(window,text='CE',bg='gray',width=10,height=4,activebackground='#62bce3')
buttce.place(x=30,y=180)
buttc=tkinter.Button(window,text='C',bg='gray',width=10,height=4,activebackground='#62bce3')
buttc.place(x=160,y=180)
buttx=tkinter.Button(window,text='X',bg='gray',width=10,height=4,activebackground='#62bce3')
buttx.place(x=290,y=180)

# number buttons

butt7=tkinter.Button(window,text='7',bg='gray',width=10,height=4,activebackground='#62bce3')
butt7.place(x=30,y=280)
butt8=tkinter.Button(window,text='8',bg='gray',width=10,height=4,activebackground='#62bce3')
butt8.place(x=160,y=280)
butt9=tkinter.Button(window,text='9',bg='gray',width=10,height=4,activebackground='#62bce3')
butt9.place(x=290,y=280)
butt4=tkinter.Button(window,text='4',bg='gray',width=10,height=4,activebackground='#62bce3')
butt4.place(x=30,y=380)
butt5=tkinter.Button(window,text='5',bg='gray',width=10,height=4,activebackground='#62bce3')
butt5.place(x=160,y=380)
butt6=tkinter.Button(window,text='6',bg='gray',width=10,height=4,activebackground='#62bce3')
butt6.place(x=290,y=380)
butt1=tkinter.Button(window,text='1',bg='gray',width=10,height=4,activebackground='#62bce3')
butt1.place(x=30,y=480)
butt2=tkinter.Button(window,text='2',bg='gray',width=10,height=4,activebackground='#62bce3')
butt2.place(x=160,y=480)
butt3=tkinter.Button(window,text='3',bg='gray',width=10,height=4,activebackground='#62bce3')
butt3.place(x=290,y=480)
butt0=tkinter.Button(window,text='0',bg='gray',width=10,height=4,activebackground='#62bce3')
butt0.place(x=30,y=580)
butt_dot=tkinter.Button(window,text='.',bg='gray',width=10,height=4,activebackground='#62bce3')
butt_dot.place(x=160,y=580)

# operator buttons

butt_equal=tkinter.Button(window,text='=',bg='green',width=29,height=4,activebackground='white')
butt_equal.place(x=290,y=580)
butt_div=tkinter.Button(window,text='/',bg='gray',width=10,height=4,activebackground='#62bce3')
butt_div.place(x=420,y=180)
butt_mult=tkinter.Button(window,text='*',bg='gray',width=10,height=4,activebackground='#62bce3')
butt_mult.place(x=420,y=280)
butt_sub=tkinter.Button(window,text='-',bg='gray',width=10,height=4,activebackground='#62bce3')
butt_sub.place(x=420,y=380)
butt_add=tkinter.Button(window,text='9',bg='gray',width=10,height=4,activebackground='#62bce3')
butt_add.place(x=420,y=480)

window.mainloop()
