# Dada a lista temperaturas = [30, 32, 31, 28, 29], calcule a média usando for.

temperaturas = [30, 32, 31, 28, 29]

soma = 0

for i in temperaturas:
    soma += i

media = soma / len(temperaturas)
print(f"Media:{media:.2f}")    