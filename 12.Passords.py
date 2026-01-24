import re

def validar_password(password):
    tiene_mayus = re.search(r"[A-Z]", password)
    tiene_minus = re.search(r"[a-z]", password)
    tiene_numero = re.search(r"[0-9]", password)
    tiene_especial = re.search(r"[^\w\s]", password)  # símbolo especial
    longitud_ok = len(password) >= 10

    if (tiene_mayus and tiene_minus and tiene_numero and 
        tiene_especial and longitud_ok):
        return True
    else:
        return False

password = input("Introduce tu contraseña: ")

if validar_password(password):
    print("✔ La contraseña es válida.")
else:
    print("✘ La contraseña NO cumple los requisitos.")
