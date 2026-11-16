import sys

def main():
    dados = sys.stdin.read().split()
    pos = 0
    while pos < len(dados):
        n = int(dados[pos]); pos += 1
        custo = int(dados[pos]); pos += 1
        melhor = 0
        atual = 0
        for _ in range(n):
            lucro = int(dados[pos]) - custo
            pos += 1
            atual = max(0, atual + lucro)
            melhor = max(melhor, atual)
        print(melhor)

main()