n = int(input())

i = 2
primo = True
while i < n and primo:
	# testar se é possível dividir n por i
	if n % i == 0:
		primo = False

	i = i + 1


if primo:
	print("Primo")
else:
	print("Composto")