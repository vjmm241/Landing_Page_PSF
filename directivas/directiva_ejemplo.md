# DIRECTIVA: ORDENAR_CARPETA

> **ID:** DIRECTIVE-ORD-001
> **Script Asociado:** `scripts/ordenar_carpeta.py`
> **Última Actualización:** 2026-01-29
> **Estado:** ACTIVO

---

## 1. Objetivos y Alcance
*Describe aquí QUÉ debe lograr esta tarea y POR QUÉ.*
- **Objetivo Principal:** Organizar la raíz del proyecto moviendo archivos sueltos a sus carpetas correspondientes (`assets`, `scripts`, `directivas`) y actualizando referencias si es necesario.
- **Criterio de Éxito:** 
  - `VictorMarquinaFactories.png` está en `assets/`.
  - `optimize_image.py` está en `scripts/`.
  - `Directiva.md` se ha movido a `directivas/directiva_ejemplo.md`.
  - `index.html` tiene la referencia de imagen actualizada.

## 2. Especificaciones de Entrada/Salida (I/O)

### Entradas (Inputs)
- **Archivos Fuente:**
  - `VictorMarquinaFactories.png` (Raíz)
  - `optimize_image.py` (Raíz)
  - `Directiva.md` (Raíz)
  - `index.html` (Raíz - para lectura y actualización)

### Salidas (Outputs)
- **Estructura de Carpetas:**
  - `assets/VictorMarquinaFactories.png`
  - `scripts/optimize_image.py`
  - `directivas/directiva_ejemplo.md`
- **Archivos Modificados:**
  - `index.html` (Referencias actualizadas)
- **Retorno de Consola:** Mensaje de éxito indicando archivos movidos y actualizados.

## 3. Flujo Lógico (Algoritmo)

1. **Inicialización:** 
   - Verificar existencia de archivos origen.
   - Verificar existencia de carpetas destino (`assets`, `scripts`, `directivas`). Crearlas si no existen.
2. **Mover Archivos:**
   - Mover `VictorMarquinaFactories.png` -> `assets/`.
   - Mover `optimize_image.py` -> `scripts/`.
   - Renombrar y Mover `Directiva.md` -> `directivas/directiva_ejemplo.md`.
3. **Actualizar Referencias:**
   - Leer `index.html`.
   - Reemplazar `src="VictorMarquinaFactories.png"` por `src="assets/VictorMarquinaFactories.png"` (o similar).
   - Guardar `index.html`.
4. **Verificación:**
   - Comprobar que los archivos ya no están en raíz.
   - Comprobar que están en destino.

## 4. Herramientas y Librerías
*Lista blanca de dependencias permitidas.*
- **Librerías Python:** `os`, `shutil`.

## 5. Restricciones y Casos Borde (Edge Cases)

### Limitaciones Conocidas
- **Archivos en uso:** Si un archivo está abierto por otro proceso, el movimiento puede fallar.
- **Referencias Dinámicas:** El script solo buscará referencias estáticas simples en `index.html`.

### Protocolo de Errores
- Si falla un movimiento, intentar revertir o notificar el error específico.

## 6. Historial de Aprendizaje
*(Nuevo)*
