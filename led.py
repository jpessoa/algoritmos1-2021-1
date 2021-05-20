def contaLED(x):
	led = 0
	for dig in x:
		if dig == "1":
			led += 2
		elif dig == "2" or dig == "3" or dig == "5":
			led += 5
		elif dig == "4":
			led += 4
		elif dig == "7":
			led += 3
		elif dig == "8":
			led += 7
		else:
			led += 6

	return led

def main():
	n = int(input())

	for i in range(n):
		x = list(input())
		quantidade = contaLED(x)
		print(f"{quantidade} leds")

main()