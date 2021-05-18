def produto(u, v):
	prod = 0.0
	for i in range(0, len(u)):
		prod = prod + u[i] * v[i]

	return prod

def main():
	u = list(map(float, input().split()))
	v = list(map(float, input().split()))
	x = produto(u, v)
	print(f"{x:.4f}")

main()