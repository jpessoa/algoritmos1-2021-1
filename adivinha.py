# Como usar o comando break
import random

n = random.randint(0, 10)

while True:
	i = int(input("Adivinhe o número: "))
	if i == n:
		print("Você acertou!")
		break
	else:
		print("Você errou! Tente novamente.")

print("Bye.")

# Faça este jogo sem usar o break