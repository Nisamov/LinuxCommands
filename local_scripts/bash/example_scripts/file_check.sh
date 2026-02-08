#!/bin/bash

# Este script comprueba la existencia de archivos y directorios en el sistema
mkdir -p /tmp/example_dir
touch /tmp/example_file.txt

# Comprobamos si el archivo existe
if [ -f /tmp/example_file.txt ]; then
    echo "El archivo /tmp/example_file.txt existe."
else
    echo "El archivo /tmp/example_file.txt no existe."
fi
# Comprobamos si el directorio existe
if [ -d /tmp/example_dir ]; then
    echo "El directorio /tmp/example_dir existe."
else
    echo "El directorio /tmp/example_dir no existe."
fi

# Se usa '-f' para comprobar ficheros y  '-d' para directorios