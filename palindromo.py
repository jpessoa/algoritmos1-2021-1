# Retorna o número de digitos de num
def contaDigitos(num):
	dig = 0
	while num != 0:
		num = num // 10
		dig = dig + 1

	return dig
#----------------------------------------

# Função que recebe n e retorna True se n é palíndromo, False caso contrário.
def EhPalindromo(n):
	numero = n
	
	digitos = contaDigitos(n)

	n = numero
	inv = 0
	while n != 0:
		mod = n % 10
		inv = inv + mod * 10 ** (digitos-1)
		digitos = digitos - 1
		n = n // 10

	return True if numero == inv else False

	#if numero == inv:
	#	return True
	#else:
    #	return False

#--------------------------------------
def main():
	n = int(input())

	if EhPalindromo(n):
		print("SIM")
	else:
		print("NAO")
#--------------------------------------

main()



