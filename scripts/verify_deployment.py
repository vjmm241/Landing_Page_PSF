import requests
import sys

def verify_deployment(url):
    print(f"🔍 Verificando despliegue en: {url}")
    
    # 1. Check Frontend
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print(f"[OK] Frontend accesible ({len(res.text)} bytes)")
        else:
            print(f"[ERROR] Frontend retornó {res.status_code}")
    except Exception as e:
        print(f"[ERROR] No se pudo conectar al frontend: {e}")

    # 2. Check Backend Health/Auth (using random token to expect 403 or specific error, ensuring connectivity)
    api_url = f"{url.rstrip('/')}/api/auth/me"
    try:
        res = requests.get(api_url, timeout=5)
        # We assume 403 Forbidden is correct because we didn't send a token
        if res.status_code == 403:
             print(f"[OK] API accesible (403 Forbidden como esperado)")
        else:
             print(f"[WARN] API retornó {res.status_code} (esperado 403 sin token)")
    except Exception as e:
        print(f"[ERROR] Falló conexión API: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python verify_deployment.py <URL_PRODUCCION>")
        print("Ej: python verify_deployment.py https://mi-proyecto.vercel.app")
    else:
        verify_deployment(sys.argv[1])
