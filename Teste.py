from tkinter import *

def muda_barrinha(tecla):
    barrinha1.focus()

janela2 = Tk()
janela2.geometry('250x250+100+100')

lb2 = Label(janela2, text='coloque seu nome')

barrinha = Entry(janela2)

barrinha.place(x=80, y=80)
barrinha.focus()
barrinha.bind("<Return>", muda_barrinha)
barrinha1 = Entry(janela2)
barrinha1.place(x=80, y=120)

janela2.mainloop()