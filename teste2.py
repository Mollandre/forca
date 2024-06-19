from tkinter import *



janela = Tk()
janela.geometry("300x300")
janela.title("forca")


caixa = Entry(janela, show="_")
caixa.place(x=20, y=20)
caixa.configure(width=3)

caixa1 = Entry(janela, show="_")
caixa1.place(x=40, y=20)
caixa1.configure(width=3)

caixa2 = Entry(janela, show="_")
caixa2.place(x=60, y=20)
caixa2.configure(width=3)

caixa3 = Entry(janela, show="_")
caixa3.place(x=80, y=20)
caixa3.configure(width=3)

caixa4 = Entry(janela, show="_")
caixa4.place(x=100, y=20)
caixa4.configure(width=3)



caixas = [caixa.get(), caixa1.get(), caixa3.get()]

label = Label(janela, text="_")
label.place(x=10, y=40)

label1 = Label(janela, text="_")
label1.place(x=20, y=40)

label2 = Label(janela, text="_")
label2.place(x=30, y=40)

label3 = Label(janela, text="_")
label3.place(x=40, y=40)

label4 = Label(janela, text="_")
label4.place(x=50, y=40)

label5 = Label(janela, text="_")
label5.place(x=60, y=40)



labelr = Label(janela, text="")
labelr.place(x=40, y=160)



Cx1 = Entry(janela, )
Cx1.place(x=40, y=140)

Cx1.insert(2,"Coloque um numero")
#Placeholder
def Apagar(event):
    if Cx1.get() == "Coloque um numero":
        Cx1.delete(0, "end")


def Voltar(event):

    if Cx1.get() == " ":

       Cx1.insert(1, "Coloque um numero")


Cx1.bind("<FocusIn>", Apagar)
Cx1.bind("<FocusOut>", Voltar)

acerto = 0
erro = 0
letra = 0



def Confirma():


    global acerto
    global erro
    global letra

    caixas = [caixa.get(), caixa1.get(), caixa2.get()]
    ccx = Cx1.get()

    while acerto != letra:

          if ccx in caixas:



              if Cx1.get() == caixa.get():
                     label.configure(text=caixa.get())



              if Cx1.get() == caixa1.get():
                     label1.configure(text=caixa1.get())


              if Cx1.get() == caixa2.get():
                     label2.configure(text=caixa2.get())


              if Cx1.get() == caixa3.get():
                     label3.configure(text=caixa3.get())



              if Cx1.get() == caixa4.get():
                    label4.configure(text=caixa4.get())

          else:
                  acerto += 1
                  label12.configure(text=acerto)

          break




botao = Button(janela, text="Confima", command=Confirma)
botao.place(x=60, y=80)

label12 = Label(janela, text=acerto)
label12.place(x=10, y=160)

label13 = Label(janela, text=erro)
label13.place(x=10, y=200)


def Comecar():

    global letra


    while letra == 0:
        if caixa.get() == "":
            letra += 0
        else:
            letra += 1

        if caixa1.get() != "":
            letra += 1


        if caixa2.get() == "":
            letra += 0
        else:
            letra += 1

        if caixa3.get() == "":
            letra += 0
        else:
            letra += 1

        if caixa4.get() == "":
            letra += 0
        else:
            letra += 1



        labelr.configure(text=letra)
        break





botao2 = Button(janela, text="Começar", command=Comecar)
botao2.place(x=40, y=200)








mainloop()