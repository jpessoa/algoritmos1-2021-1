x = float(input())
n = int(input())

valor = 0.0
for i in range(0, n+1):
	# print(i)

	# calcula i!
	fat = 1
	for j in range(1, i+1):
		fat = fat * j

	#print(f"{x}^{i} / {fat}")
	valor = valor + x ** i / fat

print(f"{valor:.4f}")