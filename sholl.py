script_sholl.py

import os
import imagej

ij = imagej.init(headless=False)  # headless=False per mantenere l'interattività

def process_images_in_directory(directory, main_dir):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".tif", ".jpg", ".png")):
                process_image(os.path.join(root, file), main_dir)

def process_image(image_path, main_dir):
    # Apri immagine in ImageJ
    ij.ui().show(ij.io().open(image_path))
    file_name = os.path.basename(image_path)

   
    ij.py.run_macro('run("Subtract Background...", "rolling=50");')
    ij.py.run_macro('run("Unsharp Mask...", "radius=1 mask=0.60");')
    ij.py.run_macro('run("Despeckle");')

 
    ij.py.run_macro(f'waitForUser("Step 1: Microglia Selection", "Select a representative microglia in {file_name}.");')

   
    results_dir = os.path.join(main_dir, "Results", os.path.splitext(file_name)[0])
    os.makedirs(results_dir, exist_ok=True)
  
    ij.py.run_macro(f'saveAs("Results", "{os.path.join(results_dir, "results.csv")}");')

    print(f" Processed {file_name}")

# === MAIN ===
main_dir = input("Enter the main directory containing images: ")
process_images_in_directory(main_dir, main_dir)
