def palabras_una_fila(palabras):
    fila1 = set("qwertyuiop")
    fila2 = set("asdfghjkl")
    fila3 = set("zxcvbnm")

    resultado = []

    for palabra in palabras:
        letras = set(palabra.lower())
        if letras.issubset(fila1) or letras.issubset(fila2) or letras.issubset(fila3):
            resultado.append(palabra)

    return resultado


entrada = input("Escribe palabras separadas por espacios: ")
lista = entrada.split()

print(palabras_una_fila(lista))
