import sys
import heapq
from collections import deque

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    out = []
    while pos < len(tokens):
        n = int(tokens[pos])
        pos += 1

        pilha = []
        fila = deque()
        heap = []  # max-heap usando valores negativos

        ok_s = ok_q = ok_p = True

        for _ in range(n):
            cmd = int(tokens[pos])
            x = int(tokens[pos + 1])
            pos += 2

            if cmd == 1:
                pilha.append(x)
                fila.append(x)
                heapq.heappush(heap, -x)
            else:
                if ok_s:
                    if not pilha or pilha.pop() != x:
                        ok_s = False
                if ok_q:
                    if not fila or fila.popleft() != x:
                        ok_q = False
                if ok_p:
                    if not heap or -heapq.heappop(heap) != x:
                        ok_p = False

        total = ok_s + ok_q + ok_p
        if total == 0:
            out.append("impossible")
        elif total > 1:
            out.append("not sure")
        elif ok_s:
            out.append("stack")
        elif ok_q:
            out.append("queue")
        else:
            out.append("priority queue")

    print("\n".join(out))

main()