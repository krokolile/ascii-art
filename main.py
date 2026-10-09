from PIL import Image

image = Image.open(r"C:\Users\lsjos\Downloads\ascii-pineapple.jpg")

print("Successfully opened image!")
print(f"Image size: {image.width} x {image.height}")