# Faça um programa que leia um número inteiro
# e diga se o número é positivo (> 0)ou não positivo.
# No caso do número ser positivo, informe se o 
# número digitado é um número alto ou não.
# Um número alto é um número maior que 1000000.

n = int(input())

if n > 0:
	print("É positivo.")
	if n > 1000000:
		print("É um número alto.")
	else:
		print("É um número baixo.")
else:
	print("É não positivo.")