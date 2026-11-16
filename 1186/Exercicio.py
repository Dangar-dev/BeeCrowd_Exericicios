operacao = input().strip().upper()
soma = 0.0
contador = 0

for i in range(12):
    for j in range(12):
        valor = float(input())
        # Abaixo da diagonal secundária: linha + coluna > 11
        if i + j > 11:
            soma += valor
            contador += 1

if operacao == 'S':
    print(f"{soma:.1f}")
else:
    media = soma / contador
    print(f"{media:.1f}")