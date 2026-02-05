# CONFIGURACIÓN OBLIGATORIA EN SUPABASE DASHBOARD

> **IMPORTANTE:** Estas configuraciones (SMTP y Plantillas de Email) **NO** se pueden subir mediante código. Es una restricción de seguridad de Supabase. Debes copiar y pegar estos valores manualmente en el panel.

## 1. Configurar SMTP (Para que los correos lleguen bien y sin alerta roja)
Ve a: **Settings** -> **Auth** -> **SMTP Settings**
Activa **Enable Custom SMTP** e introduce:

| Campo | Valor |
|---|---|
| **Sender Email** | `no-reply@prosmartfactories.com` |
| **Sender Name** | `Pro Smart Factories` |
| **Host** | `smtp.hostinger.com` |
| **Port** | `587` |
| **Username** | `no-reply@prosmartfactories.com` |
| **Password** | `4V/t6@Vb[4` |
| **Simulated** | (Dejar desactivado) |

*Dale a "Save".*

---

## 2. Configurar Plantilla de "Reset Password" (Para quitar el inglés feo)
Ve a: **Auth** -> **Email Templates** -> **Reset Password**.

**Subject:**
`Restablecer Contraseña - ProSmart Factories`

**Body (Source Code):**
*(Borra todo lo que hay y pega este HTML exacto)*

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body style="background-color: #030406; color: #ffffff; font-family: sans-serif; margin: 0; padding: 0;">
    <div style="max-width: 600px; margin: 0 auto; padding: 40px 20px; text-align: center;">
        <div style="color: #f97316; font-size: 24px; font-weight: 800; margin-bottom: 30px; letter-spacing: 2px; text-transform: uppercase;">
            PROSMART FACTORIES
        </div>
        <div style="background-color: #f8fafc; border-radius: 24px; padding: 40px; text-align: center;">
            <div style="font-size: 24px; font-weight: 700; margin-bottom: 12px; color: #0f172a;">
                Restablecer Contraseña
            </div>
            <div style="font-size: 16px; color: #64748b; margin-bottom: 30px; line-height: 1.5;">
                Has solicitado restablecer tu contraseña. Haz clic en el botón de abajo para elegir una nueva.
            </div>

            <a href="{{ .ConfirmationURL }}" style="display: inline-block; margin-top: 20px; padding: 16px 32px; background-color: #ea580c; color: white !important; text-decoration: none; border-radius: 12px; font-weight: 700; font-size: 16px;">
                Restablecer mi Contraseña
            </a>

            <p style="color: #475569; font-size: 14px; line-height: 1.6; margin-top: 25px;">
                Si no has solicitado este cambio, ignorar este correo. El enlace expirará pronto.
            </p>
        </div>
        <div style="margin-top: 40px; font-size: 13px; color: #94a3b8; line-height: 1.6;">
            © 2026 ProSmart Factories. Todos los derechos reservados.<br>
            Mensaje automático de seguridad.
        </div>
    </div>
</body>
</html>
```

*Dale a "Save".*

---

## 3. Configurar Plantilla de "Confirm Signup" (Código OTP 6 dígitos)
Ve a: **Auth** -> **Email Templates** -> **Confirm Signup**.

**Subject:**
`Tu Código de Verificación - ProSmart Factories`

**Body (Source Code):**
*(Borra todo y pega esto)*

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body style="background-color: #030406; color: #ffffff; font-family: sans-serif; margin: 0; padding: 0;">
    <div style="max-width: 600px; margin: 0 auto; padding: 40px 20px; text-align: center;">
        <div style="color: #f97316; font-size: 24px; font-weight: 800; margin-bottom: 30px; letter-spacing: 2px; text-transform: uppercase;">
            PROSMART FACTORIES
        </div>
        <div style="background-color: #f8fafc; border-radius: 24px; padding: 40px; text-align: center;">
            <div style="font-size: 24px; font-weight: 700; margin-bottom: 12px; color: #0f172a;">
                Verificación de Seguridad
            </div>
            <div style="font-size: 16px; color: #64748b; margin-bottom: 30px; line-height: 1.5;">
                Usa el siguiente código para acceder a la Demo Interactiva.
            </div>

            <div style="background-color: #ffffff; border: 2px dashed #f97316; border-radius: 16px; padding: 25px; font-size: 32px; font-weight: 800; letter-spacing: 4px; color: #ea580c; margin: 0 auto 30px auto; display: inline-block; min-width: 50%;">
                {{ .Token }}
            </div>

            <p style="color: #475569; font-size: 15px; line-height: 1.6; margin-bottom: 25px;">
                Este código es válido por 10 minutos.<br>
                Si no has solicitado este acceso, puedes ignorar este correo.
            </p>
        </div>
        <div style="margin-top: 40px; font-size: 13px; color: #94a3b8; line-height: 1.6;">
            © 2026 ProSmart Factories. Todos los derechos reservados.<br>
            Mensaje automático de seguridad.
        </div>
    </div>
</body>
</html>
```

*Dale a "Save".*

---

## 4. Configurar URLs de Redirección (Para que el Login funcione)
Ve a: **Authentication** -> **URL Configuration**.

**Site URL:**
`https://prosmart-demo.vercel.app`

**Redirect URLs:**
*(Añade estas dos)*
- `https://prosmart-demo.vercel.app/**`
- `http://localhost:3000/**` (Opcional, para pruebas locales)

*Dale a "Save".*

---

## 5. Configurar Storage (Para subir PDFs)
Ve a: **Storage**.
Debes crear 2 Buckets **si no existen**:

### Bucket 1: `user_documents`
- **Name:** `user_documents`
- **Public:** NO (Debe ser privado)
- **Allowed MIME types:** `application/pdf`
- **File size limit:** 10MB

### Bucket 2: `document_images`
- **Name:** `document_images`
- **Public:** NO (Privado)
- **Allowed MIME types:** `image/*`

*No necesitas configurar políticas (RLS) manualmente si ya corriste la migración, pero ASEGÚRATE de que los buckets existan con estos nombres exactos.*

---

## 6. Resumen Final
Has configurado manualmente:
1.  ✅ **SMTP** (Hostinger)
2.  ✅ **Plantillas de Email** (Reset & Confirm)
3.  ✅ **URLs** (Vercel)
4.  ✅ **Buckets** (Storage)

**¡TODO LISTO!** Tu proyecto está 100% configurado para producción.
