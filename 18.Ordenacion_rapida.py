def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)


entrada = input("Escribe números separados por espacios: ")

# Convertir la entrada en una lista de enteros
lista_numeros = [int(x) for x in entrada.split()]

# Llamar a quicksort y mostrar el resultado
resultado = quicksort(lista_numeros)
print("Lista ordenada:", resultado)
