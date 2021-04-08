# sem usar o break
import random

n = random.randint(0, 10)

acertou = False

while not acertou:
	i = int(input("Adivinhe o número: "))
	if i == n:
		acertou = True
	else:
		print("Você errou! Tente novamente.")

print("Você acertou!")
print("Bye.")
