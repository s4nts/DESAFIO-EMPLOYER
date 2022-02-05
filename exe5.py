nome = input("Insire um nome:")
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0

for letra in nome: 
    if letra in vogais:
        contador += 1

print("O nome tem ", contador, "vogais")