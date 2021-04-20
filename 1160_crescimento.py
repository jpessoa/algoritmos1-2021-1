t = int(input())

for i in range(t):
	PA, PB, G1, G2 = input().split()
	PA = int(PA)
	PB = int(PB)
	G1 = float(G1)
	G2 = float(G2)

	tempo = 0
	while PA <= PB and tempo <= 100:
		tempo = tempo + 1
		PA = PA + (PA * G1) // 100
		PB = PB + (PB * G2) // 100
		print(PA, PB, tempo)

	if tempo > 100:
		print("Mais de 1 seculo.")
	else:
		print(f"{tempo} anos.")