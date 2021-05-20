def combinador(x, y):
	x = list(x)
	y = list(y)
	z = []

	if len(x) < len(y):
		menor = len(x)
	else:
		menor = len(y)

	pegaDoX = True
	i = 0
	j = 0
	for k in range(menor*2):
		if pegaDoX:
			z.append(x[i])
			i += 1
			pegaDoX = False
		else:
			z.append(y[j])
			j += 1
			pegaDoX = True

	# Copia o restante do maior vetor em Z
	if len(x) < len(y):
		for k in range(j, len(y)):
			z.append(y[k])
	else:
		for k in range(i, len(x)):
			z.append(x[k])

	return "".join(z)


def main():
	n = int(input())

	for i in range(n):
		x, y = input().split()
		z = combinador(x, y)
		print(z)

main()