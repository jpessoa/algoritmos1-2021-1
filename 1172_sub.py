def substitui(vet):
	for i in range(0, len(vet)):
		if vet[i] <= 0:
			vet[i] = 1
#---------------------------------

def imprime(vet):
	for i in range(0, len(vet)):
		print(f"X[{i}] = {vet[i]}")


def main():
	x = []
	for i in range(1, 11):
		num = int(input())
		x.append(num)

	substitui(x)
	imprime(x)


main()