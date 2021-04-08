n = int(input())

i = 0
somap = somai = 0
while i < n:
	m = int(input())
	
	if m % 2 == 0:
		somap = somap + m
	else:
		somai = somai + m

	i = i + 1

print(f"Pares: {somap}\nImpares: {somai}")