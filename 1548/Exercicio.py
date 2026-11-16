N = int(input())

for _ in range(N):
    M = int(input())

    notas = list(map(int, input().split()))

    ordenada = sorted(notas, reverse=True)

    resposta = 0

    for i in range(M):
        if notas[i] == ordenada[i]:
            resposta += 1

    print(resposta)