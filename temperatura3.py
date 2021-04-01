# Faça um programa que leia um valor float que é a
# temperatura. O programa deve informar se
# - está muito frio: t < 0
# - um pouco frio: t >= 0 e t < 14
# - agradável: t >= 14 e t < 23
# - calor: t >= 23

t = float(input("Qual a temperatura atual? "))

if t < 0.0:
	print("Frio.")
elif t >= 0.0 and t < 14.0:
	print("Está um pouco frio.")
elif t >= 14.0 and t < 23.0:
	print("Está agradável.")
else:
	print("Calor.")
