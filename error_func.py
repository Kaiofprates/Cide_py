from tkinter import *
import os

def error(status):
    tela = Tk()
    tela.title("__Error__")
    tela['bg'] = '#FF0000'
    tela.geometry('550x650')
    texto = Text(tela,height = 40, width = 70,bg = "white", fg ="black")
    texto.tag_config("a", foreground="blue", underline=1)
    texto.place(x = 30, y =60)
    texto.insert(INSERT,status)
    tela.mainloop()
