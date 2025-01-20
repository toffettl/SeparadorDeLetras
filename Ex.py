nome = input("Digite seu nome: ")
tamanhoNome = len(nome)
indice = 0
separado = ""

while indice < tamanhoNome:
    letra = nome[indice]
    separado += f"*{letra}"
    indice += 1

separado += "*"
print(separado)
