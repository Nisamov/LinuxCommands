# Pautas de Contribución para LinuxCommands

¡Gracias por contribuir a LinuxCommands! Antes de enviar una solicitud de extracción, por favor, tómese un momento para revisar estas pautas.

## Proceso de Contribución

El repositorio sigue un estándar fijo de documentación para mantener el orden y permitir una correcta indexación a la hora de generar PDFs.

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
```json
:category: directorio_origen
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

Se pide tener en cuenta el [PULL_REQUEST_TEMPLATE](.github/PULL_REQUEST_TEMPLATE) en caso de querer colaborar con el repositorio, así como las contribuciones han de cumplir los siguientes puntos:
- [x] [Requerido] El contenido agregado está en el idioma nativo del repositorio (Español)
    - Es obligatorio que todos los cambios vengan en el idioma oficial del repositorio.
- [x] [Requerido] Los comandos documentados han sido revisados y validados
    - Esta opción será marcada por el supervisor de los pull request.
- [x] [Requerido] La estructura sigue el Modelo Base del repositorio
    - Es necesario que se tenga en cuenta la estructura de directorios y ficheros, así como extensiones de los mismos a la hora de agregar nuevo contenido en el repositorio.
- [x] [Requerido] Se ha verificado que no hay errores tipográficos o de sintaxis
    - Se pide revisar los cambios en búsqueda de pequeños errores, pues se valora principalmente, la correcta documentación del contenido.

Otros puntos que no cuenten con "**[Requerido]**" son opcionales y no influirán en su posibilidad de aceptación como contribución.