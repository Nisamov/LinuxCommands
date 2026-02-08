#!/bin/bash

# Este script muestra los argumentos pasados por consola
echo "El primer argumento es: $1"
echo "El segundo argumento es: $2"
# Es posible pasarle un maximo de 9 argumentos, cada uno se accede con $1, $2, ..., $9

# Condicionales para verificar el valor del primer argumento
if [ "$1" == "hola" ]; then
    echo "¡Hola! Has ingresado el primer argumento como 'hola'."
elif [ "$1" == "adios" ]; then
    echo "¡Adiós! Has ingresado el primer argumento como 'adios'."
fi

# Bucle para restar el segundo argumento hasta que sea mayor que 0
while [ $2 -gt 0 ]; do
    echo "Restando... $2"
    $2=$(( $2 - 1 ))
done