number = int(input("Introduce un número entre el 10 y 20: "))

if 10 <= number <= 20:
    print(f"Tu número es {number}\n")

    print("Números desde 1 hasta tu número:")
    for i in range(1, number + 1):
        print(i)

    print("\nNúmeros desde tu número hasta 30:")
    for i in range(number, 31):
        print(i)
else:
    print("El número no está entre 10 y 20.")

