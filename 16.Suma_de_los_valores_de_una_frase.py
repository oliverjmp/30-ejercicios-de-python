frase = input("Escribe una frase que contenga números: ")

suma = 0
numero_actual = ""

for caracter in frase:
    if caracter.isdigit():
        numero_actual += caracter
    else:
        if numero_actual != "":
            suma += int(numero_actual)
            numero_actual = ""

# Para capturar el último número si la frase termina en dígito
if numero_actual != "":
    suma += int(numero_actual)

print("La suma de los números es:", suma)
