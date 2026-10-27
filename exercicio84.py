vetor = []


for i in range(12):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)


print("\n--- NÚMEROS PARES ---")
for numero in vetor:
    if numero % 2 == 0:
        print(numero)

print("\n--- NÚMEROS ÍMPARES ---")
for numero in vetor:
    if numero % 2 != 0:
        print(numero)
