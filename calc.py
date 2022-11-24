import tkinter

# window

window=tkinter.Tk()
window.geometry('530x700')
window.title('Calculator'.center(150))
window.config(bg='black')

# label

lb=tkinter.Label(window,height=7,width=66,text='',bg='white',anchor="se")
lb.place(x=30,y=30,)

# number button click action  add

opvalue=0
oldvalue=''
newvalue=''
eqe=""


def button1_clicked(value):
    global eqe
    eqe+=value
    lb.config(text=eqe)


def button2_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button3_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button4_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button5_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button6_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button7_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button8_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button9_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def button0_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)


def buttondot_clicked(value):
    global eqe
    eqe += value
    lb.config(text=eqe)

# control button click action

def buttonce_clicked():
    global eqe
    eqe = ''

    lb.config(text=eqe)

def buttonc_clicked():
  global oldvalue
  global newvalue
  global opvalue
  global eqe

  oldvalue=''
  newvalue=''
  opvalue=0
  eqe=''
  lb.config(text=eqe)


def buttonX_clicked():
    global eqe
    eqe=''
    num=lb['text']
    cout=1
    for i in num:
        if cout<len(num):
            eqe += i
            cout+=1

        else:
           break
    lb.config(text=eqe)


# operator button click action

def add_but_clicked():
    global oldvalue
    global eqe
    global opvalue

    eqe=''
    oldvalue=lb['text']
    lb.config(text=eqe)
    opvalue=1


def sub_but_clicked():
    global oldvalue
    global eqe
    global opvalue

    eqe=''
    oldvalue=lb['text']
    lb.config(text=eqe)
    opvalue=2

def mult_but_clicked():
    global oldvalue
    global eqe
    global opvalue

    eqe=''
    oldvalue=lb['text']
    lb.config(text=eqe)
    opvalue=3


def div_but_clicked():
    global oldvalue
    global opvalue
    global eqe

    eqe=''
    oldvalue=lb['text']
    lb.config(text=eqe)
    opvalue=4


def equal_button_clicked():
    global opvalue
    global oldvalue
    global newvalue
    newvalue=lb['text']

    if opvalue==1:

        resuil=float(oldvalue)+float(newvalue)
        lb.config(text=resuil)

    elif opvalue==2:
        resuil = float(oldvalue) - float(newvalue)
        lb.config(text=resuil)

    elif opvalue==3:
        resuil = float(oldvalue) * float(newvalue)
        lb.config(text=resuil)

    elif opvalue==4:
        resuil = float(oldvalue) / float(newvalue)
        lb.config(text=resuil)
    else:
        initial=lb['text']
        lb.config(text=initial)


# control buttons

buttce=tkinter.Button(window,text='CE',bg='#fc475f',width=10,height=4,activebackground='red',command=lambda :buttonce_clicked())
buttce.place(x=30,y=180)
buttc=tkinter.Button(window,text='C',bg='#fc475f',width=10,height=4,activebackground='red',command=lambda :buttonc_clicked())
buttc.place(x=160,y=180)
buttx=tkinter.Button(window,text='X',bg='#fc475f',width=10,height=4,activebackground='red',command=lambda :buttonX_clicked())
buttx.place(x=290,y=180)

# number buttons

butt7=tkinter.Button(window,text='7',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button7_clicked('7'))
butt7.place(x=30,y=280)
butt8=tkinter.Button(window,text='8',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button8_clicked('8'))
butt8.place(x=160,y=280)
butt9=tkinter.Button(window,text='9',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button9_clicked('9'))
butt9.place(x=290,y=280)
butt4=tkinter.Button(window,text='4',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button4_clicked('4'))
butt4.place(x=30,y=380)
butt5=tkinter.Button(window,text='5',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button5_clicked('5'))
butt5.place(x=160,y=380)
butt6=tkinter.Button(window,text='6',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button6_clicked('6'))
butt6.place(x=290,y=380)
butt1=tkinter.Button(window,text='1',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button1_clicked('1'))
butt1.place(x=30,y=480)
butt2=tkinter.Button(window,text='2',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button2_clicked('2'))
butt2.place(x=160,y=480)
butt3=tkinter.Button(window,text='3',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button3_clicked('3'))
butt3.place(x=290,y=480)
butt0=tkinter.Button(window,text='0',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :button0_clicked('0'))
butt0.place(x=30,y=580)
butt_dot=tkinter.Button(window,text='.',bg='gray',width=10,height=4,activebackground='#62bce3',command=lambda :buttondot_clicked('.'))
butt_dot.place(x=160,y=580)

# operator buttons

butt_equal=tkinter.Button(window,text='=',bg='#5bf0a5',width=29,height=4,activebackground='white',command=lambda :equal_button_clicked())
butt_equal.place(x=290,y=580)
butt_div=tkinter.Button(window,text='/',bg='#695cab',width=10,height=4,activebackground='green',command=lambda :div_but_clicked())
butt_div.place(x=420,y=180)
butt_mult=tkinter.Button(window,text='*',bg='#695cab',width=10,height=4,activebackground='green',command=lambda :mult_but_clicked())
butt_mult.place(x=420,y=280)
butt_sub=tkinter.Button(window,text='-',bg='#695cab',width=10,height=4,activebackground='green',command=lambda :sub_but_clicked())
butt_sub.place(x=420,y=380)
butt_add=tkinter.Button(window,text='+',bg='#695cab',width=10,height=4,activebackground='green',command=lambda :add_but_clicked())
butt_add.place(x=420,y=480)






window.mainloop()
