![Cartel Principal](.github/media/sheyald.png)

---
<p align="center">
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ESP"><img src="https://img.shields.io/badge/🇪🇸%20ESP-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ENG"><img src="https://img.shields.io/badge/🇬🇧%20ENG-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/FR"><img src="https://img.shields.io/badge/🇫🇷%20FR-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/DE"><img src="https://img.shields.io/badge/🇩🇪%20DEU-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/PT"><img src="https://img.shields.io/badge/🇵🇹%20POR-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/RU"><img src="https://img.shields.io/badge/🇷🇺%20RUS-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ZH"><img src="https://img.shields.io/badge/🇨🇳%20中文-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/KO"><img src="https://img.shields.io/badge/🇰🇷%20한국-000?style=flat-square&logo=adobeacrobatreader" /></a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/JA"><img src="https://img.shields.io/badge/🇯🇵%20日本語-000?style=flat-square&logo=adobeacrobatreader" /></a>
</p>

# LinuxCommands
[![Last commit](https://img.shields.io/github/last-commit/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff&label=ultima-actualizacion)](https://github.com/Nisamov/LinuxCommands/commits)[![License](https://img.shields.io/github/license/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff&label=licencia)](LICENSE)[![Visits](https://img.shields.io/endpoint?url=https://hits.dwyl.com/Nisamov/LinuxCommands.json&style=flat-square&color=000000&labelColor=ffffff&label=visitas)](https://github.com/Nisamov/LinuxCommands)

### Estructura y referencia para documentar comandos y servicios en Linux

LinuxCommands nació como una recopilación de apuntes personales para organizar y entender mejor distintos comandos, scripts y servicios en Linux.

Con el tiempo, se fue estructurando para que sea más fácil de navegar y consultar, tanto para mí como para cualquier persona interesada en aprender o consultar comandos y servicios de manera práctica.

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
```JSON
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

Se pide tener en cuenta el [PULL_REQUEST_TEMPLATE](.github/PULL_REQUEST_TEMPLATE) en caso de querer colaborar con el repositorio.
</details>

---
<details open>
<summary><strong>• TRADUCCIONES</strong></summary>
<h1>Traducciones en los documentos</h1>

El repositorio se adapta a diferentes lenguas mediante la automatización de la generación PDF.
<p align="center">
  <a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ESP"><img src="https://img.shields.io/badge/🇪🇸%20Español-Descargar?style=flat&color=000000&labelColor=ffffff" /></a><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ENG"><img src="https://img.shields.io/badge/🇬🇧%20English-Download?style=flat&color=000000&labelColor=ffffff" /><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/FR"><img src="https://img.shields.io/badge/🇫🇷%20Français-Bientôt?style=flat&color=000000&labelColor=ffffff" /></a></a><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/DE"><img src="https://img.shields.io/badge/🇩🇪%20Deutsch-Herunterladen?style=flat&color=000000&labelColor=ffffff" /></a><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/PT"><img src="https://img.shields.io/badge/🇧🇷%20Português-Em%20breve?style=flat&color=000000&labelColor=ffffff" /></a><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/RU"><img src="https://img.shields.io/badge/🇷🇺%20Русский-Скоро?style=flat&color=000000&labelColor=ffffff" /></a><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/ZH"><img src="https://img.shields.io/badge/🇨🇳%20简体中文-即将推出?style=flat&color=000000&labelColor=ffffff" /></a><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/KO"><img src="https://img.shields.io/badge/🇰🇷%20한국어-준비%20중?style=flat&color=000000&labelColor=ffffff" /></a><a href="https://github.com/Nisamov/LinuxCommands/releases/tag/JA"><img src="https://img.shields.io/badge/🇯🇵%20日本語-準備中?style=flat&color=000000&labelColor=ffffff" /></a>
</p>

> En caso de ver iconos semejantes a "▯" es porbable que requiera descargar los carácteres en el equipo.
> [Descargar fuentes CJK manualmente](https://github.com/notofonts/noto-cjk/releases/latest)
</details>

---
<p align="center">
  <a href="https://github.com/Nisamov/LinuxCommands/stargazers">
    <img src="https://img.shields.io/github/stars/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff" />
  </a>
  <a href="https://github.com/Nisamov/LinuxCommands/network/members">
    <img src="https://img.shields.io/github/forks/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff" />
  </a>
  <a href="https://github.com/Nisamov/LinuxCommands/releases">
    <img src="https://img.shields.io/github/downloads/Nisamov/LinuxCommands/total?style=flat-square&color=000000&labelColor=ffffff" />
  </a>
  <a href="https://github.com/Nisamov/LinuxCommands/watchers">
    <img src="https://img.shields.io/github/watchers/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff" />
  </a>
  <a href="https://github.com/Nisamov/LinuxCommands/pulls">
    <img src="https://img.shields.io/github/issues-pr/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff" />
  </a>
  <a href="https://github.com/Nisamov/LinuxCommands/pulls?q=is%3Apr+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-pr-closed/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff" />
  </a>
  <a href="https://github.com/Nisamov/LinuxCommands/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Nisamov/LinuxCommands?style=flat-square&color=000000&labelColor=ffffff" />
  </a>
</p>

<div align="center">
  <p>Linux Commands - By Nisamov | MIT License - 2026</p>
  <p>Contacto: <a href="mailto:nisamov.contact@gmail.com">nisamov.contact@gmail.com</a></p>
</div>
