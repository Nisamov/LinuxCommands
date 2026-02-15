# Formato y significado en nombres de directorios

EL nombramiento de los directorios del repositorio no es una coincidencia ni un accidente, están nombrados de tal forma que cada directorio informe sobre el contenido de su interior con un sutil vistazo.

Los nombres de los directorios **de primer nivel** son palabras compuestas, siguiendo la siguiente estructura: `"[a]_[b]_[c]"`.

### [a] Primera sección
En esta, se pueden encontrar palabras como "host", o "local".
- host: El contenido del directorio está orientado a ser hosteado en un servidor
- local: El contenido del directorio está orientado a la administración o manejo de un equipo local

### [b] Segunda sección
Aqui viene el nombre identificativo de cada subapartado, este dependerá del tipo de orientación que se le quiera dar al contenido del mismo.

Ejemplos:
- host_shared_storage: Orientado a un equipo servidor, con proposito de almacenamiento de datos.
- local_group: Orientado a un equipo local, con propósito de administrar y gestionar grupos.
- local_scripts: Orientado a un equipo local, con propósito de ejecutar scripts en el equipo.

### [c] Tercera sección
Esta tercera sección es una continuación de la primera, sirve con diferencial entre diferentes posibles nombres identicos.

Ejemplos (no necesariamente existentes):
- host_shared_storage: Orientado a un equipo servidor, con proposito de almacenamiento de datos.
- host_shared_users: Orientado a un equipo servidor, con proposito a la compartición de usuarios entre quiepos servidor.

Para directorios de niveles inferiores (sea segundo, tercer, cuarto...) nivel, la estructura varía, pues ahi ya no es requerido indicar el tipo de orientación que tiene el interior del directorio, sinó, en estos subdirectorios de bajo nivel, es requerido clasificar su contenido, sean scripts, nombre de servicios, toería, etc...

Los nombres de directorios tanto de primer nivel como inferiores, han de estar en inglés, esto es debido a la longitud de las palabras y la simplicidad encontrada en ellas.

No es lo mismo escribir: "local_network", que "red local", pese a que en español, cuenta con menos palabras, la estructura de las palabras en inglés permite poder agrupar los tipos de directorios de primer nivel sin requerir un filtro adicional (siendo este una cuarta sección al principio de los directorios, semejante a "00_ejemplo_ejemplo2, 01_ejemplo_ejemplo2, etc...")