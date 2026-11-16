numeros = [int(input()) for _ in range(5)]

pares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1

print(f"{pares} valores pares")