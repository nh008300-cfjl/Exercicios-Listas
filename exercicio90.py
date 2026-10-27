
X = int(input("Digite o número inteiro X que deseja buscar: "))

vetor = []
print("\n--- AGORA DIGITE OS 32 NÚMEROS DO VETOR ---")


for i in range(32):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)


total_ocorrencias = vetor.count(X)

print(f"\nO número {X} apareceu {total_ocorrencias} vez(es) no vetor.")
