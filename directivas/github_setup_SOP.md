# DIRECTIVA: CONFIGURACION_GITHUB_REPOSITORIO

> **ID:** DIRECTIVE-GIT-001
> **Script Asociado:** `scripts/setup_github_repo.py`
> **Última Actualización:** 2026-02-05
> **Estado:** ACTIVO

---

## 1. Objetivos y Alcance
- **Objetivo Principal:** Crear un repositorio en GitHub y vincularlo con el proyecto local.
- **Criterio de Éxito:** El repositorio existe en GitHub y contiene el código local sincronizado.

## 2. Instrucciones Técnicas

### Requisitos Previos
- Tener un `GITHUB_TOKEN` válido en `CREDENCIALES.txt` o variables de entorno.
- Git instalado y configurado localmente.

### Lógica de Creación
1. Verificar si el repositorio ya existe en GitHub via API.
2. Si no existe, crearlo como repositorio **público** (a menos que se especifique lo contrario).
3. Configurar el remoto `origin` en la carpeta local.
4. Realizar el primer push.

## 3. Trampas Conocidas y Restricciones
- **Error 401:** Token inválido. Verificar `CREDENCIALES.txt`.
- **Error 422:** El repositorio ya existe. En este caso, solo vincular el remoto.
- **Merge Conflicts:** Si el repositorio de GitHub tiene un README inicial y el local no, usar `--allow-unrelated-histories` o crear el repo vacío.

## 4. Notas de Memoria
- Siempre usar el nombre de la carpeta actual como nombre del repositorio por defecto.
- Asegurarse de que `.gitignore` incluya archivos sensibles antes de subir.
