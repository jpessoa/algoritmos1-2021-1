def harmonico(n):
	harmonico = 0.0
	for i in range(1, n+1):
		harmonico = harmonico + 1.0 / i

	return harmonico
#-----------------------------------------


def main():
	n = int(input())

	har = harmonico(n)

	print(f"{har:.4f}")

main()