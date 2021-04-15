d = 1
s = 0.0
for i in range(1, 40, 2):
	#print(f"{i} / {d}")
	s = s + i / d
	d = d * 2
	
print(f"{s:.2f}")
