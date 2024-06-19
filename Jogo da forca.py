from tkinter import *


janela = Tk()
janela.geometry("300x500")
janela.title("Jogo da Forca")

label1 = Label(janela, text="Coloque Aqui a palavra para adivinhar", font=12)
label1.place(x=10, y=10)

palavra = Entry(janela, show="* ", font=14)
palavra.place(x=40, y=40)

label2 = Label(janela, text="     Palavra para adivinhar", font=17,)
label2.place(x=10, y=160)

label3 = Label(janela, text=" ", font=15)
label3.place(x=10, y=200)

label4 = Label(janela, text=" ", font=12)
label4.place(x=10, y=100)

label5 = Label(janela, text=" ", font=15)
label5.place(x=10, y=230)

label6 = Label(janela, text=" ", font=15)
label6.place(x=10, y=360)

tentativa = Entry(janela, )
tentativa.place(x=10, y=300)



def Secreta():

    text = palavra.get()
    tamanho = len(text)

    label3.configure(text="_ " * len(palavra.get()))
    label4.configure(text=f"A palavra tem {tamanho} letras ")


botao = Button(janela, text="Começar", command=Secreta)
botao.place(x=90, y=70)



def Confirma():
    palavra = "python"

    letras_usuario = []

    chances = 4

    ganhou = False

    while True:

        # criar a nossa logica

        for letra in palavra:

            if letra.lower() in letras_usuario:

                print(letra, end=" ")

            else:

                print("_", end=" ")

        print(f"Você tem {chances} chances")

        tentativa = input("Escolha uma letra para adivinhar: ")

        letras_usuario.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():
            chances -= 1

        ganhou = True

        for letra in palavra:

            if letra.lower() not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break

    if ganhou:

        print(f"Parabéns, você ganhou. A palavra era: {palavra}")

    else:

        print(f"Você perdeu! A palavra era: {palavra}")

botao2 = Button(janela, text="Confirma", command=Confirma)
botao2.place(x=40, y=400)
mainloop()