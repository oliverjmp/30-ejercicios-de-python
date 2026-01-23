numeros = []

# Pedir 10 números al usuario
for i in range(10):
    num = int(input(f"Introduce el número {i+1}: "))
    numeros.append(num)

print("\nResultados:")
for num in numeros:
    # Determinar si es positivo o negativo
    if num >= 0:
        tipo = "POSITIVO"
    else:
        tipo = "NEGATIVO"
    
    # Determinar si está repetido
    if numeros.count(num) > 1:
        repetido = "REPETIDO"
    else:
        repetido = "NO REPETIDO"
    
    print(f"{num} → {tipo} | {repetido}")
