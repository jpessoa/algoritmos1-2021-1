import math

# Função que retorna o maior elemento da lista
def maiorElemento(x):
	maior = x[0]
	for i in range(1, len(x)):
		if x[i] > maior:
			maior = x[i]

	return maior

# Função que retorna o menor elemento
def menorElemento(x):
	menor = x[0]
	for i in range(1, len(x)):
		if x[i] < menor:
			menor = x[i]

	return menor

# Função que calcula a média
def calculaMedia(x):
	soma = 0.0
	for valor in x:
		soma += valor

	return soma / len(x)

def calculaVariancia(x, m):
	soma = 0.0
	for valor in x:
		soma += (valor - m) ** 2

	return soma / len(x)

def calculaDesvio(varx):
	return math.sqrt(varx)

def main():
	x = list(map(float, input().split()))
	print(x)

	maiorx = maiorElemento(x)
	print(f"Maior = {maiorx:.2f}")

	menorx = menorElemento(x)
	print(f"Menor = {menorx:.2f}")

	mediax = calculaMedia(x)
	print(f"Média = {mediax:.2f}")

	varx = calculaVariancia(x, mediax)
	print(f"Variância = {varx:.2f}")

	desvio = calculaDesvio(varx)
	print(f"Desvio padrão = {desvio:.2f}")	



main()