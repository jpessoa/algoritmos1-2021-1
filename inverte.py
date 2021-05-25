l = [1, 2, 4, 8, 16, 32]

# inverte usando outro vetor:
#a = []
#for i in range(len(l)-1, -1, -1):
	#a.append(l[i])
#print(a)

# inverte sem usar outro vetor
j = len(l)-1
for i in range(len(l) // 2):
	temp = l[j]
	l[j] = l[i]
	l[i] = temp
	j = j - 1

print(l)