def polinomio(x, a):
	soma = a[0]
	for i in range(1, len(a)):
		soma = soma + a[i] * (x ** i)

	return soma


def main():
	a = list(map(float, input().split()))

	k = int(input())
	for i in range(k):
		x = float(input())
		valorp = polinomio(x, a)
		print(f"{valorp:.4f}")

main()