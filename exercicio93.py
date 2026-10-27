frase = input("Digite uma frase: ")

vogais_padrao = "aeiou"
consoantes_padrao = "bcdfghjklmnpqrstvwxyz"

total_vogais = 0
total_consoantes = 0
total_outros = 0


for caractere in frase:
    
    char_min = caractere.lower()
    
    if char_min in vogais_padrao:
        total_vogais += 1
    elif char_min in consoantes_padrao:
        total_consoantes += 1
    else:
        total_outros += 1

print("\n--- RESULTADO DA CONTAGEM ---")
print(f"Vogais: {total_vogais}")
print(f"Consoantes: {total_consoantes}")
print(f"Outros caracteres: {total_outros}")
