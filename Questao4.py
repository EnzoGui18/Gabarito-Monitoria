#Considere a seguinte lista de nomes: nomes = ['Maria', 'João', 'Ana', 'Pedro',
#'João', 'Paulo']. Escreva um programa que crie um conjunto (set) a partir dessa
#lista e exiba os nomes que possuem mais de 4 letras, EM PYTHON.

nomes = ['Maria', 'João', 'Ana', 'Pedro', 'João', 'Paulo']

# Criação do conjunto a partir da lista
conjunto_nomes = set(nomes)

# Inicialização de uma lista vazia para armazenar os nomes com mais de 4 letras
nomes_mais_de_4_letras = []

# Verifica cada nome no conjunto
for nome in conjunto_nomes:
    # Verifica se o nome possui mais de 4 letras
    if len(nome) > 4:
        # Adiciona o nome à lista
        nomes_mais_de_4_letras.append(nome)

# Exibe os nomes com mais de 4 letras
print("Nomes com mais de 4 letras:")
for nome in nomes_mais_de_4_letras:
    print(nome)