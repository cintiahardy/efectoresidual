# Uso: copiá este archivo junto a la carpeta "img" y ejecutá:
#   pip install pillow
#   python optimizar.py
# Crea img/webp/ con cada foto en WebP (máx. 1600 px). Las originales no se tocan.
import re
from pathlib import Path
from PIL import Image, ImageOps

src = Path("img")
out = src / "webp"
out.mkdir(exist_ok=True)

for f in src.iterdir():
    if f.suffix.lower() in (".jpg", ".jpeg", ".png"):
        im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
        im.thumbnail((1600, 1600))
        name = re.sub(r"\s+", "-", f.stem.lower()) + ".webp"
        im.save(out / name, "WEBP", quality=78, method=6)
        print("OK", f.name, "->", name)
