#!/bin/bash

# Este script muestra cómo usar pipes para conectar comandos en bash.
# El comando 'ls' lista los archivos en el directorio actual, y su salida se pasa a 'grep' para filtrar solo los archivos que contienen "example" en su nombre.
ls -l | grep "example"
# Como resultado, solo se mostrarán los archivos que contienen "example" en su nombre, junto con sus detalles.
echo "Output:"
echo "-rw-r--r-- 1 user user 1234 Jun 10 12:34 example_file.txt" 