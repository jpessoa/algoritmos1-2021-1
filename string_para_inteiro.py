# Conversão de tipos: de string para int  e vice-versa

idade_str = input("Qual a sua idade? ")

idade_int = int(idade_str)   # Converte de string para número inteiro.

nova_idade = idade_int + 10

nova_idade_str = str(nova_idade)  # Converte de número inteiro para string.

print("Tenho " + nova_idade_str)
