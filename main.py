#!/usr/bin/env python3

# Import the necessary modules
from PIL import Image
import os
import re

# Path to the folder containing the original images
original_images_folder = "stock_images"

def main():
    # Iterate through the files in the original images folder
    for image_file in os.listdir(original_images_folder):
        image_file_path = os.path.join(original_images_folder, image_file)
        # Check if the current file is an actual file (not a folder)
        if os.path.isfile(image_file_path):
            # Open the image and perform rotation and resizing
            image = Image.open(image_file_path)
            processed_image = image.rotate(90).resize((128, 128))
            # Check if the image is a palette image and convert it to RGBA if necessary
            if processed_image.mode == 'P':
                processed_image = processed_image.convert('RGBA')
            # Check if the image is in a format that is not RGB or grayscale and convert it to RGB if necessary
            if processed_image.mode not in ['RGB', 'L']:
                processed_image = processed_image.convert('RGB')
            # Get the base name of the image file (without the extension)
            match = re.search(r'(.*)\..*', image_file)
            if match:
                image_base_name = match.group(1)
            else:
                image_base_name=image_file

            # Define the new file extension and the folder for the processed images
            new_image_extension = ".jpeg"
            processed_images_folder = "processed_images/"
            # Create the processed images folder if it does not exist
            if not os.path.exists(processed_images_folder):
                os.makedirs(processed_images_folder)
            # Define the full path of the processed image
            processed_image_path = processed_images_folder + image_base_name + new_image_extension
            # Save the processed image
            processed_image.save(processed_image_path)

# Call the main function
main()
