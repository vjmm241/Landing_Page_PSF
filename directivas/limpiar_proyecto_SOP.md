# DIRECTIVA: LIMPIEZA_Y_ORGANIZACION_SOP

> **ID:** DIRECTIVE-CLN-001
> **Script Asociado:** `scripts/limpiar_proyecto.py`
> **Última Actualización:** 2026-02-05
> **Estado:** ACTIVO

---

## 1. Objetivos y Alcance
- **Objetivo Principal:** Eliminar archivos basuras, carpetas obsoletas y organizar los archivos sueltos en la raíz para mantener un repositorio limpio y profesional.
- **Criterio de Éxito:** 
  - Las carpetas `_archive/` y `server/` han sido eliminadas.
  - No hay archivos `.md` sueltos en la raíz (movidos a `docs/` o `directivas/`).
  - No hay archivos `.py` sueltos en la raíz (movidos a `scripts/`).
  - Los activos PNG/JPG están en `assets/`.

## 2. Especificaciones de Entrada/Salida (I/O)

### Entradas (Inputs)
- **Directorio Raíz:** `c:/Users/victo/OneDrive/Documents/Landing_Page_PSF`
- **Lista de carpetas a eliminar:** `_archive`, `server`.

### Salidas (Outputs)
- **Estructura Organizada:**
  - `docs/`: Contiene manuales, planes y esquemas SQL.
  - `scripts/`: Contiene toda la lógica de Python y JS.
  - `assets/`: Imágenes y activos multimedia.
  - `directivas/`: SOPs y guías de trabajo del agente.

## 3. Flujo Lógico (Algoritmo)

1. **Inicialización:** Verificar permisos y existencia de rutas base.
2. **Eliminación:** Borrar de forma recursiva las carpetas `_archive` y `server`.
3. **Clasificación:**
    - Mover archivos `.js`, `.py` a `scripts/`.
    - Mover archivos `.md` de documentación a `docs/`.
    - Mover archivos `.md` que sean SOPs a `directivas/`.
    - Mover archivos de imagen a `assets/`.
4. **Limpieza de Raíz:** Asegurar que solo queden archivos de configuración esenciales (`.env`, `.gitignore`, `package.json`, etc.) y los archivos `.html` principales.
5. **Verificación:** Listar contenido final de la raíz para confirmar limpieza.

## 4. Herramientas y Librerías
- **Librerías Python:** `os`, `shutil`, `glob`.

## 5. Restricciones y Casos Borde (Edge Cases)
- **Archivos Críticos:** No mover `index.html`, `nuestra-solucion.html`, `vercel.json`, o archivos de configuración de entorno.
- **Conflictos de Nombre:** Si el archivo ya existe en el destino, añadir prefijo o notificar (el script debe manejar sobrescritura controlada).

## 6. Historial de Aprendizaje
- **2026-02-05:** Creación inicial para optimización solicitada por el usuario.
