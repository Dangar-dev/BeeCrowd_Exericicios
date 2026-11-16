a, b, c = map(int, input().split())

# Caso 1: Desceu no 1º-2º, mas subiu ou parou no 2º-3º
if a > b and b <= c:
    print(":)")

# Caso 2: Subiu no 1º-2º, mas desceu ou parou no 2º-3º
elif a < b and b >= c:
    print(":(")

# Caso 3: Subiu em ambos, mas subiu menos (ou igual) no segundo intervalo
elif a < b and b < c:
    if (c - b) < (b - a):
        print(":(")
    else:
        print(":)")

# Caso 4: Desceu em ambos, mas desceu menos no segundo intervalo
elif a > b and b > c:
    if (b - c) < (a - b):
        print(":)")
    else:
        print(":(")

# Caso 5: Estabilidade no início
elif a == b:
    if c > b:
        print(":)")
    else:
        print(":(")