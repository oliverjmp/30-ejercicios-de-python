import random
import os

ARCHIVO = "agenda.txt"

def obtener_siguiente_id():
    if not os.path.exists(ARCHIVO):
        return 1
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        if not lineas:
            return 1
        # Última línea -> primer campo es el ID
        ultima_linea = lineas[-1].strip()
        ultimo_id = int(ultima_linea.split(";")[0])
        return ultimo_id + 1

def generar_nombre_falso():
    nombres = ["Carlos", "Lucía", "Mateo", "Ana", "Javier", "Sofía", "Diego", "Elena"]
    apellidos = ["Pérez", "García", "López", "Martínez", "Rodríguez", "Sánchez", "Morales", "Torres"]
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    return nombre, apellido

def generar_telefono_falso():
    codigos_pais = ["+34", "+58", "+52", "+57", "+1"]
    codigo = random.choice(codigos_pais)
    numero = "".join(str(random.randint(0, 9)) for _ in range(9))  # 9 dígitos
    return f"{codigo} {numero}"

def guardar_contacto(id_contacto, nombre, apellido, telefono):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        # Formato: ID;Nombre;Apellido;Teléfono
        f.write(f"{id_contacto};{nombre};{apellido};{telefono}\n")

def main():
    cantidad = int(input("¿Cuántos contactos falsos quieres generar? "))
    for _ in range(cantidad):
        id_contacto = obtener_siguiente_id()
        nombre, apellido = generar_nombre_falso()
        telefono = generar_telefono_falso()
        guardar_contacto(id_contacto, nombre, apellido, telefono)
        print(f"Contacto generado: {id_contacto} - {nombre} {apellido} - {telefono}")

    print(f"\nContactos guardados en '{ARCHIVO}'")

if __name__ == "__main__":
    main()
