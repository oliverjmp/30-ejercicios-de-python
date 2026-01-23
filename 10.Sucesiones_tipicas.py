# Programa que genera los N primeros números de Fibonacci
# y los guarda en un archivo llamado fibonacci.txt

N = int(input("Introduce cuántos números de Fibonacci quieres generar: "))

fibonacci = []

# Generar la sucesión
a, b = 0, 1
for _ in range(N):
    fibonacci.append(a)
    a, b = b, a + b

# Mostrar por pantalla
print("\nLos primeros", N, "números de Fibonacci son:")
print(fibonacci)

# Guardar en fichero
with open("fibonacci.txt", "w") as fichero:
    for numero in fibonacci:
        fichero.write(str(numero) + "\n")

print("\nLos números han sido guardados en fibonacci.txt")
