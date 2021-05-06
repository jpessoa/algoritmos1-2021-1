def dobro(x):
	for i in range(1, len(x)):
		x[i] = 2 * x[i-1]

#-------------------------------------

def imprime(x):
	for i in range(0, len(x)):
		print(f"N[{i}] = {x[i]}")

#-------------------------------------

def main():
	n = int(input())

	vet = [0] * 10
	vet[0] = n

	dobro(vet)
	imprime(vet)

#-------------------------------------

main()
