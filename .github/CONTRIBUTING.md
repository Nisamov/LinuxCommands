# Pautas de Contribución para LinuxCommands

¡Gracias por contribuir a LinuxCommands! Antes de enviar una solicitud de extracción, por favor, tómese un momento para revisar estas pautas.

## Proceso de Contribución

El repositorio sigue un estándar fijo de documentación para mantener el orden y permitir una correcta indexación a la hora de generar PDFs.

1. Clonar el repositorio y crear un Pull Request - [Crear Pull Request](https://github.com/Nisamov/LinuxCommands/pulls)
2. Realizar cambios o crear contenido siguiendo la estructura del repositorio:
    - [Ejemplo de premodelo en Markdown (.md)](.github/templates/markdown.md)
    - [Ejemplo de premodelo en Documento Ascii tipo Index (.adoc)](.github/templates/asciidocument_index.adoc)
    - [Ejemplo de premodelo en Documento Ascii tipo Comandos (.adoc)](.github/templates/asciidocument_command.adoc)
    - [Ejemplo de premodelo en Documento Ascii tipo Documentos (.adoc)](.github/templates/asciidocument_docs.adoc)
    - [Formato y significado en nombres de directorios](STRUCTURE.md)
3. Abrir pull request y rellenar las casillas indicadas.
4. Solicitar revisión del pull request.

### Indexación de comandos

La indexación que se lleva a cabo en el repositorio permite que los comandos se muestren en la [página web | búsqueda](https://nisamov.github.io/LinuxCommands/search.html).

Ejemplo de estructura `.json` en `.adoc`, esta estructura es la que hace posible la indexación del comando en la página web:
```json
:category: directorio_origen
[.metadata]
{
  "description": "Descripción",
  "usage": "comando [OPCIONES] 'programa' archivo",
  "options": {
    "-opcion1": "Opcion1",
    "-opcion2": "Opcion2",
    "-opcion3": "Opcion3"
  }
}
```
Esta estructura está unicamente en rutas semejantes a `*/commands/*.adoc`, lo que permite que se identifique su contenido como un comando y al aplicar dicha estructura, se crea así un comando nuevo que será procesado por un workflow para ser aplicado directamente en `docs/commands.json`.

## Requisitos del Pull Request

Se pide tener en cuenta el [PULL_REQUEST_TEMPLATE](.github/PULL_REQUEST_TEMPLATE) en caso de querer colaborar con el repositorio, así como las contribuciones han de cumplir los siguientes puntos:

Todos los cambios deben estar en el idioma oficial del repositorio (Español).
- [x] [Requerido] Los comandos documentados han sido revisados y validados.
    - Esta opción será marcada por el supervisor del pull request.
- [x] [Requerido] La estructura sigue el Modelo Base del repositorio.
    - Es necesario respetar la estructura de directorios y ficheros, así como sus extensiones.
- [x] [Requerido] Se ha verificado que no hay errores tipográficos o de sintaxis.
    - Se recomienda revisar cuidadosamente los cambios para asegurar la correcta documentación del contenido.

Otros puntos que no cuenten con "**[Requerido]**" son opcionales y no influirán en su posibilidad de aceptación como contribución.