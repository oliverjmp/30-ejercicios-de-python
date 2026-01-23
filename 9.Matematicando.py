import math

# ------------------ PARTE 1: DOS NÚMEROS ------------------

print("=== Cálculo de MCD y MCM de dos números ===")
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

mcd_2 = math.gcd(a, b)
mcm_2 = abs(a * b) // mcd_2

print(f"\nMCD({a}, {b}) = {mcd_2}")
print(f"MCM({a}, {b}) = {mcm_2}")

# ------------------ PARTE 2: LISTA DE 5 NÚMEROS ------------------

print("\n=== Ahora introduce 5 números para una lista ===")
lista = []

for i in range(5):
    num = int(input(f"Número {i+1}: "))
    lista.append(num)

# Función para calcular MCM de dos números
def mcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# MCD de toda la lista
mcd_lista = lista[0]
for n in lista[1:]:
    mcd_lista = math.gcd(mcd_lista, n)

# MCM de toda la lista
mcm_lista = lista[0]
for n in lista[1:]:
    mcm_lista = mcm(mcm_lista, n)

print(f"\nLista introducida: {lista}")
print(f"MCD de la lista = {mcd_lista}")
print(f"MCM de la lista = {mcm_lista}")
