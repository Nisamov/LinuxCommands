![Cartel Principal](.github/media/sheyald.png)

---
<p align="center">
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ESP">Español</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ENG">English</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/FR">Français</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/DE">Deutsch</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/PT">Português</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/RU">Русский</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ZH">中文</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/KO">한국어</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/JA">日本語</a>
</p>

# LinuxCommands
[![Last commit](https://img.shields.io/github/last-commit/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff&label=ultima-actualizacion)](https://github.com/Nisamov/LinuxCommands/commits)[![License](https://img.shields.io/github/license/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff&label=licencia)](LICENSE)[![Visits](https://img.shields.io/endpoint?url=https://hits.dwyl.com/Nisamov/LinuxCommands.json&style=flat-square&color=000000&labelColor=ffffff&label=visitas)](https://github.com/Nisamov/LinuxCommands)

### Estructura y referencia para documentar comandos y servicios en Linux

LinuxCommands nació como una recopilación de apuntes personales para organizar y entender mejor distintos comandos, scripts y servicios en Linux.

[Más información sobre los orígenes del repositorio](.github/INFO.md).

---
<details open>
<summary><strong>• OBJETIVOS DEL PORYECTO</strong></summary>
<h1>Objetivos del proyecto</h1>

- Proporcionar un formato claro y reutilizable para documentar comandos y servicios de Linux.
- Facilitar una documentación legible para humanos y mantenible a largo plazo.
- Reducir duplicación, ambigüedad y variaciones innecesarias entre repositorios.
- Servir como referencia práctica para administradores de sistemas, desarrolladores y equipos técnicos.
</details>

---
<details open>
<summary><strong>• ESTRUCTURA DEL PROYECTO</strong></summary>
<h1>Estructura del proyecto</h1>

La organización del repositorio está pensada para facilitar la navegación y el crecimiento progresivo del contenido:

<!-- AUTO-GENERATED-INDEX:START -->
- [host_services](/host_services)
- [host_shared_storage](/host_shared_storage)
- [host_web_server](/host_web_server)
- [linux_fundamentals](/linux_fundamentals)
- [local_filesystem](/local_filesystem)
- [local_group](/local_group)
- [local_network](/local_network)
- [local_permissions](/local_permissions)
- [local_process](/local_process)
- [local_scripts](/local_scripts)
- [local_security](/local_security)
- [local_services](/local_services)
- [local_software](/local_software)
- [local_storage](/local_storage)
- [local_system_data](/local_system_data)
- [local_users](/local_users)
<!-- AUTO-GENERATED-INDEX:END -->
</details>

---
<details open>
<summary><strong>• FORMATO DE DOCUMENTACIÓN</strong></summary>
<h1>Formato de documentación</h1>

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
- [x] [Requerido] Los comandos documentados han sido revisados y validados
- [x] [Requerido] La estructura sigue el Modelo Base del repositorio
- [x] [Requerido] Se ha verificado que no hay errores tipográficos o de sintaxis

Otros puntos que no cuenten con "[Requerido]" son opcionales y no influirán en su posibilidad de aceptación como contribución.

</details>

---
<details open>
<summary><strong>• TRADUCCIONES</strong></summary>
<h1>Traducciones en los documentos</h1>

El repositorio se adapta a diferentes lenguas mediante la automatización de la generación PDF.
<p align="center">
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ESP">Español</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ENG">English</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/FR">Français</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/DE">Deutsch</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/PT">Português</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/RU">Русский</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ZH">中文</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/KO">한국어</a>
  &nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/JA">日本語</a>
</p>

> En caso de ver iconos semejantes a "▯" es probable que sea necesario [descargar fuentes CJK](https://github.com/notofonts/noto-cjk/releases/latest) en el equipo.
</details>

---
<div align="center">
  <p>Linux Commands - By Nisamov | MIT License - 2026</p>
  <p>Contacto: <a href="mailto:nisamov.contact@gmail.com">nisamov.contact@gmail.com</a></p>
</div>
