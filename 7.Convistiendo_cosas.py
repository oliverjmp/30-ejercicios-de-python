def decimal_a_todos():
    # Acepta coma o punto como separador decimal
    entrada = input("Introduce un número decimal: ").replace(",", ".")
    decimal = float(entrada)

    # Las bases solo funcionan con enteros → convertimos la parte entera
    entero = int(decimal)

    print(f"\nParte entera usada para conversiones: {entero}")
    print(f"Binario: {bin(entero)[2:]}")
    print(f"Octal: {oct(entero)[2:]}")
    print(f"Hexadecimal: {hex(entero)[2:].upper()}")


def binario_a_decimal():
    binario = input("Introduce un número binario: ")
    decimal = int(binario, 2)
    print(f"Decimal: {decimal}")


def octal_a_decimal():
    octal = input("Introduce un número octal: ")
    decimal = int(octal, 8)
    print(f"Decimal: {decimal}")


def hexadecimal_a_decimal():
    hexa = input("Introduce un número hexadecimal: ")
    decimal = int(hexa, 16)
    print(f"Decimal: {decimal}")


# ---------------- MENÚ PRINCIPAL ----------------

while True:
    print("\n===== CONVERSOR NUMÉRICO =====")
    print("1. Decimal → Binario / Octal / Hexadecimal")
    print("2. Binario → Decimal")
    print("3. Octal → Decimal")
    print("4. Hexadecimal → Decimal")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        decimal_a_todos()
    elif opcion == "2":
        binario_a_decimal()
    elif opcion == "3":
        octal_a_decimal()
    elif opcion == "4":
        hexadecimal_a_decimal()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

