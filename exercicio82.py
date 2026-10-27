# Criando um vetor (lista) vazio para armazenar os valores
vetor = []

# Loop para solicitar os 11 valores ao usuário
for i in range(11):
    valor = input(f"Digite o {i+1}º valor: ")
    vetor.append(valor)

print("\n--- VALORES APRESENTADOS ---")

# Loop para exibir os valores com o separador entre as linhas
for i in range(11):
    print(vetor[i])
    
    # Adiciona o separador apenas entre as linhas (evita colocar após o último)
    if i < 10:
        print("----------------")
