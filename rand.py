import random

i = 0
while i < 100:
	n = random.randint(1, 1000)
	#n = random.random() * 100
	print(f"{n}", end=" ")
	i += 1
