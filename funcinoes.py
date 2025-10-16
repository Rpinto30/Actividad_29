import random
def bubble(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            print(f"Comparando {lista[i]} y {lista[j]}")
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            print(lista)
    return lista

def sort(lista):
    for i in range(len(lista)-1):
        _min = i
        for j in range(i+1, len(lista)):
            if lista[_min] > lista[j]:
                lista[j], lista[_min] = lista[_min], lista[j]
            print(f"Pasando {_min} a la izquierda...",lista)
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    piv = lista[len(lista)//2]
    menores = [x for x in lista if x <piv]
    iguales = [x for x in lista if x ==piv]
    mayores = [x for x in lista if x >piv]
    print(f"Menores: {menores}, iguales={iguales}, mayores={mayores} | Pivote={piv}")
    return quicksort(menores) + iguales + quicksort(mayores)

def bogo(lista):
    intentos = 0
    while not all(lista[i] <= lista[i+1] for i in range(len(lista)-1)):
        random.shuffle(lista)
        print(f"{lista}".center(150))
        intentos += 1
    return f"{lista}, El numero ganador es {intentos}"


def pedir():
    lista = []
    print("INGRESA UNA LISTA DE DATOS".center(20, "*"))
    n = int(input("Ingresa cuantos datos necesitas: "))
    for j in range(n):
        lista.append(input(f"  -Ingresa el dato {j+1}: "))
    return lista
