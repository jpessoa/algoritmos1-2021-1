n = int(input())

numero = n


digitos = 0
while n != 0:
	n = n // 10
	digitos = digitos + 1

n = numero
inv = 0
while n != 0:
	mod = n % 10
	inv = inv + mod * 10 ** (digitos-1)
	digitos = digitos - 1
	n = n // 10



if numero == inv:
	print("SIM")
else:
	print("NAO")