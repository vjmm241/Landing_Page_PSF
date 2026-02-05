import os
import shutil

# DIRECTIVA: ORDENAR_CARPETA
# Script para mover archivos y establecer directivas.

def main():
    base_dir = r"c:/Users/victo/OneDrive/Documents/Landing_Page_PSF"
    
    # Definir movimientos: (origen_relativo, destino_relativo, nuevo_nombre_opcional)
    moves = [
        ("VictorMarquinaFactories.png", "assets/VictorMarquinaFactories.png"),
        ("optimize_image.py", "scripts/optimize_image.py"),
        ("Directiva.md", "directivas/directiva_ejemplo.md") # Renombramos al mover
    ]

    print(f"Iniciando organización en: {base_dir}")

    # Asegurar directorios destino
    for _, dest in moves:
        dest_path = os.path.join(base_dir, dest)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Ejecutar movimientos
    for src, dest in moves:
        src_path = os.path.join(base_dir, src)
        dest_path = os.path.join(base_dir, dest)

        if os.path.exists(src_path):
            try:
                # Si el destino ya existe, advertir
                if os.path.exists(dest_path):
                    print(f"ADVERTENCIA: El destino ya existe: {dest}. Sobrescribiendo...")
                    os.remove(dest_path) # Eliminar destino para permitir 'move' limpio o usar replace, shutil.move maneja esto a veces pero mejor ser explícito si queremos overwrite comportamiento

                shutil.move(src_path, dest_path)
                print(f"[OK] Movido: {src} -> {dest}")
            except Exception as e:
                print(f"[ERROR] Falló mover {src} -> {dest}: {e}")
        else:
            print(f"[SKIP] No encontrado: {src} (Posiblemente ya movido)")

    # Actualizar index.html
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Buscar referencia simple
            old_ref = 'src="VictorMarquinaFactories.png"'
            new_ref = 'src="assets/VictorMarquinaFactories.png"'
            
            if old_ref in content:
                print("[UPDATE] Actualizando referencia en index.html...")
                new_content = content.replace(old_ref, new_ref)
                
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print("[OK] index.html actualizado.")
            else:
                print("[INFO] No se encontró referencia 'src=\"VictorMarquinaFactories.png\"' en index.html (o ya actualizada).")
                
        except Exception as e:
             print(f"[ERROR] Falló actualizar index.html: {e}")
    else:
        print("[SKIP] index.html no encontrado.")

    print("\nOrganización completada.")

if __name__ == "__main__":
    main()
