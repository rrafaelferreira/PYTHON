# Crie um sistema que ajude um caixa de loja a registrar vendas até que o cliente finalize a compra: Pergunte ao usuário o preço de cada item. Use um loop while para continuar somando os valores enquanto o usuário não digitar 0, que indica o fim da compra. Após o término, exiba o total da compra no formato: "Total da compra: R$ X". A cada item adicionado, exiba também o valor acumulado até o momento. Dica: use uma variável para acumular o total e outra para armazenar o valor do item informado pelo usuário.

total = 0

while True:
    preco = float(input("Informe o preço do item. (Ou digite '0' para encerrar o programa): R$ "))

    if preco == 0:
        break

    total += preco
    print(f"Total parcial: R$ {total:.2f}")
print(f"Total da compra: R$ {total:.2f}")    