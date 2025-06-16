# Nome: Jhon Jackson da Silva Santos
# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Projeto Integrador Extensionista – ADS 1
# Semestre Letivo: 1º Termo – 2025

Produtos = {}
Itens = []
n = 1
while True:

    Produtos["item"] = str(input(f'Produto {n}: '))
    Produtos["preço"] = float(input(f'Preço {n}: '))
    n += 1
    Itens.append(Produtos.copy())
    msg = int(input("Para encerrar Digite [0] Continuar [1] : "))

    if msg == 0 :
        print("Obrigado , Volte sempre!")
        break

#print(Itens)
total = sum(Produtos.values())
for c, v in enumerate(Itens):
    print(f'{v["item"]} : $R {v["preço"]}')

print(total)