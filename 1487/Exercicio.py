import sys

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    caso = 0
    out = []
    while pos + 1 < len(tokens):
        n = int(tokens[pos]); t = int(tokens[pos + 1])
        pos += 2
        if n == 0:
            break
        caso += 1
        itens = []
        for _ in range(n):
            d = int(tokens[pos]); p = int(tokens[pos + 1])
            pos += 2
            itens.append((d, p))

        dp = [0] * (t + 1)
        for d, p in itens:
            if d == 0:
                continue
            for tt in range(d, t + 1):
                v = dp[tt - d] + p
                if v > dp[tt]:
                    dp[tt] = v

        out.append("Instancia %d" % caso)
        out.append(str(dp[t]))
        out.append("")

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))

main()