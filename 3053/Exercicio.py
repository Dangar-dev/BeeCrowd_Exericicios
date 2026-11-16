n = int(input())
pos = input().strip()  # A, B ou C

for _ in range(n):
    mov = int(input().strip())
    if mov == 1:  # troca A e B
        if pos == "A":
            pos = "B"
        elif pos == "B":
            pos = "A"
    elif mov == 2:  # troca B e C
        if pos == "B":
            pos = "C"
        elif pos == "C":
            pos = "B"
    elif mov == 3:  # troca A e C
        if pos == "A":
            pos = "C"
        elif pos == "C":
            pos = "A"

print(pos)