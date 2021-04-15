# Faça um programa que leia um número inteiro e
# responda quantos dígitos ele tem

n = int(input())

digitos = 0
while n != 0:
	n = n // 10
	digitos = digitos + 1	

print(digitos)