import os
from PIL import Image
import json

# Color lists
colors = {
    "c1": (255, 0, 0),      # Red
    "c2": (0, 255, 0),      # Green
    "c3": (0, 0, 255),      # Blue
    "c4": (255, 255, 0),    # Yellow
    "c5": (255, 0, 255),    # Magenta
    "c6": (0, 255, 255),    # Cyan
    "c7": (0, 0, 0),        # Black
    "c8": (255, 255, 255),  # White
    # Add more colors here...
}

reverse_colors = {v: k for k, v in colors.items()}                  # Read from var

try:
    with open("setting.json", "r") as settings_file:                # Read settings from setting.json
        settings = json.load(settings_file)
        photo_folder = settings.get("photo_folder", "pics")
        photo_filename = settings.get("photo_filename", "sss.png")
except FileNotFoundError:
    photo_folder = "pics"
    photo_filename = "sss.png" 
input_filename_without_extension = os.path.splitext(photo_filename)[0]
output_file = os.path.join(photo_folder, f"{input_filename_without_extension}_output.txt")

try:
    image_path = os.path.join(photo_folder, photo_filename)
    img = Image.open(image_path)
    width, height = img.size

    with open(output_file, "w", encoding="utf-8") as output:
        for y in range(height):
            output_line = ""
            for x in range(width):
                pixel_color = img.getpixel((x, y))
                color_variable = reverse_colors.get(pixel_color, "Unknown")
                output_line += f"{color_variable}, ({x}, {y}) | "
            output.write(output_line.rstrip(" | ") + "\n")

    print(f"Processing complete. Output written to '{output_file}'.")

except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    with open(output_file, "a", encoding="utf-8") as output:
        output.write(f"An error occurred: {str(e)}\n")
    print(f"An error occurred: {str(e)}")
