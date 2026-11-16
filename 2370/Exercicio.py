N, T = map(int, input().split())

alunos = []

for _ in range(N):
    nome, habilidade = input().split()
    habilidade = int(habilidade)

    alunos.append((habilidade, nome))

# Maior habilidade primeiro
alunos.sort(reverse=True)

times = [[] for _ in range(T)]

for i, (habilidade, nome) in enumerate(alunos):
    time = i % T
    times[time].append(nome)

# Ordena os nomes dentro de cada time
for time in times:
    time.sort()

# Imprime
for i, time in enumerate(times):
    print(f"Time {i + 1}")

    for nome in time:
        print(nome)

    print()