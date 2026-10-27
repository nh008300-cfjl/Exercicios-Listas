
nomes = []
idades = []


for i in range(7):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    nomes.append(nome)
    idades.append(idade)

print("\n--- PESSOAS COM 18 ANOS OU MAIS ---")


for i in range(7):
    if idades[i] >= 18:
        print(nomes[i])
