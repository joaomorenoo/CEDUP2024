from tkinter import *

janela = Tk()
janela.geometry("1280x720")
janela.title("Sabrina")
text = Label(janela, text = "Texto teste")
text.grid(column = 0, row = 0)

botao = Button(janela, text = "OI", command = print("hello world!"))
botao.grid(column = 1, row = 1)
ext = Label(janela, text = "")
text.grid(column = 0, row = 0)
ext = Label(janela, text = "")
text.grid(column = 1, row = 1)
ext = Label(janela, text = "")
text.grid(column = 2, row = 2)
ext = Label(janela, text = "")
text.grid(column = 3, row = 3)
ext = Label(janela, text = "")
text.grid(column = 4, row = 4)
ext = Label(janela, text = "")
text.grid(column = 5, row = 5)
ext = Label(janela, text = "")
text.grid(column = 6, row = 6)
ext = Label(janela, text = "")
text.grid(column = 7, row = 7)
ext = Label(janela, text = "")
text.grid(column = 8, row = 8)
ext = Label(janela, text = "")
text.grid(column = 9, row = 9)




janela.mainloop()