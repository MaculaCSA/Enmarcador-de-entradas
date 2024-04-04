import os
import re

# Carpeta del proyecto
ruta_carpeta = r"./img"

# Comprobar si la carpeta existe, si no existe, crearla
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

# Recorre todos los archivos en la carpeta
for nombre_archivo in os.listdir(ruta_carpeta):
    if nombre_archivo.endswith(".png"):
        # Nombre del archivo sin extensión
        nombre_archivo_sin_ext = os.path.splitext(nombre_archivo)[0]
        # ID del archivo (el mismo que el nombre del archivo sin extensión)
        archivo_id = nombre_archivo_sin_ext

        # Ruta al archivo origen.svg
        ruta_archivo_origen = os.path.join(ruta_carpeta, "origen.svg")

        # Lee el archivo origen.svg y reemplaza el texto
        with open(ruta_archivo_origen, "r") as archivo_origen:
            svg_contenido = archivo_origen.read()
            # Reemplaza "0.png" por el nombre del archivo actual y "NUMEROS ESPECIALES" por el ID del archivo
            svg_contenido_modificado = re.sub(r"0.png", nombre_archivo, svg_contenido)
            svg_contenido_modificado = re.sub(r"NUMEROS ESPECIALES", archivo_id, svg_contenido_modificado)

        # Escribe el nuevo archivo svg
        ruta_archivo_svg = os.path.join(ruta_carpeta, f"{nombre_archivo_sin_ext}.svg")
        with open(ruta_archivo_svg, "w") as archivo_svg:
            archivo_svg.write(svg_contenido_modificado)