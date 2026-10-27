vetor = []


for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

soma_impares = 0
multiplicacao_pares = 1

for i in range(10):
    if i % 2 != 0:
        # Posição ímpar (índices 1, 3, 5, 7, 9)
        soma_impares += vetor[i]
    else:
       
        multiplicacao_pares *= vetor[i]

print(f"\nA: Resultado da soma das posições ímpares: {soma_impares}")
print(f"B: Resultado da multiplicação das posições pares: {multiplicacao_pares}")
