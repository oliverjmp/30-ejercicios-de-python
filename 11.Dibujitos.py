n = int(input("Introduce un número para el tamaño de las figuras: "))

# 1) MEDIA PUNTA DE FLECHA HACIA ABAJO
print("\n1) MEDIA PUNTA DE FLECHA HACIA ABAJO")
for i in range(n, 0, -1):
    print("*" * i)

# 2) RECTÁNGULO SIN RELLENO
print("\n2) RECTÁNGULO SIN RELLENO")
print("*" * n)
for i in range(n - 2):
    print("*" + " " * (n - 2) + "*")
if n > 1:
    print("*" * n)

# 3) FLECHA ARRIBA + LÍNEA + FLECHA ABAJO (FIGURA FIJA)
print("\n3) FLECHA ARRIBA + LÍNEA + FLECHA ABAJO")

print("  *")
print(" ***")
print("*****")
print("  |")
print("  |")
print(" ***")
print("  *")

# 4) PUNTA DE FLECHA COMPLETA HACIA ARRIBA
print("\n4) PUNTA DE FLECHA COMPLETA HACIA ARRIBA")

for i in range(1, n + 1):
    espacios = n - i
    estrellas = 2 * i - 1
    print(" " * espacios + "*" * estrellas)

