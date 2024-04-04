# Convertidor SVG a PNG

Este repositorio contiene un par de scripts en Python diseñados para trabajar con archivos SVG y PNG. Estos scripts permiten realizar dos tareas principales:

1. **Modificación de archivos SVG:**
   - El script `modificar_svg.py` se encarga de recorrer una carpeta de archivos PNG y modificar un archivo SVG base con los nombres de estos archivos, generando así nuevos archivos SVG modificados. Esto es útil para crear variantes de un mismo archivo SVG con nombres de archivos específicos incrustados en ellos.

2. **Conversión de archivos SVG a PNG:**
   - El script `convertir_svg_a_png.py` convierte los archivos SVG en una carpeta dada en archivos PNG de alta resolución. Utiliza el software Inkscape para llevar a cabo esta conversión.

## Uso

### Modificar archivos SVG

Antes de ejecutar el script `modificar_svg.py`, asegúrate de tener una carpeta llamada `img` en la misma ubicación que el script, que contenga los archivos PNG que quieres utilizar para modificar tus archivos SVG base. Luego, simplemente ejecuta el script y se generarán los archivos SVG modificados en la misma carpeta.

```bash
python modificar_svg.py
```

### Convertir archivos SVG a PNG

Antes de ejecutar el script `convertir_svg_a_png.py`, asegúrate de tener una carpeta llamada `img` en la misma ubicación que el script, que contenga los archivos SVG que deseas convertir. El script creará una carpeta `PNG` dentro de la carpeta `img` donde guardará los archivos PNG generados.

```bash
python convertir_svg_a_png.py
```

## Requisitos

- Python 3.x
- Inkscape (para la conversión de SVG a PNG)