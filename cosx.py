x = float(input())
k = int(input())

cos = 0.0
somar = True
for i in range(0, k+1, 2):
	# Calcular i!
	fat = 1
	for j in range(1, i+1):
		fat = fat * j

	#print(f"{x}^{i} / {fat}")
	if somar:
		cos = cos + x ** i / fat
		somar = False
	else:
		cos = cos - x ** i / fat
		somar = True

print(f"{cos:.4f}")