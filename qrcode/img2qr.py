import base64
import segno # Use 'pip install segno' if you don't have it
import math
import os

FILE_PATH = "/home/_penguinator_/Downloads/compressed.zip"
CHUNK_SIZE = 2000

with open(FILE_PATH, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

total_chunks = math.ceil(len(b64_data) / CHUNK_SIZE)
if not os.path.exists("qr_grid_svg"): os.makedirs("qr_grid_svg")

for i in range(total_chunks):
    start = i * CHUNK_SIZE
    end = start + CHUNK_SIZE
    payload = f"{i}|{total_chunks}|{b64_data[start:end]}"

    # Create the QR and save as SVG
    qr = segno.make(payload, error='L')
    qr.save(f"qr_grid_svg/chunk_{i:04d}.svg", scale=1)

print(f"Generated {total_chunks} SVG QR codes.")
