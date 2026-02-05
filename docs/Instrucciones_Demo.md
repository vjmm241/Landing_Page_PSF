INSTRUCCIÓN BACKEND – APP CHATBOT TÉCNICO SOBRE PDF

\> Objetivo: Construir un backend 100% serverless con Supabase para una app que:

Autentica usuarios por email \+ contraseña

Verifica acceso mediante código OTP de 6 dígitos por email

Solicita Nombre y Empresa tras login

Permite subir UN ÚNICO PDF por usuario

Usa ese PDF como base de conocimiento persistente por sesión/usuario

Proporciona una demo interactiva de chatbot técnico que responde SOLO en base al PDF

Funciona sin backend local (todo cloud)

\---

STACK OBLIGATORIO

Backend: Supabase

Auth: Supabase Auth (Email \+ OTP)

DB: PostgreSQL \+ pgvector

Storage: Supabase Storage

IA: OpenAI API

Infra: Edge Functions (Supabase)

\---

PRINCIPIO CLAVE DE DISEÑO

❌ NO backend local

❌ NO procesos en memoria

✅ Todo persistente en Supabase

✅ El PDF se procesa una sola vez

✅ El chatbot siempre consulta la misma base vectorial del usuario

\---

1\. AUTENTICACIÓN

1.1 Login Email \+ Password

Usar Supabase Auth con proveedor Email habilitado.

Flujo:

1\. Usuario introduce email \+ password

2\. Se crea usuario en Supabase Auth

3\. Se envía verificación por email usando SMTP corporativo

\---

1.2 Verificación por OTP (6 dígitos)

Usar autenticación OTP por email nativa de Supabase.

Requisitos obligatorios:

Envío mediante SMTP corporativo (Hostinger)

Correo en HTML responsive alineado a la marca

Código OTP de 6 dígitos claramente destacado

Flujo:

1\. Usuario introduce email

2\. Supabase genera código OTP de 6 dígitos

3\. Supabase envía email vía SMTP Hostinger

4\. Usuario introduce el código

5\. Sesión validada

\---

1.3 RECUPERACIÓN DE CONTRASEÑA (RESET FLOW)

Objetivo: Seguridad reforzada al cambiar credenciales.

Flujo:

1. Usuario solicita link de recuperación por correo.

2. Usuario regenera la clave (Nueva contraseña).

3. Reset de Sesión: El sistema obliga a una nueva autenticación.

4. Re-verificación OTP: Se trata al usuario como nuevo inicio de sesión y se envía un nuevo código OTP de 6 dígitos.

5. Usuario valida OTP -> Acceso concedido (Inicio desde 0).

\---

2\. PERFIL DE USUARIO

2.1 Tabla profiles

create table profiles (  
  id uuid references auth.users on delete cascade,  
  name text not null,  
  company text not null,  
  created\_at timestamp default now(),  
  primary key (id)  
);

RLS:

auth.uid() \= id

\---

3\. GESTIÓN DEL PDF (UN SOLO PDF POR USUARIO)

3.1 Storage

Bucket: user\_documents

Privado

Estructura:

user\_documents/{user\_id}/document.pdf

Regla estricta:

Solo puede existir un PDF activo por usuario

Si se sube uno nuevo:

Se reemplaza el archivo

Se eliminan embeddings e imágenes previas

\---

3.2 Tabla documents

create table documents (  
  id uuid primary key default gen\_random\_uuid(),  
  user\_id uuid references auth.users on delete cascade,  
  file\_path text not null,  
  processed boolean default false,  
  created\_at timestamp default now()  
);

Restricción lógica:

Un solo documento activo por user\_id

\---

4\. BASE VECTORIAL

4.1 Tabla document\_chunks

create table document\_chunks (  
  id bigserial primary key,  
  user\_id uuid,  
  content text,  
  embedding vector(1536)  
);

Índice:

create index on document\_chunks using ivfflat (embedding vector\_cosine\_ops);

\---

5\. PROCESAMIENTO DEL PDF (EDGE FUNCTION)

5.1 Edge Function: process\_pdf

Se ejecuta cuando:

El usuario sube o reemplaza su PDF

Pasos obligatorios:

1\. Descargar PDF desde Supabase Storage

2\. Extraer texto completo

3\. Extraer imágenes embebidas

4\. Asociar imágenes a su contexto textual

5\. Dividir texto en chunks semánticos

6\. Generar embeddings con OpenAI

7\. Eliminar embeddings e imágenes anteriores del usuario

8\. Insertar nuevos embeddings

9\. Marcar documento como processed \= true

\---

6\. CHATBOT TÉCNICO

6.1 Flujo por mensaje

1\. Usuario envía pregunta

2\. Generar embedding de la pregunta

3\. Buscar los chunks más relevantes del usuario

4\. Buscar imágenes relevantes asociadas al contexto

5\. Construir contexto técnico

6\. Consultar OpenAI Chat Completion

\---

6.2 Query vectorial

select content  
from document\_chunks  
where user\_id \= :user\_id  
order by embedding \<-\> :query\_embedding  
limit 5;

\---

6.3 PROMPT DEL SISTEMA (OBLIGATORIO)

Eres un ASISTENTE TÉCNICO SENIOR especializado en documentación técnica.

REGLAS ABSOLUTAS:  
\- Responde ÚNICAMENTE usando la información contenida en el documento del usuario.  
\- NO inventes, NO completes con suposiciones, NO extrapoles.  
\- Si la información no está en el documento, indícalo explícitamente.  
\- Nunca alucines ni aportes conocimiento externo.

FORMA DE RESPUESTA OBLIGATORIA:  
\- Explica SIEMPRE paso a paso.  
\- Cada paso debe ser claro, técnico y preciso.  
\- Cuando exista una imagen, diagrama o figura relevante en el documento:  
  \- Muéstrala inmediatamente después del paso al que hace referencia.  
  \- Alterna el formato: texto → imagen → texto → imagen.

ESTILO:  
\- Tono profesional y técnico.  
\- Claridad absoluta.  
\- Lenguaje de ingeniero senior.  
\- Nada genérico.

Si el usuario pide algo fuera del alcance del documento:  
\- Responde: "La información solicitada no está presente en el documento proporcionado."

\---

7\. SEGURIDAD

RLS en todas las tablas

Cada usuario solo accede a sus datos

OpenAI API Key solo en Edge Functions

Storage privado

\---

8\. DEMO INTERACTIVA (BACKEND)

El backend debe devolver respuestas estructuradas (texto \+ imágenes)

No lógica de UI

Todo orientado a consumo por frontend

\---

9\. RESULTADO FINAL ESPERADO

Backend 100% serverless

PDF persistente por usuario

Chatbot técnico con texto \+ imágenes

Sin backend local

Escalable como SaaS

\---

(UI/UX ULTRA REALISTA – IPHONE 17 PRO MAX 3D)

\> Objetivo: La demo debe simular un iPhone 17 Pro Max hiperrealista en 3D, dentro del cual se ejecuta WhatsApp móvil (no web) de forma interactiva, transmitiendo sensación de producto real, premium y listo para producción.

\---

10.1 PRINCIPIO DE DISEÑO

❌ No WhatsApp Web

❌ No mockup plano

✅ Simulación iPhone 17 Pro Max en 3D

✅ UI idéntica a WhatsApp móvil

✅ Sensación de app nativa

La demo debe parecer:

\> “Esto ya está en producción en un iPhone real.”

\---

10.2 MOCKUP IPHONE 17 PRO MAX (3D)

Características visuales

Render 3D del dispositivo (frame, bordes, cámara, notch)

Sombra realista

Ligero efecto parallax

Escala responsive

Opciones técnicas:

SVG \+ CSS avanzado

Three.js (si es necesario)

Mockup 3D optimizado para web

\---

10.3 PANTALLA INTERNA: WHATSAPP MÓVIL

Requisitos estrictos

UI idéntica a WhatsApp iOS:

Header con nombre y avatar

Burbuja verde (usuario)

Burbuja gris (bot)

Hora

Check de mensaje

Barra inferior:

Emoji button

Input texto

Clip adjuntar

Micrófono (visual)

\---

10.4 INPUT DE PDF (FLUJO NATIVO)

Simular flujo real de WhatsApp:

1\. Tap en icono 📎

2\. Modal iOS:

“Archivos”

“Seleccionar PDF”

3\. Upload

4\. Mensaje automático:

\> "Documento recibido. Analizando…"

\---

10.5 ANIMACIONES CLAVE

Escritura con animación realista

Scroll natural

Vibración sutil (haptic fake)

Mensajes entrantes con delay humano

\---

10.6 EMOJIS Y RICH CONTENT

Emojis nativos estilo iOS

Render de imágenes dentro del chat

Preview de imágenes técnicas

\---

10.7 CONEXIÓN BACKEND

Cada acción del chat:

Input → Edge Function

Respuesta estructurada → render móvil

\---

11\. CHATBOT TÉCNICO AVANZADO (TEXTO \+ IMÁGENES)

(TEXTO \+ IMÁGENES)

\> Objetivo: El chatbot debe responder de forma técnica, paso a paso y, cuando el PDF contenga figuras, diagramas o imágenes, debe mostrarlas directamente en el chat, no solo referenciarlas.

\---

11.1 PRINCIPIO CLAVE

❌ No solo texto

❌ No referencias tipo “ver figura 7, página 13”

✅ El chatbot muestra la imagen real cuando aporta valor

✅ Experiencia tipo software técnico profesional

\---

11.2 PROCESAMIENTO DEL PDF (BACKEND)

Extracción avanzada

Durante el procesamiento del PDF:

1\. Extraer texto

2\. Extraer imágenes embebidas

3\. Asociar cada imagen a:

Página

Contexto textual cercano

\---

Storage de imágenes

Bucket: document\_images

Estructura:

document\_images/{user\_id}/{document\_id}/page\_X\_image\_Y.png

\---

11.3 TABLAS ADICIONALES

Tabla document\_images

create table document\_images (  
  id bigserial primary key,  
  user\_id uuid,  
  document\_id uuid,  
  page\_number int,  
  image\_url text,  
  context text  
);

\---

11.4 EMBEDDINGS MULTIMODALES

Generar embeddings:

Del texto

Del contexto asociado a cada imagen

Esto permite que una pregunta semántica también recupere imágenes relevantes.

\---

11.5 LÓGICA DEL CHATBOT (BACKEND)

Flujo por pregunta

1\. Usuario pregunta

2\. Generar embedding de la pregunta

3\. Buscar:

Chunks de texto relevantes

Imágenes relevantes por contexto

4\. Construir respuesta estructurada:

Explicación paso a paso

Imágenes intercaladas cuando aporten claridad

\---

Formato de respuesta (JSON)

{  
  "steps": \[  
    "Paso 1: ...",  
    "Paso 2: ..."  
  \],  
  "images": \[  
    {  
      "url": "https://...",  
      "caption": "Figura X – Descripción"  
    }  
  \]  
}

\---

11.6 PROMPT DEL SISTEMA (CHATBOT)

Eres un asistente técnico experto.  
Explica siempre paso a paso.  
Cuando el documento incluya diagramas o imágenes relevantes,  
incorpóralas directamente en la respuesta.  
No hagas referencias abstractas.  
Si algo no está en el documento, indícalo.

\---

12\. FRONT-END CHAT (RENDER TEXTO \+ IMÁGENES)

12.1 Burbujas de mensaje avanzadas

Texto con formato markdown

Bloques numerados (pasos)

Imágenes renderizadas dentro del chat

Caption técnico debajo de cada imagen

\---

12.2 COMPONENTES CLAVE

ChatMessage

StepList

ImageMessage

TypingIndicator

\---

12.3 UX DE IMÁGENES

Click para ampliar (modal)

Zoom

Fondo oscuro

\---

13\. TONO Y PERSONALIDAD DEL CHATBOT

Técnico

Claro

Preciso

Profesional

Nada genérico

Ejemplo:

"Paso 1: Identifique el parámetro X en el panel de control (ver imagen)."

\---

14\. DEMO INTERACTIVA PREMIUM

14.1 Mensaje inicial del bot

"He analizado tu documento técnico. Puedes preguntarme sobre parámetros, normas, diagramas o procedimientos paso a paso."

\---

14.2 Indicadores visuales

Documento cargado ✔

Base de conocimiento lista ✔

\---

16\. GUIÓN EXACTO DE LA DEMO COMERCIAL (INTERACTIVA)

\> Objetivo: Que cualquier persona que vea o use la demo entienda el valor en menos de 3 minutos y piense: “Esto lo necesito en mi empresa”.

\---

16.1 CONTEXTO DE LA DEMO

Formato:

Pantalla: iPhone 17 Pro Max 3D

App: WhatsApp móvil

Usuario: Cliente potencial

Bot: Asistente Técnico IA

\---

16.2 SECUENCIA DE LA DEMO (PASO A PASO)

PASO 1 – MENSAJE INICIAL AUTOMÁTICO

Mensaje del bot:

\> "Hola 👋 He analizado tu documento técnico y estoy listo para ayudarte.

Puedes preguntarme sobre parámetros, normas, procedimientos o diagramas, y te responderé paso a paso usando exactamente la información de tu manual."

(Indicador visual: Documento cargado ✔ · Base de conocimiento lista ✔)

\---

PASO 2 – PRIMERA PREGUNTA GUIADA

Chip sugerido:

\> “Explícame este parámetro”

Usuario hace tap.

\---

PASO 3 – RESPUESTA DE IMPACTO

Bot responde:

Paso 1: Define el parámetro X según el capítulo 3\.

Paso 2: Ajusta el rango permitido entre Y y Z.

Paso 3: Verifica el resultado según la norma indicada.

(Se muestra imagen real del diagrama del PDF dentro del chat)

\---

PASO 4 – PREGUNTA AVANZADA

Usuario escribe:

\> “¿Qué norma regula este procedimiento?”

Bot:

Identifica la norma exacta

Explica su aplicación práctica

Muestra esquema si existe

\---

PASO 5 – MOMENTO WOW

Usuario:

\> “Explícamelo como si fuera un técnico nuevo.”

Bot:

Simplifica

Mantiene precisión técnica

Refuerza sensación de inteligencia real

\---

17\. COPY DEL CHAT INICIAL (ONBOARDING)

17.1 MENSAJE DE BIENVENIDA (FIJO)

\> "Soy tu asistente técnico inteligente.

He sido entrenado exclusivamente con tu documento, por lo que mis respuestas siempre estarán basadas en tus normas, manuales y procedimientos.

Pregúntame lo que quieras."

\---

17.2 MENSAJES DE ESTADO

Documento subido:

\> "Documento recibido. Analizando contenido técnico…"

Listo:

\> "Base de conocimiento lista. Puedes empezar a preguntar."

\---

FIN DE LA INSTRUCCIÓN  
