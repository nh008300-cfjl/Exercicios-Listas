
vetor_X = []
vetor_Y = []

print("--- ENTRADA DE DADOS PARA O VETOR X ---")
for i in range(8):
    valor = int(input(f"Digite o {i+1}º valor de X: "))
    vetor_X.append(valor)

print("\n--- ENTRADA DE DADOS PARA O VETOR Y ---")
for i in range(8):
    valor = int(input(f"Digite o {i+1}º valor de Y: "))
    vetor_Y.append(valor)

print("\n--- RESULTADO DA MULTIPLICAÇÃO (X * Y) ---")
for i in range(8):
    resultado = vetor_X[i] * vetor_Y[i]
    print(f"{vetor_X[i]} x {vetor_Y[i]} = {resultado}")
