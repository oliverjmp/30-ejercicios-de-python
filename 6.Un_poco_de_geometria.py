import math

print("Introduce las coordenadas del primer punto:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("\nIntroduce las coordenadas del segundo punto:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Distancia entre los dos puntos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Punto medio
punto_medio_x = (x1 + x2) / 2
punto_medio_y = (y1 + y2) / 2

print(f"\nLa distancia entre los dos puntos es: {distancia}")
print(f"El punto medio es: ({punto_medio_x}, {punto_medio_y})")
