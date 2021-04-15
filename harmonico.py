n = int(input())

harmonico = 0.0
for i in range(1, n+1):
	harmonico = harmonico + 1.0 / i

print(f"{harmonico:.4f}")