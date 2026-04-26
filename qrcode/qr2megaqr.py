import glob
import os
import math

SOURCE_DIR = "qr_grid_svg"
OUTPUT_FILE = "mega_qr_card.svg"
TILE_SIZE = 100 # Internal coordinate units

files = sorted(glob.glob(os.path.join(SOURCE_DIR, "*.svg")))
total_files = len(files)

cols = math.ceil(math.sqrt(total_files))
rows = math.ceil(total_files / cols)

# Start building the Master SVG string
svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{cols * TILE_SIZE}" height="{rows * TILE_SIZE}" viewBox="0 0 {cols * TILE_SIZE} {rows * TILE_SIZE}">'
svg_footer = '</svg>'
svg_body = ""

for index, file in enumerate(files):
    x = (index % cols) * TILE_SIZE
    y = (index // cols) * TILE_SIZE

    # We use an <image> tag to reference the local SVG files
    # Note: For printing, it's better to embed the content, but referencing is faster for testing.
    filename = os.path.basename(file)
    svg_body += f'<image xlink:href="{SOURCE_DIR}/{filename}" x="{x}" y="{y}" width="{TILE_SIZE}" height="{TILE_SIZE}" />\n'

with open(OUTPUT_FILE, "w") as f:
    f.write(svg_header + svg_body + svg_footer)

print(f"Vector masterpiece saved as {OUTPUT_FILE}")
