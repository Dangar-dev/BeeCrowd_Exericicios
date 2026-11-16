# -*- coding: utf-8 -*-

renda = float(input())

if renda <= 2000.00:
    print("Isento")
elif renda <= 3000.00:
    print(f"R$ {(renda - 2000) * 0.08:.2f}")
elif renda <= 4500.00:
    print(f"R$ {(80 + (renda - 3000) * 0.18):.2f}")
else:
    print(f"R$ {(350 + (renda - 4500) * 0.28):.2f}")
