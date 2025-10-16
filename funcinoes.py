import random
def bubble(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
bubble([14, 18, 13, 11, 8, 50, 25])

def sort(lista):
    for i in range(len(lista)-1):
        _min = i
        for j in range(i+1, len(lista)):
            if lista[_min] > lista[j]:
                lista[j], lista[_min] = lista[_min], lista[j]
    return lista

def quicksort(lista):
    if len(lista) <= 1: return lista
    piv = lista[len(lista)//2]
    menores = [x for x in lista if x <piv]
    iguales = [x for x in lista if x ==piv]
    mayores = [x for x in lista if x >piv]
    return quicksort(menores) + iguales + quicksort(mayores)

def bogo(lista):
    intentos = 0
    while not all(lista[i] <= lista[i+1] for i in range(len(lista)-1)):
        random.shuffle(lista)
        print(f"{lista}".center(150))
        intentos += 1
    return f"{lista}, El numero ganador de la rifa es {intentos}"
bogo([8, 9, 6, 3])

