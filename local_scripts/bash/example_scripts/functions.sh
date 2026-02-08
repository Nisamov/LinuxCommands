#!/bin/bash

# Declaracion de funcion echo_hola
# Estas funciones son agrupaciones de comandos que realizan una tarea especifica, en este caso imprimir un mensaje en pantalla
function echo_hola() {
    echo "Hola!!"
}

# La llamada a la funcion se hace escribiendo su nombre, seguido de parentesis, aunque no es necesario escribir los parentesis si no se le van a pasar argumentos
echo_hola

function argumentos() {
    echo "El primer argumento es: $1"
    echo "El segundo argumento es: $2"
}
# Llamada a la funcion con argumentos
argumentos "Hola" "Mundo"
# En este caso devolverá "Hola Mundo"

# Funciones más avanzadas pueden devolver valores utilizando la palabra clave "return" o simplemente imprimiendo el resultado y capturándolo con una variable
function suma() {
    local resultado=$(( $1 + $2 ))
    echo $resultado
}
# Capturando el resultado de la función suma
resultado_suma=$(suma 5 10)
# Muestra por consola el resultado de la suma
echo "El resultado de la suma es: $resultado_suma"