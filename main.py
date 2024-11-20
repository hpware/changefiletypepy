from PIL import Image
import os

input_dir = "i/"
output_dir = "o/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files = os.listdir(input_dir)
num = 1

for file in files:
    imgpath = os.path.join(input_dir, file)
    img = Image.open(imgpath)
    filename1 = os.path.join(file)[0]
    filename2 = os.path.join(file)[1]
    filename3 = os.path.join(file)[2]
    filename4 = os.path.join(file)[3]
    newfile = filename1 + filename2 + filename3 + filename4 + str(num) + ".png"
    output_p = os.path.join(output_dir, newfile)
    img.save(output_p, format="PNG")
    num += 1
    print(f"Converted {file} to {newfile}")

print("All files converted")