# DIRECTIVA: DEMO_INTERACTIVA_WHATSAPP_IA

> **ID:** DEMO-2026-01-28  
> **Script/Página Asociada:** `nuestra-solucion.html` + `server/server.js`  
> **Última Actualización:** 2026-01-28  
> **Estado:** FASE 2 - INTEGRACIÓN BACKEND

---

## 1. Objetivos y Alcance

- **Objetivo Principal:** Crear una demo interactiva donde usuarios puedan experimentar el asistente IA de ProSmart Factories. Simula el proceso de subir un manual PDF y hacer preguntas que la IA responde citando páginas.

- **Criterio de Éxito:** 
  1. Usuario puede acceder vía modal de login
  2. Usuario puede simular upload de PDF
  3. Usuario puede escribir preguntas en chat
  4. Sistema responde con texto + número de página + nombre del manual

## 2. Especificaciones de Entrada/Salida (I/O)

### Entradas (Inputs)
- **Argumentos Requeridos:**
  - `email`: String - Email del usuario para login (cualquier formato válido)
  - `password`: String - Contraseña (cualquier valor, demo simulada)
  - `pdf_file`: File - Archivo PDF (simulado, no se procesa realmente)
  - `pregunta`: String - Texto de la pregunta del usuario

### Salidas (Outputs)
- **Respuesta IA:**
  - `texto`: String - Respuesta a la pregunta
  - `pagina`: Integer - Número de página citada
  - `seccion`: String - Nombre de la sección del manual
  - `manual`: String - Nombre del archivo PDF subido

## 3. Flujo Lógico (Algoritmo)

### Paso 1: Acceso a la Página
- Usuario entra a `nuestra-solucion.html`
- Ve hero explicativo con botón "Comenzar Demo"
- Mockup de WhatsApp está bloqueado por overlay de login

### Paso 2: Login
- Usuario hace clic en "Comenzar Demo"
- Se muestra modal de login
- Usuario introduce email y contraseña (cualquier valor válido)
- Sistema almacena estado `isLoggedIn = true`
- Overlay de login desaparece
- Se activa zona de upload

### Paso 3: Upload PDF
- Usuario arrastra o selecciona archivo PDF
- Barra de progreso simula procesamiento (3 segundos)
- Mensajes de estado: "Extrayendo texto..." → "Analizando..." → "Listo"
- Sistema almacena `pdfUploaded = true` y `uploadedFileName`
- Se habilita input de chat y botones de ejemplo

### Paso 4: Chat Interactivo
- Usuario escribe pregunta en input o usa botón de ejemplo
- Sistema muestra mensaje del usuario en chat
- Indicador "escribiendo..." durante 1.5-2.5 segundos
- Sistema busca palabras clave en pregunta
- Retorna respuesta pre-programada con página y sección

### Paso 5: Respuesta con Fuente
- Respuesta incluye texto formateado
- Footer con: icono PDF + "Página X | Sección Y | NombreManual.pdf"
- Se muestra timestamp actual

## 4. Herramientas y Librerías
- **Frontend:** HTML5, CSS3, JavaScript Vanilla
- **Animaciones:** GSAP 3.12.2
- **Fonts:** Plus Jakarta Sans, Bebas Neue, JetBrains Mono (Google Fonts)
- **No requiere backend**

## 5. Restricciones y Casos Borde

### Limitaciones Conocidas
- **Limitación 1:** El backend almacena el PDF en memoria (se pierde al reiniciar el servidor).
- **Limitación 2:** Soporte mono-usuario/mono-archivo (el último PDF subido es el contexto global).
- **Limitación 3:** Límite de tokens en Gemini Pro (truncamos el texto extraído a 15k caracteres).

### Requisitos Técnicos
- Node.js v16+
- API Key de Google Gemini en `server/.env`
- Puerto 3001 disponible para el backend

### Validaciones Requeridas
- Email debe tener formato válido (HTML5 validation)
- Solo acepta archivos PDF en upload
- Input de chat no puede estar vacío para enviar
- **UX:** El mockup debe mantener altura fija para evitar saltos de layout al recibir mensajes.

## 6. Protocolo de Errores y Aprendizajes (Memoria Viva)

| Fecha | Error Detectado | Causa Raíz | Solución/Parche Aplicado |
|-------|-----------------|------------|--------------------------|
| 28/01 | Mockup deforma Layout | `min-height` permitía crecimiento | Cambiado a `height` fija con scroll interno en `chat-area`. |
| 28/01 | Respuestas Genéricas | Falta de contexto amigable | Refactorizado `aiResponses` con emojis, pasos numerados y más keywords. |
| 28/01 | Mockup "Flotante" Irreal | Diseño CSS plano (genérico) | Rediseño estilo iPhone 16 Pro Max con marcos de titanio y Dynamic Island. |
| 28/01 | Falta de Inmersión | Mockup estático | Implementación de GSAP para entrada y efecto 3D Parallax con movimiento de ratón. |

> **Nota de Implementación:** Para escalabilidad, mantener el `chat-area` con `scroll-behavior: smooth` y añadir la fuente opcionalmente solo si el par `page/section` existe en el objeto de respuesta.

## 7. Ejemplos de Uso

```bash
# Acceso directo
Abrir en navegador: nuestra-solucion.html

# Palabras clave de prueba sugeridas
"¿Cómo calibro el eje?" -> Respuesta detallada pág 23
"tengo un error" -> Guía de diagnóstico pág 95
```

## 8. Checklist de Pre-Ejecución
- [x] Archivo `nuestra-solucion.html` creado
- [x] Logo de PSF disponible en `assets/images/`
- [x] Fonts de Google accesibles (Plus Jakarta, Bebas Neue)
- [x] GSAP CDN accesible

## 9. Checklist Post-Ejecución
- [x] Login modal funcional (simulado)
- [x] Upload PDF con barra de progreso progresiva
- [x] Chat con scroll interno automático (`scrollTop = scrollHeight`)
- [x] Mockup iPhone 16 Pro Max con efecto 3D interactivo
- [x] Respuestas amigables con fuentes dinámicas
- [x] Responsive en móvil (viewport adaptado)

## 10. Evolución Futura (Fase 2)
[... mismo contenido ...]

