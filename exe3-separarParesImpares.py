lista = [1,3,35,40,85,123,121,209,200,305,350]
print("A lista inicial é:", lista)

def vericaImpares(numero):
    if(int(numero / 2) != float(numero / 2)) :
        return numero

def vericaPares(numero):
    if(int(numero / 2) == float(numero / 2)) :
        return numero

impares = list(map(vericaImpares, lista))
impares = list(filter(None, impares))
print("Os números ímpares são:", impares)
pares = list(map(vericaPares, lista))
pares = list(filter(None, pares))
print("Os números pares são:", pares)

feedback = input('gostou do programa? ')