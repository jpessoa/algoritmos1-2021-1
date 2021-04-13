# Faça um algoritmo que leia um inteiro 2 <= n <= 100
# e em seguida leia uma sequência de n números.
# O algoritmo deve responder "SIM" se a sequência for
# crescente e "NÃO", caso contrário.

n = int(input())

ant = int(input())

n = n - 1
crescente = True
while n > 0 and crescente:
	x = int(input())
	if not x > ant:
		crescente = False

	ant = x
	n = n - 1

if crescente:
	print("SIM")
else:
	print("NÃO")