# File written by ChatGPT to replace backgrounds with white color

from rembg import remove
from PIL import Image, ImageOps
import os
import io

# Define folders
input_folder = "screws"         # folder with original images
output_folder = "screws_clean"  # folder to save background-replaced images
background_color = (255, 255, 255)  # white background

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Load original image
        input_path = os.path.join(input_folder, filename)
        with open(input_path, "rb") as inp_file:
            input_data = inp_file.read()

        # Remove background
        output_data = remove(input_data)

        # Convert to RGBA image
        image_no_bg = Image.open(io.BytesIO(output_data)).convert("RGBA")

        # Create a solid color background image
        background = Image.new("RGBA", image_no_bg.size, background_color + (255,))

        # Paste the original image onto the background
        final_image = Image.alpha_composite(background, image_no_bg)

        # Convert to RGB (drop alpha) and save
        final_rgb = final_image.convert("RGB")
        output_path = os.path.join(output_folder, filename)
        final_rgb.save(output_path)

        print(f"Processed: {filename}")