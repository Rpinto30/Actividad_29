from funcinoes import *
while True:
    print("Menu de metodos de ordenamiento".center(50, "=")+
          "\n1. Ordenar lista usando BubbleSort\n"
          "2. Numero aleatorio usando BogoSort\n"
          "3. Ordenar edades con Select\n"
          "4. Ordenar lista con Quicksort"
          "5. Salir")
    select = (input("selecciona una opcion: "))
    match select:
        case "1":
            print(f"La lista ordenada está lista! {bubble(pedir())}")
        case "2":
            print(bogo(pedir()))
        case "3":
            print(sort(pedir()))
        case "4":
            print(quicksort(pedir()))
        case "5":
            print("Saliendo del sistema")
            break
        case _: break
