
alunos = []
notas = []


for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append(nome)
    notas.append(nota)


media_turma = sum(notas) / 5

print(f"\nMédia das notas da turma: {media_turma:.2f}")
print("\n--- ALUNOS COM NOTA MENOR QUE 7 ---")


algum_aluno_abaixo = False
for i in range(5):
    if notas[i] < 7:
        print(f"Aluno: {alunos[i]} - Nota: {notas[i]}")
        algum_aluno_abaixo = True

if not algum_aluno_abaixo:
    print("Nenhum aluno ficou abaixo de 7!")
