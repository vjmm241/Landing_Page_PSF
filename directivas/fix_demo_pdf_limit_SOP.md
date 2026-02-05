# DIRECTIVA: ARREGLAR DEMO Y AUMENTAR LÍMITE PDF

> **ID:** DEMO-FIX-2026-02-05  
> **Script/Página Asociada:** `nuestra-solucion.html`, `supabase/functions/process_pdf/index.ts`  
> **Estado:** PLANIFICACIÓN

---

## 1. Objetivos y Alcance

- **Objetivo Principal:** Asegurar que la demo sea funcional y permita procesar archivos PDF de hasta 10MB.
- **Criterio de Éxito:** 
  1. El límite de subida en el frontend y backend permite hasta 10MB.
  2. La función `process_pdf` maneja archivos más grandes sin exceder el tiempo de ejecución (timeout).
  3. Se procesan más de 5 chunks para mejorar la calidad de la respuesta en documentos largos.

## 2. Especificaciones de I/O

### Entradas
- Archivo PDF de hasta 10MB.
- `document_id` y `userId` para la función de procesamiento.

### Salidas
- Chunks de texto y embeddings almacenados en la base de datos.
- Respuesta de éxito de la Edge Function.

## 3. Flujo Lógico (Algoritmo)

1. **Revisión del Frontend:** Comprobar si hay validaciones de tamaño en `nuestra-solucion.html`.
2. **Optimización del Backend:**
   - Aumentar el límite de chunks de embeddings (actualmente en 5).
   - Revisar la gestión de memoria durante el parseo de PDF.
   - Asegurar que los errores se devuelven como JSON con status 200 para evitar excepciones genéricas en el cliente.
3. **Verificación:** Ejecutar script de prueba para simular el proceso.

## 4. Herramientas y Librerías
- Supabase Edge Functions (Deno).
- PDF.js (vía ESM.sh).
- OpenAI Embeddings API.
- Python (para scripts de verificación).

## 5. Restricciones y Casos Borde
- **Timeout de Edge Functions:** El procesamiento de PDFs muy grandes puede tardar.
- **Límites de OpenAI:** Coste y velocidad de generación de embeddings para muchos chunks.
- **Memoria de Deno:** archivos de 10MB pueden ocupar mucha RAM al descomprimirse en memoria.

## 6. Protocolo de Errores (Memoria Viva)
- **Batching is mandatory:** Processing > 20 chunks individually hits Edge Function timeouts. Always use OpenAI's array input and Supabase's batch `.insert()`.
- **Memory management:** For PDFs near 10MB, Deno might run low on memory if too many objects are kept in scope. The current `process_pdf` implementation focuses on text extraction which is relatively safe, but complex images should be ignored (already handled via `disableFontFace: true`).
- **Status 200 required:** Always return HTTP 200 for internal errors to allow the frontend `supabase.functions.invoke` to catch the error in the body instead of throwing a generic exception.

---

## 7. Checklist de Ejecución
- [ ] Modificar `process_pdf/index.ts` para aumentar el límite de chunks.
- [ ] Verificar configuración de storage `user_documents` (Manual).
- [ ] Crear script `scripts/verify_pdf_limit.py`.
- [ ] Ejecutar verificación y documentar resultados.
