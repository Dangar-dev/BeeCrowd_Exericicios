import sys

dados = list(map(int, sys.stdin.read().split()))

N = dados[0]
numeros = dados[1:N + 1]

frequencia = {}

for numero in numeros:
    if numero in frequencia:
        frequencia[numero] += 1
    else:
        frequencia[numero] = 1

for numero in sorted(frequencia):
    print(f"{numero} aparece {frequencia[numero]} vez(es)")