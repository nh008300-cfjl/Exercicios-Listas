vetor = []
impares = []


for i in range(21):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)
    
    
    if numero % 2 != 0:
        impares.append(numero)

print("\n--- RESULTADO DA ANÁLISE ---")


if len(impares) == 0:
    print("Todos são pares.")
else:
    print("Existem números ímpares.")
    
    
    impares.sort()
    
    print("Números ímpares encontrados (em ordem crescente):")
    for impar in impares:
        print(impar)
