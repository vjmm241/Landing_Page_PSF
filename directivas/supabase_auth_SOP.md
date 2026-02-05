# SOP: SUPABASE_AUTH_AND_SECRETS

> **ID:** SOP-SUPA-001
> **Script Asociado:** N/A
> **Estado:** ACTIVO

---

## 1. Problema: Error "Access token not provided"
Este error ocurre cuando se intenta usar el CLI de Supabase (`npx supabase ...`) para operaciones remotas (como `secrets set`) sin haber autenticado la sesión.

## 2. Solución Determinista

### Opción A: Variable de Entorno (Recomendado para CI/CD y Agentes)
1. Obtener un "Personal Access Token" desde el dashboard de Supabase (Settings -> Access Tokens).
2. Configurar la variable de entorno `SUPABASE_ACCESS_TOKEN` con dicho valor.
3. El CLI detectará automáticamente el token.

### Opción B: Login Interactivo (Solo para Humanos)
1. Ejecutar `supabase login`.
2. Seguir el enlace al navegador y autorizar.

## 3. Trampas Conocidas
- **No confundir con SERVICE_ROLE_KEY:** El Access Token es para el CLI, no para la base de datos.
- **Project Ref:** Siempre incluir `--project-ref {id}` si se opera sobre un proyecto específico.

## 4. Pasos para Arreglar "Arregla esto"
1. Solicitar el `SUPABASE_ACCESS_TOKEN` al usuario.
2. Guardarlo en el archivo `CREDENCIALES.txt` para futura referencia (con precaución).
3. Ejecutar el comando de secretos precedido por la variable:
   `$env:SUPABASE_ACCESS_TOKEN="..."; npx supabase secrets set ...`
