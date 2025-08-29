script_scaling.py

import os

from PIL import Image

def process_images_in_directory(directory, distance_in_pixels=6.0126, known_distance=1.0, pixel_aspect=1.0, unit="micron"):
    """
    Process all images in a directory and its subdirectories,
    setting scale metadata (simulating ImageJ's Set Scale).
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".tif", ".tiff", ".jpg", ".png")):
                image_path = os.path.join(root, file)
                set_scale_for_image(image_path, distance_in_pixels, known_distance, pixel_aspect, unit)

def set_scale_for_image(image_path, distance_in_pixels, known_distance, pixel_aspect, unit):
    """
    Open image, attach scale metadata, and re-save it.
    Note: Pillow does not natively support ImageJ calibration metadata,
    but we can embed it in TIFF tags or as a description.
    """
    img = Image.open(image_path)
    
    # Simulate scale metadata
    scale_info = f"distance={distance_in_pixels}, known={known_distance}, pixel_aspect={pixel_aspect}, unit={unit}"
    
    # Add metadata (for TIFF/PNG only some formats support this)
    metadata = img.info
    metadata["ScaleInfo"] = scale_info

    # Save back image (preserving format if possible)
    out_path = image_path  # overwrite original
    img.save(out_path, **metadata)

    print(f"Processed {image_path} with scale: {scale_info}")

# === RUN ===
main_dir = input("Enter the path to your main directory: ")
process_images_in_directory(main_dir)

