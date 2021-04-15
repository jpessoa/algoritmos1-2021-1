n = int(input())

pi = 0.0
somar = True
for i in range(1, n+1, 2):
	if somar:
		pi = pi + 4.0 / i
		somar = False
	else:
		pi = pi - 4.0 / i
		somar = True


print(f"{pi:.4f}")