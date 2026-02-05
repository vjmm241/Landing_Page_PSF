import os
import shutil
import glob

# DIRECTIVA: LIMPIEZA_Y_ORGANIZACION_SOP
# Script para limpiar y organizar el proyecto PSF.

def main():
    base_dir = r"c:/Users/victo/OneDrive/Documents/Landing_Page_PSF"
    
    # 1. Eliminar carpetas obsoletas
    folders_to_delete = ["_archive", "server"]
    for folder in folders_to_delete:
        path = os.path.join(base_dir, folder)
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"[DELETE] Carpeta eliminada: {folder}")
            except Exception as e:
                print(f"[ERROR] No se pudo eliminar {folder}: {e}")

    # 2. Asegurar existencia de carpetas destino
    dest_dirs = ["docs", "scripts", "assets", "directivas"]
    for d in dest_dirs:
        os.makedirs(os.path.join(base_dir, d), exist_ok=True)

    # 3. Definir reglas de movimiento (archivo_pattern, carpeta_destino)
    # Evitamos mover archivos esenciales de la raíz
    essential_root_files = [
        "index.html", "nuestra-solucion.html", "aviso-legal.html", 
        "politica-cookies.html", "politica-privacidad.html",
        "vercel.json", "package.json", "package-lock.json",
        "robots.txt", "sitemap.xml", ".env", ".env.local", ".gitignore"
    ]

    # Mover archivos .py y .js sueltos a scripts/
    for ext in ["*.py", "*.js"]:
        for f_path in glob.glob(os.path.join(base_dir, ext)):
            fname = os.path.basename(f_path)
            if fname not in essential_root_files and fname != "limpiar_proyecto.py":
                dest = os.path.join(base_dir, "scripts", fname)
                try:
                    shutil.move(f_path, dest)
                    print(f"[MOVE] {fname} -> scripts/")
                except Exception as e:
                    print(f"[ERROR] Moviendo {fname}: {e}")

    # Mover archivos .md sueltos (excepto README.md si lo hubiera, que no hay según listado)
    for f_path in glob.glob(os.path.join(base_dir, "*.md")):
        fname = os.path.basename(f_path)
        if fname not in essential_root_files:
            # Si es una directiva, a directivas/
            if "_SOP" in fname or "directiva" in fname.lower() or fname == "implementation_monitor.md":
                dest_sub = "directivas"
            else:
                dest_sub = "docs"
            
            dest = os.path.join(base_dir, dest_sub, fname)
            try:
                shutil.move(f_path, dest)
                print(f"[MOVE] {fname} -> {dest_sub}/")
            except Exception as e:
                print(f"[ERROR] Moviendo {fname}: {e}")

    # Mover imágenes sueltas a assets/ (si las hubiera en raíz)
    for ext in ["*.png", "*.jpg", "*.jpeg", "*.svg", "*.ico"]:
        for f_path in glob.glob(os.path.join(base_dir, ext)):
            fname = os.path.basename(f_path)
            if fname not in essential_root_files:
                dest = os.path.join(base_dir, "assets", fname)
                try:
                    shutil.move(f_path, dest)
                    print(f"[MOVE] {fname} -> assets/")
                except Exception as e:
                    print(f"[ERROR] Moviendo {fname}: {e}")

    print("\n[OK] Limpieza y organización completada.")

if __name__ == "__main__":
    main()
