name = input("Introduce tu nombre: ")
age = input("Introduce tu edad: ")
height = int(input("Introduce tu altura en cm: "))
height1=height / 100
metros = height // 100
centimetros = height % 100

print(f"Hola {name}, tienes {age} años y mides {height1} metros.")
print(f"El usuario {name}, tiene {age} años y mide {metros} metro(s) y {centimetros} centímetro(s)")
