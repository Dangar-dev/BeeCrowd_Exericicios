import math

while True:
    entrada = input().split()
    if entrada[0] == '0':
        break
    
    a, b, c = map(int, entrada)
    
    area_casa = a * b
    # Regra de três: area_casa está para c% assim como area_terreno está para 100%
    area_terreno = (area_casa * 100) / c
    
    lado = math.sqrt(area_terreno)
    # math.floor ou int() para truncar o valor
    print(int(lado))