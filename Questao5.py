#Escreva um programa que solicite ao usuário que digite uma lista de números
#inteiros separados por vírgula. O programa deve criar uma nova lista contendo
#apenas os números pares da lista original, utilizando uma estrutura de
#repetição, EM PYTHON


# Solicita ao usuário que digite uma lista de números inteiros separados por vírgula
numeros_str = input("Digite uma lista de números inteiros separados por vírgula: ")

# Separa os números em uma lista
numeros = numeros_str.split(",")

# Criação da lista para armazenar os números pares
numeros_pares = []

# Verifica cada número na lista
for numero in numeros:
    # Converte o número para inteiro
    numero = int(numero.strip())
    
    # Verifica se o número é par
    if numero % 2 == 0:
        # Adiciona o número à lista de números pares
        numeros_pares.append(numero)

# Exibe a lista de números pares
print("Números pares:")
print(numeros_pares)