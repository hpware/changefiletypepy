from PIL import Image
import os

input_image_path = "2.jpg"
image = Image.open(input_image_path)
print("Image Format: ", image.format)
print("Image Mode: ", image.mode)
print("Image size: ", image.size)