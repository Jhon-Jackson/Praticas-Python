itens = {}
produtos = []

itens["nome"] = str(input("seu nome: "))
itens["idade"] = int(input('Sua idade: '))
produtos.append(itens.copy())
print(produtos)
print(produtos[0]['nome'])
print(produtos[0]['idade'])