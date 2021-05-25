def inverte(vet):
	j = len(vet)-1
	for i in range(len(vet) // 2):
		temp = vet[j]
		vet[j] = vet[i]
		vet[i] = temp
		j = j - 1

def main():
	l = list(map(int, input().split()))

	inverte(l)
	
	print(l)

main()