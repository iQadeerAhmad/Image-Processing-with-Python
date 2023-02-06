# Image-Processing-with-Python


A Python script to process images in a folder and save the processed images in another folder.

## Features
- Rotate the images by 90 degrees
- Resize the images to 128x128 pixels
- Convert palette images to RGBA
- Convert other image formats to RGB
- Save the processed images as JPEG files

## Requirements
- Python 3
- PIL (Pillow) library

## Usage
1. Place your original images in the `stock_images` folder.
2. Run the script using `python3 image_processing.py`.
3. The processed images will be saved in the `processed_images` folder.

## Note
- If the `processed_images` folder does not exist, it will be created automatically.
- The script only processes actual files (ignores hidden files and directories).
- The script uses the base name of the original image files (without the extension) as the base name for the processed image files.
