lista = []
num1 = input("Insira o primeiro número: ")
lista.append(float(num1))
num2 = input("Insira o segundo número: ")
lista.append(float(num2))
num3 = input("Insira o terceiro número: ")
lista.append(float(num3))
num4 = input("Insira o quarto número: ")
lista.append(float(num4))
num5 = input("Insira o quinto número: ")
lista.append(float(num5))

print("Os números inseridos foram:", lista)
lista.sort(reverse=True)

print("A lista em ordem decrescente é", lista)