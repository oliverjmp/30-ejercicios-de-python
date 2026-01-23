print("Este programa solicita tres números al usuario y muestra el máximo, el mínimo, los números pares e impares entre ellos.")
number = int(input("Introduce un número: "))
number2 = int(input("Introduce otro número: "))
number3 = int(input("Introduce un último número: "))

maximo = max(number, number2, number3)
minimo = min(number, number2, number3)

print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")

print("Números pares:")
for i in range(minimo, maximo + 1):
    if i % 2 == 0:
        print(i)

print("Números impares:")
for i in range(minimo, maximo + 1):
    if i % 2 != 0:
        print(i)
