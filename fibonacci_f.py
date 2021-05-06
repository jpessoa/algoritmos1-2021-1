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

	Fn = fibo(n)

	print(Fn)

#-------------------------------------

main()