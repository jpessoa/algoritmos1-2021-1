def derivada(a):
	d = []
	for i in range(1, len(a)):
		d.append(i * a[i])

	return d
	
def imprime(vet):
	for c in vet:
		print(f"{c:.4f}")

def main():
	a = list(map(float, input().split()))
	c = derivada(a)
	imprime(c)

main()