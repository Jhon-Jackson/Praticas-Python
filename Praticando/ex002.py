
# file = open("Textos.txt", "r")
# teste = file.read()
# file.close()



# with open("Textos.txt", "a") as file:
#     file.write("\nOlá, Samuel")
#     open("Textos.txt", "r")
#
#
# with open("Textos.txt", "r") as file:
#     teste = file.read()
#     #print(teste)
#
# with open("Textos.txt", "r") as file:
#     for idx, linha in enumerate(file):
#         print(idx, linha.strip())

Arquivo = "Textos.txt"
while True:
    print("para Finalizar Digite Sair")
    nota = input("Escreva uma nota: ")

    with open(Arquivo, "a") as file:
        file.write(nota + "!\n" )

    if nota == "sair":
        break

with open(Arquivo, "r") as file :
    for idx, linha in enumerate(file):
        print(f"{idx + 1}. {linha}")
