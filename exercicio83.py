vetor = []


for i in range(18):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

print("\n--- NÚMEROS EM ORDEM INVERSA ---")


for i in range(17, -1, -1):
    print(vetor[i])
