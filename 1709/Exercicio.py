import sys
from math import gcd

def main():
    p = int(sys.stdin.readline())
    # destino (0-indexado) da carta na posição i
    dest = [0] * p
    n = p // 2
    for i in range(p):
        if i < n:
            dest[i] = 2 * i + 1
        else:
            dest[i] = 2 * (i - n)

    vis = [False] * p
    res = 1
    for i in range(p):
        if not vis[i]:
            tam = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = dest[j]
                tam += 1
            res = res * tam // gcd(res, tam)
    print(res)

main()