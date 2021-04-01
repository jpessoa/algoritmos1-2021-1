# 1036 Bhaskara

# entrada:
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

# outro jeito de fazer a entrada:
#a, b, c = map(float, input().split())

delta = b ** 2 - 4.0 * a * c

if delta < 0.0 or a == 0.0:
	print("Impossivel calcular")
else:
	r1 = (-b + (delta ** 0.5)) / (2.0 * a)
	r2 = (-b - (delta ** 0.5)) / (2.0 * a)
	print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
	#print(f"R2 = {r2:.5f}")