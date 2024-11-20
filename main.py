from PIL import Image

input_image_path = "filehere.jpg"
image = Image.open(input_image_path)
print("Image Format: ", image.format)
print("Image Mode: ", image.mode)
print("Image size: ", image.size)