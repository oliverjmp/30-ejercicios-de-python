import string
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def limpiar_texto(texto):
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, " ")
    return texto


def analizar_texto(texto):
    texto = limpiar_texto(texto)
    palabras = texto.split()

    if not palabras:
        print("No se encontraron palabras en el texto.")
        return

    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    total_palabras = len(palabras)
    palabras_unicas = len(frecuencias)

    max_frec = max(frecuencias.values())
    mas_frecuentes = [p for p, f in frecuencias.items() if f == max_frec]

    longitud_promedio = sum(len(p) for p in palabras) / total_palabras

    print("\n--- RESULTADOS DEL ANÁLISIS ---")
    print("Total de palabras:", total_palabras)
    print("Palabras únicas:", palabras_unicas)
    print("Palabra(s) más frecuente(s):", ", ".join(mas_frecuentes))
    print("Frecuencia:", max_frec)
    print("Longitud promedio:", round(longitud_promedio, 2))

    print("\nTop 10 palabras más frecuentes:")
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, freq in top10:
        print(f"{palabra}: {freq}")


def seleccionar_archivo_txt():
    root = Tk()
    root.withdraw()                 # Oculta la ventana principal
    root.attributes('-topmost', True)  # Fuerza la ventana al frente
    ruta = askopenfilename(
        title="Selecciona un archivo .txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    root.destroy()
    return ruta


# -------------------------------
#       MENÚ PRINCIPAL
# -------------------------------
while True:
    print("\nANALIZADOR DE TEXTO")
    print("1. Pegar texto manualmente")
    print("2. Seleccionar archivo .txt")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        texto = input("\nPega el texto a analizar:\n")
        analizar_texto(texto)

    elif opcion == "2":
        ruta = seleccionar_archivo_txt()
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    texto = f.read()
                analizar_texto(texto)
            except Exception as e:
                print("Error al leer el archivo:", e)
        else:
            print("No seleccionaste ningún archivo.")

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")
