from PIL import Image
from pathlib import *
import os

img_path = Path(input("Image path: ").strip('"'))
print("Image size: {} MB".format(round(os.stat(img_path).st_size/1e6), 2))
type = input("Compression? [Lossy/jpg]:\n1. Lossy (jpg)\n2. Lossless (png)\n\n")

if ("2" or "less" or "png") in type.lower():
    ext = ".png"
    frmt = ext.strip(".")
else:
    ext = ".jpg"
    frmt = "jpeg"

temp_name = "tmp_" + img_path.stem + ext
output_name = "compressed_" + img_path.stem + ext
temp = img_path.parent / temp_name
output = img_path.parent / output_name

img = Image.open(img_path)
if img.mode in ("RGBA", "P"): img = img.convert("RGB")

n = 0
qual = 100
while (n != 3):
    qlty = int(input("Quality of compression [{}]: ".format(str(qual))) or qual)
    img.save(temp, optimize=True, format=frmt, quality=qlty)
    print("File size: {} MB".format(round(os.stat(temp).st_size/1e6, 2)))
    done = input("Do you want to save? [No]:\n1. No\n2. Yes\n\n")
    if ("2" or "y") in done.lower():
        n = 3
    qual -= 5

img.save(output, optimize=True, format=frmt, quality=qlty)

delete = input("Do you want to delete the original image? [No]:\n1. No\n2. Yes\n\n")
if ("2" or "y") in delete.lower():
    os.remove(img_path)
os.remove(temp)
input("Press any key to exit! ")