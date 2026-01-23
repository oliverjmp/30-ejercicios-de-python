# 1. Pedir números hasta que el usuario introduzca 0
lista = []
num = int(input("Introduce un número (0 para terminar): "))

while num != 0:
    lista.append(num)
    num = int(input("Introduce un número (0 para terminar): "))

print("\nLista completa:", lista)

# 2. Mostrar los números en posición par (índices pares)
print("\nNúmeros en posición par:")
for i in range(0, len(lista), 2):
    print(f"Posición {i}: {lista[i]}")

# 3. Mostrar los números en orden inverso
print("\nLista en orden inverso:")
print(lista[::-1])

# 4. Partir la lista en dos mitades
mitad = len(lista) // 2
primera_mitad = lista[:mitad]
segunda_mitad = lista[mitad:]

print("\nPrimera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)

# 5. Mostrar elementos de la primera mitad excepto el primero y el último
print("\nElementos de la primera mitad (sin primero ni último):")
if len(primera_mitad) > 2:
    print(primera_mitad[1:-1])
else:
    print("No hay suficientes elementos para mostrar.")

# 6. Mostrar máximo y mínimo de la segunda mitad
if len(segunda_mitad) > 0:
    print("\nMáximo de la segunda mitad:", max(segunda_mitad))
    print("Mínimo de la segunda mitad:", min(segunda_mitad))
else:
    print("\nLa segunda mitad está vacía.")
