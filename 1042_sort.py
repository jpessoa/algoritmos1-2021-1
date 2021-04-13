a, b, c = map(int, input().split())

if a < b:
	if b < c:
		#print(f"{a}\n{b}\n{c}")
		A = a
		B = b
		C = c
	else:
		# b é o maior de todos
		if a < c:
			print(f"{a}\n{c}\n{b}")
		else:
			print(f"{c}\n{a}\n{b}")
else:
	if a < c:
		print(f"{b}\n{a}\n{c}")
	else:
		# a é o maior de todos
		if b < c:
			print(f"{b}\n{c}\n{a}")
		else:
			print(f"{c}\n{b}\n{a}")


print(f"\n{a}\n{b}\n{c}")