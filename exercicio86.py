
vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

X = int(input("\nDigite o número X que deseja buscar: "))


quantidade = vetor.count(X)

print(f"\nO número {X} aparece {quantidade} vez(es) no vetor.")
