from tkinter import *
import webbrowser
import random

c = 0
r = 10

def abrirlink():
    webbrowser.open("https://www.youtube.com/watch?v=EVHs7jmRdXk&ab_channel=FOBOSPLANET")



janela = Tk()
botao1 = Button(janela, text="SIM", command = abrirlink)
botao1.grid(column = 2, row = 1, padx= 10, pady= 10)
botao2 = Button(janela, text="NÃO", command = "")
botao1.grid(column = 2, row = 1, padx= 10, pady= 10)
text = Label(janela, text = "")
text.grid(column = 1, row = 1)
janela.mainloop()