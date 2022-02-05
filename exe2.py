lista = []
num1 = input("Insira o primeiro número: ")
lista.append(float(num1))
num2 = input("Insira o segundo número: ")
lista.append(float(num2))
num3 = input("Insira o terceiro número: ")
lista.append(float(num3))
num4 = input("Insira o quarto número: ")
lista.append(float(num4))

print("Os numero inseridos foram:", lista)
lista.sort()
print("A lsita ordenada em ordem crescente é:", lista)
menor = lista[0]
maior = lista[-1]
print("O mais baixo valor da lista é: ", menor)
print("O mais maior valor da lista é: ", maior)
media = (menor + maior) / 2
print("A média do menor número para o maior é:", media)
