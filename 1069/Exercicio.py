N = int(input())

for _ in range(N):
    linha = input().strip()

    pilha = []
    diamantes = 0

    for caractere in linha:
        if caractere == '<':
            pilha.append('<')

        elif caractere == '>':
            if pilha:
                pilha.pop()
                diamantes += 1

    print(diamantes)