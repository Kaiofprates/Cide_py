#Author = Los Guidos
#encoding = utf-8

import re

def translate(res):
	#arq = open("translate.txt","w")
	#code = open(texto,"r")
	#res = code.read()
	var = re.findall(r"int(.*);",res)
	inteiro = []
	for i in var[:]:
		inteiro.append(i)
	var = re.findall(r"float(.*);",res)
	real = []
	for i in var[:]:
		real.append(i)
	var = re.findall(r"char(.*);",res)
	char = []
	for i in var[:]:
		char.append(i)
	var = re.findall(r"leia(.*)?;",res)

	var  = str(var);var = var.replace(")","");var = var.replace("[","");var = var.replace("'","")
	var = var.replace("(","");var = var.replace("]","");var = var.replace(" ","")
	var = var.split(",")


	f = str(real)
	f= f.replace(")","");f = f.replace("[","");f = f.replace("'","")
	f = f.replace("(","");f = f.replace("]","");f = f.replace(" ","")
	f = f.split(",")


	if type(var) == list: 
		for i in var[:]:
			for j in f[:]:
				if i == j:
				
					s = "leia("+i+");"
					d = "scanf("+""" "%f" """+", &"+i+");"

					res = res.replace(s,d)

	if type(var) == str:
		for i in f[:]:
			if i == var:
		
				s = "leia("+i+");"
				d = "scanf("+""" "%f" """+", &"+i+");"
				res = res.replace(s,d)


	inteiro = str(inteiro)
	inteiro= inteiro.replace(")","");inteiro = inteiro.replace("[","");inteiro = inteiro.replace("'","")
	inteiro = inteiro.replace("(","");inteiro = inteiro.replace("]","");inteiro = inteiro.replace(" ","")
	inteiro = inteiro.split(",")


	if type(var) == list: 
		for i in var[:]:
			for j in inteiro[:]:
				if i == j:
				
					s = "leia("+i+");"
					d = "scanf("+""" "%i" """+", &"+i+");"

					res = res.replace(s,d)

	if type(var) == str:
		if i in inteiro[:]:
			if i == var:
		
				s = "leia("+i+");"
				d = "scanf("+""" "%i" """+", &"+i+");"
				res = res.replace(s,d)
	res = res.replace("escreva","printf")

	header = "#include <stdio.h>\n#include <stdlib.h>\nint main(){\n"
	end = "\ngetchar();\nreturn 0;\n}"
	codfim = (header+res+end)
	#arq.write(codfim)
	#arq.close()

	return codfim


#a = translate(input("codigo: "))
#print(a)