binario = int(input())

dec = exp = 0
while binario != 0:
	div = binario // 10
	mod = binario % 10
	dec = dec + mod * (2 ** exp)
	exp = exp + 1
	binario = div

print(dec)