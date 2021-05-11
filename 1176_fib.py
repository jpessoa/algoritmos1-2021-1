def fibonacci(n):
	fib = [0, 1]

	for i in range(2, n+1):
		fib.append(fib[i-1] + fib[i-2])

	return fib[n]

#--------------------------------

def main():
	t = int(input())

	for i in range(t):
		n = int(input())
		f = fibonacci(n)
		print(f"Fib({n}) = {f}")

main()