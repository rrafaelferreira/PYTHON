# Um supermercado quer controlar produtos e preços. Crie uma lista de produtos: "arroz", "feijão", "macarrão". Crie uma tupla com os preços correspondentes: 5.50, 7.20, 4.30. Pergunte ao usuário o nome de um produto e: Se estiver na lista, exiba o preço correspondente. Se não estiver, informe que o produto não está disponível. Exiba todos os produtos com seus preços.

produtos = ["arroz", "feijão", "macarrão"]
precos = (5.50, 7.20, 4.30)

nomep = input("Digite o nome do produto: ").lower()

if nomep in produtos:
    i = produtos.index(nomep)
    print(f"Preço: R$ {precos[i]:.2f}")
else:
    print("Produto não disponível.")

print("\nLista de produtos:")
for nome, preco in zip(produtos, precos):
    print(f"{nome} - R$ {preco:.2f}")