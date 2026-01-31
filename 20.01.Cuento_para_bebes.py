from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

cuento = """
PÁGINA 1
Había una vez un pequeño osito llamado Coco. 
Coco vivía en un bosque lleno de árboles altos y flores de muchos colores. 
Cada mañana, cuando el sol despertaba, Coco salía de su cueva para saludar a sus amigos:
la mariposa Azulita, el conejo Brinco y la tortuga Lenta.

Un día, Coco escuchó un sonido suave, como un susurro del viento.
“¿Quién anda ahí?”, preguntó Coco con curiosidad.
Entonces vio una pequeña luciérnaga que brillaba como una estrella.
“Hola, soy Chispa”, dijo la luciérnaga. “Estoy buscando mi hogar, pero me perdí”.

Coco sonrió y dijo: “No te preocupes, Chispa. Yo te ayudaré a encontrarlo”.
Y así comenzó una aventura llena de luz, risas y amistad.


PÁGINA 2
Coco y Chispa caminaron por el bosque, siguiendo pequeños destellos en el aire.
Cada vez que Chispa veía una luz, pensaba que era su familia, pero siempre era otra cosa:
una gota de rocío, un reflejo del río o una estrella traviesa escondiéndose entre las hojas.

Finalmente, llegaron a un árbol muy grande que brillaba suavemente.
“¡Ese es mi hogar!”, exclamó Chispa emocionada.
De entre las ramas salieron muchas luciérnagas que iluminaron el bosque entero.

Chispa abrazó a Coco con su luz cálida.
“Gracias por traerme de vuelta”, dijo.
Coco sonrió y respondió: “Los amigos siempre se ayudan”.

Y así, bajo un cielo lleno de estrellas, Coco regresó a su cueva,
feliz de haber vivido una nueva aventura.
"""

# -------------------------------
# Guardar archivo con ventana
# -------------------------------
Tk().withdraw()  # Oculta la ventana principal

ruta = asksaveasfilename(
    title="Guardar cuento como...",
    defaultextension=".txt",
    filetypes=[("Archivo de texto", "*.txt")]
)

if ruta:
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(cuento)
    print("Cuento guardado correctamente en:", ruta)
else:
    print("No se guardó el archivo.")
