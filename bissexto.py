ano = int(input())

if ano % 4 == 0:
	if ano % 100 == 0:
		if ano % 400 == 0:
			print("Bissexto")
		else:
			print("Ano qualquer")
	else:
		print("Bissexto")
else:
	print("Ano qualquer")

# outro jeito
#if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
#    print('Ano bissexto.')
#else:
#    print('Não é um ano bissexto.')