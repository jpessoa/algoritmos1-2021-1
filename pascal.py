m = int(input())

for n in range(0, m):
	for k in range(0, n+1):
		#print(f"C({n}, {k})", end="  ")

		# Calcular n!
		fat1 = 1
		for i in range(1, n+1):
			fat1 = fat1 * i

		# Calcular k!
		fat2 = 1
		for i in range(1, k+1):
			fat2 = fat2 * i

		# Calcular (n-k)!
		fat3 = 1
		for i in range(1, n-k+1):
			fat3 = fat3 * i

		comb = fat1 // (fat2 * fat3)
		print(comb, end=" ")

	print("")
