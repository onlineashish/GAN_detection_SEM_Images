from PIL import Image
import os

def resize_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                image_path = os.path.join(root, file)
                image = Image.open(image_path)
                resized_image = image.resize((256, 256))
                resized_image = resized_image.convert("RGB")
                resized_image.save(image_path)

# Example usage
# resize_images("dataset")
                


