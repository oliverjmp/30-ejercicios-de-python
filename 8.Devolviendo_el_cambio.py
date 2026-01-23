# Programa para calcular la mínima cantidad de monedas necesarias

# Lista de monedas disponibles (en euros)
monedas = [2, 1, 0.5, 0.2, 0.05, 0.02, 0.01]

# Entrada del usuario (acepta coma o punto)
D = float(input("Introduce una cantidad de dinero (ej: 12.37): ").replace(",", "."))

print("\nDesglose mínimo de monedas:")

for moneda in monedas:
    cantidad = int(D // moneda)  # cuántas monedas de este tipo caben
    if cantidad > 0:
        print(f"{cantidad} moneda(s) de {moneda}€")
    D = round(D % moneda, 2)  # resto, redondeado para evitar errores de coma flotante
    if D == 0:
        break   # si ya no queda nada, salimos del bucle
