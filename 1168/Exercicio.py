# Segmentos por dígito (0-9)
leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n = int(input())
for _ in range(n):
    numero = input().strip()
    total = sum(leds[int(d)] for d in numero)
    print(f"{total} leds")