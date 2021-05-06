# Faça um programa que some os primeiros n números de Fibonacci.
# Calcula o n-ésimo número de Fibonacc
def fibo(n):
	if n == 0 or n == 1:
		fib = n
	else:
		# n >= 2
		a = 0
		b = 1
		for i in range(1, n):
			fib = a + b
			a = b
			b = fib

	return fib

#-------------------------------------
def main():
	n = int(input())

	soma = 0
	for i in range(0, n):
		soma += fibo(i)


	print(soma)

#-------------------------------------

main()