def func(uma_lista):
	uma_lista.append(10)


def alterax(x):
	x += 1

def main():
	l = [0, 1, 2]
	func(l)
	print(l)


	x = 5
	alterax(x)
	print(x)


main()