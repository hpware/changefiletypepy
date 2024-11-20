from PIL import Image
import os

input_dir = "i"
output_dir = "o"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files = os.listdir(input_dir)

for file in files:
    imgpath = os.path.join(input_dir, file)
    img = Image.open(imgpath)
    newfile = os.path.join(file)[0] + ".png"
    output_dir = os.path.join(output_dir, newfile)
    img.save(output_dir, format="PNG")

    print(f"Converted {file} to Format")

print("All files converted")