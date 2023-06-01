#Crie uma tupla de números inteiros. Escreva um programa que conte quantas
#vezes um determinado número aparece na tupla. Solicite ao usuário que digite
#um número e exiba a contagem correspondente, EM PYTHON.

# Criação da tupla de números inteiros
numeros = (10, 5, 8, 3, 15, 12, 5, 8, 5)

# Solicita ao usuário que digite um número
numero_desejado = int(input("Digite um número: "))

# Inicialização da variável de contagem
contagem = 0

# Percorre cada número na tupla
for numero in numeros:
    # Verifica se o número atual é igual ao número desejado
    if numero == numero_desejado:
        # Incrementa a contagem
        contagem += 1

# Exibe a contagem correspondente
print(f"O número {numero_desejado} aparece {contagem} vez(es) na tupla.")