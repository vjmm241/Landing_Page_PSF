import os
import re

def optimize_html(file_path):
    if not os.path.exists(file_path):
        print(f"[ERROR] Archivo no encontrado: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Iniciando optimización de {os.path.basename(file_path)}...")

    # 1. Eliminar comentarios HTML (opcional, pero ayuda a limpiar)
    # re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL) 
    
    # 2. Simplificar espacios en blanco excesivos
    # simplified_content = re.sub(r'\n\s*\n', '\n\n', content)
    
    # 3. Buscar y corregir rutas de scripts/imágenes movidos (si no se hizo antes)
    # Ya se movieron los .md y .py, pero index.html suele referenciar imágenes en assets/
    
    # 4. Inyectar mejoras estéticas específicas (CSS)
    # Por ejemplo, asegurar que el gradiente de fondo sea más suave o tenga efectos modernos.
    modern_styles = """
    /* Modern UI Enhancements */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .text-gradient {
        background: linear-gradient(135deg, #fff 0%, var(--primary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    """
    
    if "</style>" in content:
        content = content.replace("</style>", f"{modern_styles}\n    </style>")
        print("[OK] Estilos modernos inyectados.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"[OK] {os.path.basename(file_path)} optimizado.")

if __name__ == "__main__":
    optimize_html(r"c:/Users/victo/OneDrive/Documents/Landing_Page_PSF/index.html")
    optimize_html(r"c:/Users/victo/OneDrive/Documents/Landing_Page_PSF/nuestra-solucion.html")
