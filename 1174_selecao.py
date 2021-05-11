def selecao(v):
	for i in range(len(v)):
		if v[i] <= 10:
			print(f"A[{i}] = {v[i]:.1f}")

#-------------------------------------

def main():

	# Leitura da entrada:
	vet = []
	for i in range(100):
		n = float(input())
		vet.append(n)

	selecao(vet)

#-------------------------------------

main()