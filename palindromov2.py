n = int(input())

numero = n
inv = 0;
while n != 0:
	inv = inv * 10 + (n % 10)
	n = n // 10

if numero == inv:
	print("SIM")
else:
	print("NAO")