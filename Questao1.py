#Escreva um programa que solicite ao usuário que digite uma frase. O programa
#deve contar e exibir quantas vezes cada letra aparece na frase, ignorando
#espaços em branco e diferenciação entre letras maiúsculas e minúsculas.
#Utilize um dicionário para armazenar as informações, EM PYTHON.

frase = input("Digite uma frase: ")

# Remove os espaços em branco da frase
frase = frase.replace(" ", "")

# Inicializa um dicionário vazio para armazenar as contagens
contagem_letras = {}

# Percorre cada letra na frase
for letra in frase:
    # Ignora a diferenciação entre letras maiúsculas e minúsculas
    letra = letra.lower()
    
    # Verifica se a letra já está no dicionário
    if letra in contagem_letras:
        # Incrementa a contagem da letra
        contagem_letras[letra] += 1
    else:
        # Adiciona a letra ao dicionário com contagem igual a 1
        contagem_letras[letra] = 1

# Exibe as contagens de cada letra
for letra, contagem in contagem_letras.items():
    print(f"A letra '{letra}' aparece {contagem} vez(es) na frase.")