import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0]); pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos]); pos += 1
        p = [0] + [int(x) for x in data[pos:pos + n]]
        pos += n
        vis = [False] * (n + 1)
        ciclos = 0
        for i in range(1, n + 1):
            if not vis[i]:
                ciclos += 1
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = p[j]
        out.append(n - ciclos)
    print("\n".join(map(str, out)))

main()