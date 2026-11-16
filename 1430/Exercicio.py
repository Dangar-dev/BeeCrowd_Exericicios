import sys

VAL = {'W': 64, 'H': 32, 'Q': 16, 'E': 8, 'S': 4, 'T': 2, 'X': 1}

def main():
    out = []
    for linha in sys.stdin:
        linha = linha.strip()
        if linha == '*':
            break
        if not linha:
            continue
        cont = 0
        for compasso in linha.split('/'):
            if compasso and sum(VAL[c] for c in compasso) == 64:
                cont += 1
        out.append(str(cont))
    print("\n".join(out))

main()