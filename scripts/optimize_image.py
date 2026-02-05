from PIL import Image
import os

input_path = "assets/VictorMarquinaFactories.png"
output_path = "assets/images/VictorMarquina_Optimized.jpg"

# Create directory if not exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

try:
    with Image.open(input_path) as img:
        # Convert to RGB regardless of original mode
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize maintaining aspect ratio
        base_width = 1000
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
        
        # Save with high quality optimization
        img.save(output_path, "JPEG", quality=90, optimize=True)
        
        # Get file sizes
        original_size = os.path.getsize(input_path) / 1024 / 1024
        new_size = os.path.getsize(output_path) / 1024 / 1024
        
        print(f"Image optimized successfully!")
        print(f"  Original: {original_size:.2f} MB")
        print(f"  Optimized: {new_size:.2f} MB")
        print(f"  Saved: {output_path}")
except Exception as e:
    print(f"Error: {e}")

