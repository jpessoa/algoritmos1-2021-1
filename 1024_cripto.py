def criptografia(w):
	l = list(w)
	
	# Primeira passada
	for i in range(len(l)):
		code = ord(l[i])
		if (code >= 65 and code <= 90)  or (code >= 97 and code <= 122):
			l[i] = chr(code + 3)

	# Segunda passada
	j = len(l)-1
	for i in range(len(l) // 2):
		temp = l[i]
		l[i] = l[j]
		l[j] = temp
		j = j - 1

	# Terceira passada
	for i in range(len(l) // 2, len(l)):
		l[i] = chr(ord(l[i])-1)

	return "".join(l)


def main():
	n = int(input())
	for i in range(n):
		w = input()
		c = criptografia(w)
		print(c)

main()