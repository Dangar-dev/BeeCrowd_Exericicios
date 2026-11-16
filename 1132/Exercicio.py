# one=3, two=3, three=5 letras
n = int(input())
for _ in range(n):
    word = input().strip()
    if len(word) == 3:   # "one" ou "two"
        # Conta diferenças com "one" e "two"
        diff_one = sum(a != b for a, b in zip(word, "one"))
        diff_two = sum(a != b for a, b in zip(word, "two"))
        if diff_one <= 1:
            print(1)
        else:
            print(2)
    else:  # len == 5, "three"
        print(3)