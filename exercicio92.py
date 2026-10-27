vetor1 = []
vetor2 = []
valores_comuns = []

print("--- ENTRADA DE DADOS: PRIMEIRO VETOR (10 VALORES) ---")
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor1.append(valor)

print("\n--- ENTRADA DE DADOS: SEGUNDO VETOR (12 VALORES) ---")
for i in range(12):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor2.append(valor)


for elemento in vetor1:
    if elemento in vetor2 and elemento not in valores_comuns:
        valores_comuns.append(elemento)

print("\n--- VALORES EM COMUM (ORDEM DECRESCENTE) ---")
if len(valores_comuns) == 0:
    print("Nenhum valor em comum foi encontrado.")
else:
   
    valores_comuns.sort(reverse=True)
    for valor in valores_comuns:
        print(valor)
