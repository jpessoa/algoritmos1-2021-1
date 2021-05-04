n = int(input())

num = int(input())
maior_atual = 1
maximo = 1
for i in range(1, n):
	ant = num
	num = int(input())

	if num > ant:
		maior_atual += 1
		if maior_atual > maximo:
			maximo = maior_atual
	else:
		maior_atual = 1

print(maximo)