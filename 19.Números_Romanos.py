def romano_a_entero(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0

    for letra in romano[::-1]:
        valor = valores[letra]
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor

    return total


def entero_a_romano(numero):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    resultado = ""

    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor

    return resultado


# -------------------------------
#       MENÚ INTERACTIVO
# -------------------------------
while True:
    print("\nCONVERSOR ROMANO ↔ ENTERO")
    print("1. Convertir de romano a entero")
    print("2. Convertir de entero a romano")
    print("3. Salir")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        romano = input("Introduce un número romano: ").upper()
        print("Resultado:", romano_a_entero(romano))

    elif opcion == "2":
        numero = int(input("Introduce un número entero: "))
        print("Resultado:", entero_a_romano(numero))

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")

    # Preguntar si desea continuar
    continuar = input("\n¿Quieres hacer otra conversión? (s/n): ").lower()
    if continuar != "s":
        print("Saliendo del programa...")
        break