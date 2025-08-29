script_counting.py

import os
import imagej

# Inizializza ImageJ con GUI
ij = imagej.init(headless=False)

def process_images(directory):
    if not os.path.isdir(directory):
        print("No directory selected")
        return
    
    output_dir = os.path.join(directory, "Counting Results")
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(directory):
        if not file.lower().endswith(".tif"):
            continue

        image_path = os.path.join(directory, file)
        name = os.path.splitext(file)[0]
        print(f"Processing {file}")

        ij.py.run_macro(f'open("{image_path}");')
        ij.py.run_macro(f'run("Duplicate...", "title={name}");')

        result_folder = os.path.join(output_dir, name)
        os.makedirs(result_folder, exist_ok=True)

        # Step 1: Threshold manuale
        ij.py.run_macro('waitForUser("Threshold", "Apply threshold so all the soma is visible, then click OK.");')

        # Step 2: Analyze Particles
        ij.py.run_macro('run("Analyze Particles...", "size=20-Infinity show=[Overlay Masks] display clear summarize overlay add");')

        # Step 3: Refine ROIs
        ij.py.run_macro('waitForUser("Refine ROIs", "Check ROI Manager and delete non-microglia ROIs, then click OK.");')
        ij.py.run_macro('waitForUser("Save ROIs", "Go to ROI Manager → More >> → Save in the correct folder, then click OK.");')

        # Step 4: Measure
        ij.py.run_macro('run("Measure");')

        # Step 5: Saving results
        ij.py.run_macro(f'saveAs("Tiff", "{os.path.join(result_folder, name + "_masked.tif")}");')
        ij.py.run_macro('selectWindow("Results");')
        ij.py.run_macro(f'saveAs("Results", "{os.path.join(result_folder, name + "_results.csv")}");')

        ij.py.run_macro('close("Results");')
        ij.py.run_macro('run("Close All");')

    print

# === RUN ===
main_dir = input("Enter the directory containing images: ")
process_images(main_dir)
