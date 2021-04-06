#a, b = input().split()
#a = int(a)
#b = int(b)

a, b = map(int, input().split())

if a < b:
	temp = b
	b = a
	a = temp

if a % b == 0:
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")