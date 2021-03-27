# Strings
"Hello World!"
'Hello World!'   # Pode-se usar aspas simples, mas eu estarei usando aspas duplas.

"123"  # Isso é uma string, e não é o número inteiro 123

# Concatenando strings, usando o operador +
# string1 + string2
print("Carlos" + "Higa")

nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)

# Concatenando duas strings e não dois números inteiros:
A = "10"
B = "9"
X = A + B
print(X)

# Não podemos concatenar uma string com um número:
# "string" + 100

# A função print()
print("Algoritmos", "Programação", 2021)


# A função input() SEMPRE RETORNA UMA STRING
#nome = input("Qual o seu nome? ")
#idade = input("Qual a sua idade? ")
#print(nome, idade)

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

X = A + B

print("X = " + str(X))


