# P = 15  M = 18.5   G = 23
# Queijo P = 2.5     M ou G = 4
# Borda = 5

def pizza():
	tamanho, queijo, borda = input().split()

	total = 0.0

	if tamanho == "P":
		total = 15.0
	elif tamanho == "M":
		total = 18.5
	else:
		total = 23.0


	if queijo == "S":
		if tamanho == "P":
			total = total + 2.5
		else:
			total = total + 4.0

	if borda == "S":
		total = total + 5.0

	print(f"Total: R$ {total:.2f}")

pizza()
