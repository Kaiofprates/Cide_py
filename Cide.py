__Author__ = "Kaio Fábio Prates"

import os
from translate_C import translate 
from tkinter import *
from tkinter import filedialog

tela = Tk()
tela.title("PY_teste")
tela['bg'] = '#4B0082'
tela.geometry('600x650')




def escolha():

	tela.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("codigo em c","*.c"),("Text Files","*.txt"),("all files","*.*")))
	file = open(tela.filename, "r")
	listFiles = file.readlines()
	for i in listFiles[:]:
		texto.insert(INSERT,i)
	
def salvar():
	a = open("arquivo.c","w")
	y = texto.get(1.0, END)
	a.write(y)
	a.close

def copilar():
	#os.system("gnome-terminal -- gcc -Wall arquivo.c -o arquivo") //Linux
	#os.system("gnome-terminal -- ./arquivo") //Linux
	#os.system("gcc -Wall arquivo.c") //Windows
	#os.system("a.exe") //Windows

def pseudocodigo():
	y = texto.get(1.0, END)
	y = y.replace("escreva","printf")
	y = y.replace("receba","scanf")
	y = y.replace("mostre","printf")
	y = y.replace("leia","scanf")
	texto.delete(1.0,END)
	x = "#include <stdio.h>\n#include <stdlib.h>\n\nint main(){\n\n"
	texto.insert(INSERT,x)
	texto.insert(INSERT,y)
	texto.insert(INSERT,"\n\ngetchar();\n\nreturn 0;\n}")

#struct = lambda: texto.insert(CURRENT,"struct funcao { };")
def traduz():
	x = translate(texto.get(1.0,END))
	texto.delete(1.0,END)
	texto.insert(INSERT,x)


texto = Text(tela,height = 40, width = 70,bg = "white", fg ="black")
texto.tag_config("a", foreground="blue", underline=1)
#button = Button(texto, text="Click", command=salvar)
#texto.window_create(INSERT, window=button)
texto.config(cursor="arrow")
texto.place(x = 55, y =60)

bot1 = Button(tela,text = "salvar",bg = '#4B0082', fg = 'white', command = salvar)
bot1.place(x = 150, y = 20)

bot2 = Button(tela,text = "copilar",bg = '#4B0082', fg = 'white', command = copilar)
bot2.place(x = 250, y = 20)

bot3 = Button(tela,text = "Pseu",height = 2, width = 1, bg = '#4B0082', fg = 'black', command = pseudocodigo)
bot3.place(x = 5, y = 60)

bot4 = Button(tela,text = "Repl",height = 2, width = 1, bg = '#4B0082', fg = 'black', command = traduz)
bot4.place(x = 5, y = 100)

bot = Button(tela,text = "Pesquisar",bg = '#4B0082', fg = 'white', command = escolha)
bot.place(x = 30, y = 20)




tela.mainloop()
