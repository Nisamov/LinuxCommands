#!/bin/bash

# Este script muestra por consola un mensaje
echo "Mensaje Mostrado Por Pantalla (Terminal)"

# Es posible mostrar contenido con colores utilizando códigos de escape ANSI
# Ejemplo de texto en rojo
echo -e "\e[31mEste texto es rojo\e[0m"
# Ejemplo de texto en verde
echo -e "\e[32mEste texto es verde\e[0m"
# Ejemplo de texto en azul
echo -e "\e[34mEste texto es azul\e[0m"

# Generamente se recomienta usar variables para almacenar los códigos de colores para facilitar su uso
# Variables de colores
RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
# Restablecer color
NC='\e[0m' # Elimina el color del mensaje
# Usar las variables para mostrar mensajes con colores
echo -e "${RED}Este texto es rojo${NC}"
echo -e "${GREEN}Este texto es verde${NC}"
echo -e "${BLUE}Este texto es azul${NC}"
echo -e "${RED}Texto en rojo${NC}, aqui no hay color, y ${BLUE}texto en azul${NC}"