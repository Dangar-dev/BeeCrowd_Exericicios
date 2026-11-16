import sys

def main():
    dados = sys.stdin.read().split()
    pos = 0
    n = int(dados[pos]); pos += 1
    for _ in range(n):
        m = int(dados[pos]); pos += 1
        precos = {}
        for _ in range(m):
            nome = dados[pos]
            preco = float(dados[pos + 1])
            precos[nome] = preco
            pos += 2
        p = int(dados[pos]); pos += 1
        total = 0.0
        for _ in range(p):
            nome = dados[pos]
            qtd = int(dados[pos + 1])
            total += precos[nome] * qtd
            pos += 2
        print(f"R$ {total:.2f}")

main()