# 🚀 Guía de Inicio Rápido - ProSmart Factories

## ⚡ Inicio Automático (Recomendado)

### Opción 1: Inicio Completo (TODO)
Haz **doble clic** en:
```
ABRIR_DEMO.bat
```
Esto hará:
1. ✅ Iniciar el **servidor web** (puerto 8000)
2. ✅ Iniciar el **servidor backend IA** (puerto 3001)
3. ✅ Abrir la demo en tu navegador
4. ✅ Todo listo para usar

### Opción 2: Solo Servidores (sin abrir navegador)
Haz **doble clic** en:
```
INICIAR_TODO.bat
```
Luego abre manualmente: `http://localhost:8000/nuestra-solucion.html`

---

## 🔧 ¿Por qué DOS servidores?

La aplicación necesita **2 servidores funcionando simultáneamente**:

1. **Servidor Web (Puerto 8000)**: Sirve los archivos HTML/CSS/JS
2. **Servidor Backend IA (Puerto 3001)**: Procesa PDFs y consultas a Gemini

Ambos deben estar corriendo para que la demo funcione.

---

## 📋 Inicio Manual

Si prefieres hacerlo manualmente, necesitas abrir **2 terminales**:

### Terminal 1: Servidor Web
```bash
cd server
node web-server.js
```

### Terminal 2: Servidor Backend IA
```bash
cd server
node server.js
```

### 3. Abrir la Demo
Abre en tu navegador: `http://localhost:8000/nuestra-solucion.html`

> ⚠️ **Importante**: NO uses `file:///` - Debe ser `http://localhost:8000`

---

## ❓ Solución de Problemas

### "Error de conexión con el cerebro IA"
**Causa**: El servidor no está corriendo  
**Solución**: Ejecuta `INICIAR_SERVIDOR.bat`

### "Cannot find module"
**Causa**: Falta instalar dependencias  
**Solución**: 
```bash
cd server
npm install
```

### Verificar si el servidor está corriendo
```bash
netstat -ano | findstr :3001
```
Si no ves nada, el servidor no está activo.

---

## 🔧 Configuración

### Variables de Entorno
El servidor usa el archivo `server/.env`:
- `GEMINI_API_KEY`: Clave API de Google Gemini
- `PORT`: Puerto del servidor (3001 por defecto)

### Modelo de IA
Actualmente configurado con: `models/gemini-flash-latest`

---

## 📝 Notas Importantes

- ⚠️ **NO CIERRES** la ventana del servidor mientras uses la demo
- ⚠️ El servidor debe estar **siempre corriendo** para que el chat funcione
- ✅ Para detener el servidor: `Ctrl+C` en su ventana o ciérrala
- ✅ Los scripts `.bat` facilitan el inicio, pero puedes usar comandos manuales

---

## 🎯 Flujo de Uso

1. **Ejecutar** `ABRIR_DEMO.bat` (solo una vez)
2. **Completar** el flujo de autenticación en la demo
3. **Subir** un manual PDF
4. **Chatear** con el Encargado Digital
5. **Cerrar** la ventana del servidor cuando termines

---

**¿Necesitas ayuda?** El servidor muestra logs en tiempo real para debugging.
