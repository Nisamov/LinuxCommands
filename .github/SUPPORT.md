# Soporte LinuxCommands

### Clonación y aporte al repositorio
Para aportar con pull request, es necesario seguir los siguientes pasos y cumplir con la sintaxis indicada a continuación.

1. Clonación de repositorio - [Crear Pull Request](https://github.com/Nisamov/LinuxCommands/pulls)
2. Cambios o creación de contenido (siguiendo la estructura en el repositorio)
    - [Ejemplo de premodelo en Markdown (.md)](.github/templates/markdown.md)
    - [Ejemplo de premodelo en Documento Ascii tipo Index (.adoc)](.github/templates/asciidocument_index.adoc)
    - [Ejemplo de premodelo en Documento Ascii para Comandos (.adoc)](.github/templates/asciidocument_command.adoc)
3. Abrir pull request y rellenar las casillas indicadas
4. Solicitar comprobación de pull resquest

### Indexación de comandos
La indexación que se lleva a cabo en el repositorio, permite su muestra en la [página web | búsqueda](https://nisamov.github.io/LinuxCommands/search.html).

Esto es posible gracias al formato con el que están montados los ficheros `.adoc`:
```JSON
:category: local_filesystem
[.metadata]
{
  "description": "Descripción",
  "usage": "comando [OPCIONES] 'programa' archivo",
  "options": {
    "-opcion1": "Opcion1",
    "-opcion2": "Opcion2",
    "-opcion3": "Opcion3",
  }
}
```
Esta estructura está unicamente en rutas semejantes a `*/commands/*.adoc`, lo que permite que se identifique su contenido como un comando y al aplicar dicha estructura, se crea así un comando nuevo que será procesado por un workflow para ser aplicado directamente en `docs/commands.json`.

### Contacto
Si te encuentras en la necesidad de contactar a un administrador usa el siguiente correo: <a href="mailto:nisamov.contact@gmail.com">nisamov.contact@gmail.com</a>