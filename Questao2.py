#Crie uma lista de números inteiros. Em seguida, escreva um programa que
#encontre e exiba o maior e o menor número da lista, bem como a soma de
#todos os números, EM PYTHON.

# Criação da lista de números inteiros
numeros = [10, 5, 8, 3, 15, 12]

# Inicialização das variáveis para o maior e menor número
maior = numeros[0]
menor = numeros[0]

# Inicialização da variável para a soma dos números
soma = 0

# Percorre cada número na lista
for numero in numeros:
    # Verifica se o número atual é maior que o maior número encontrado até o momento
    if numero > maior:
        maior = numero
    
    # Verifica se o número atual é menor que o menor número encontrado até o momento
    if numero < menor:
        menor = numero
    
    # Adiciona o número atual à soma
    soma += numero

# Exibe o maior, o menor e a soma dos números
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma dos números é: {soma}")