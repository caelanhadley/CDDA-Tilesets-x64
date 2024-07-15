import os
from PIL import Image, UnidentifiedImageError

def scale_images_in_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                img_path = os.path.join(root, filename)
                try:
                    with Image.open(img_path) as img:
                        # Get current size
                        width, height = img.size
                        
                        # Scale image by a factor of 2
                        new_size = (width * 2, height * 2)
                        scaled_img = img.resize(new_size, Image.NEAREST)
                        
                        # Save the scaled image
                        scaled_img.save(img_path)
                        print(f"Scaled {img_path} to {new_size}")
                except UnidentifiedImageError:
                    print(f"Cannot identify image file {img_path}, skipping...")

# Replace 'path_to_base_directory' with the path to your base directory
base_directory = './gfx/UltimateCataclysm'
scale_images_in_directory(base_directory)
