# Função sem parâmetros
def digaHello():
	print("Hello World!")

# Função com um parâmetro chamado nome
def digaHelloFulano(nome):
	print(f"Hello {nome}!")

def digaHelloFuladoDeTal(nome, sobrenome):
	print(f"Hello {nome} {sobrenome}!")

def digaHelloFulanoIdade(nome, idade):
	print(f"Oi {nome}. Vejo que você tem {idade} anos.")

def dobro(x):
	valor_dobrado = 2 * x
	return valor_dobrado

def dobroTriplo(x):
	dobro = 2 * x
	triplo = 3 * x

	return dobro, triplo


def main():
	# Chamando uma função e passando um argumento a ela:
	digaHelloFulano("Alan")
	digaHelloFulano("Carlos")

	digaHelloFuladoDeTal("Maria", "Silva")

	digaHelloFulanoIdade("José", 35)

	valor = dobro(2.5)
	print(valor)

	a, b = dobroTriplo(3.2)
	print(f"{a:.2f}, {b:.2f}")


main()