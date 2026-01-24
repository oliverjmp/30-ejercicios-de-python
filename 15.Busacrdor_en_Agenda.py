def cargar_agenda(archivo):
    contactos = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                id_, nombre, apellido, telefono = linea.split(";")
                contactos.append({
                    "id": int(id_),
                    "nombre": nombre,
                    "apellido": apellido,
                    "telefono": telefono
                })
    return contactos


def buscar_por_nombre(contactos, nombre):
    return [c for c in contactos if c["nombre"].lower() == nombre.lower()]


def buscar_por_apellido(contactos, apellido):
    return [c for c in contactos if c["apellido"].lower() == apellido.lower()]


def buscar_por_id(contactos, id_buscar):
    return [c for c in contactos if c["id"] == id_buscar]


def mostrar_contactos(lista):
    if not lista:
        print("No se encontraron resultados.")
        return
    for c in lista:
        print(f"ID: {c['id']} - {c['nombre']} {c['apellido']} - {c['telefono']}")


def main():
    archivo = "agenda.txt"
    contactos = cargar_agenda(archivo)

    while True:
        print("\n--- MENÚ DE BÚSQUEDA ---")
        print("1. Buscar por nombre")
        print("2. Buscar por apellido")
        print("3. Buscar por ID")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre: ")
            resultados = buscar_por_nombre(contactos, nombre)
            mostrar_contactos(resultados)

        elif opcion == "2":
            apellido = input("Introduce el apellido: ")
            resultados = buscar_por_apellido(contactos, apellido)
            mostrar_contactos(resultados)

        elif opcion == "3":
            id_buscar = int(input("Introduce el ID: "))
            resultados = buscar_por_id(contactos, id_buscar)
            mostrar_contactos(resultados)

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
