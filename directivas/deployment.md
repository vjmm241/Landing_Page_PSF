# DIRECTIVA: DESPLIEGUE_PRODUCCION

> **ID:** DIRECTIVE-DEP-001
> **Script Asociado:** `scripts/verify_deployment.py`
> **Última Actualización:** 2026-01-29
> **Estado:** ACTIVO

---

## 1. Objetivos y Alcance
- **Objetivo Principal:** Desplegar la demo en Vercel conectada a Supabase.
- **Criterio de Éxito:** La aplicación es accesible vía URL pública y el chat funciona con persistencia en Supabase.

## 2. Especificaciones de Configuración

### Variables de Entorno (Vercel)
Se deben configurar las siguientes variables en el dashboard de Vercel:
- `SUPABASE_URL`: URL del proyecto Supabase.
- `SUPABASE_ANON_KEY`: Clave pública (browser).
- `SUPABASE_SERVICE_KEY`: Clave privada (server).
- `OPENAI_API_KEY`: API Key de OpenAI.
- `JWT_SECRET`: Secreto para firmar tokens.

### Base de Datos (Supabase)
- Ejecutar `docs/SCHEMA_SUPABASE.sql` en el SQL Editor de Supabase antes del primer despliegue.

## 3. Flujo de Despliegue

1. **Commit & Push:** Asegurar que todo el código esté commiteado.
2. **Vercel CLI:** Ejecutar `vercel --prod` o conectar repositorio GitHub.
3. **Verificación:** Ejecutar `scripts/verify_deployment.py` contra la URL resultante.

## 4. Notas Técnicas
- El backend usa `serverless functions`. Los archivos subidos (`uploads/`) son efímeros y se borran tras la ejecución.
- Para persistencia de archivos a largo plazo, usar Supabase Storage (Pendiente de implementación).
