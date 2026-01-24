def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

inicio = int(input("Año de inicio: "))
fin = int(input("Año de fin: "))

print(f"Años bisiestos entre {inicio} y {fin}:")

for anio in range(inicio, fin + 1):
    if es_bisiesto(anio):
        print(anio)
