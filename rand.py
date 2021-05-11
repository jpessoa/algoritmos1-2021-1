import random

i = 0
while i < 1000000:
	n = random.randint(1, 6)
	# n = random.random() * 30 + -1
	print(f"{n}", end=" ")
	i += 1
