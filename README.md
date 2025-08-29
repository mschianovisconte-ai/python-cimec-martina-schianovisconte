# Work Protocol for Image Processing

The project consists of setting a protocol in order to automatize images processing. in this case we are going to analize cerebellum slices acquired on confocal microscope focusing our attention to the number and branching of microglia cells. The aim is to automatize in particular processes such as Cell counting and Sholl analysis.

Step 1: Set Scale

Setting the scale for images is an important step in image processing because it establishes a conversion factor between the pixel measurements in the image and real-world measurements. This allows for accurate measurements and analysis of objects in the image using known distances or units.

In this work protocol, the scale for fluorescence images taken at 20x magnification is derived from an image with the following metadata:

Width: 283.0718 microns (1702
Height: 283.0718 microns (1702)
Resolution: 6.0126 pixels per micron
Pixel size: 0.1663x0.1663 micron^2
Objective: 40x/0.95 Plan Apochromatic Lambda D

The macro or script used in this step iteratively sets the scale for images in a specified directory and its subfolders. The user is prompted to select the main directory containing the images. The macro/script retrieves a list of subdirectories within the main directory and processes each subdirectory.

For each image file in the directories, the scale parameters (distanceInPixels, knownDistance, pixelAspect, unit) are set based on the derived scale from the optimum image. The "Set Scale..." command is then used to apply the scale to the image with the "Global" option enabled.

Optionally, the updated image metadata can be saved, and the image is closed.

Work Protocol for Branching Analysis
This protocol describes automatically processing and analysing microglia images using Fiji (ImageJ). The script will:
●	Preprocess images (background subtraction, sharpening, despeckling)
●	Select and segment a single microglial cell
●	Apply thresholding and skeletonization
●	Perform Sholl analysis to quantify branching complexity
●	Automatically save results into structured folders
________________________________________
Step 1. Setting Up the Analysis
●	Open Fiji (ImageJ).
●	Ensure that the Sholl Analysis and Skeletonize (2D/3D) plugins are installed.
●	Make sure a folder named "Results" exists in your working directory. If not, create it manually before running the script.
●	Run the script in Fiji's Macro Editor.

Step 2. Selecting the Image Directory
●	When prompted, select the main folder containing your microglia images.
●	The script will process all images in this folder and any subfolders.
●	Click OK to proceed.

Step 3. Image Preprocessing
Each image undergoes the following preprocessing steps:
●	Background subtraction using a rolling ball radius of 50 pixels.
●	Sharpening using an unsharp mask (radius=1, mask=0.60).
●	Noise removal using the Despeckle function.

Step 4. Selecting a Microglia Cell
●	A preview image is created for better visibility.
●	Adjust Brightness/Contrast (Ctrl+Shift+C) to enhance the microglia.
●	Identify a healthy, isolated microglia in the center of the image.
●	Click OK once the microglia is identified

Step 5. Selecting a Region of Interest (ROI)
●	Use the Rectangle Selection Tool to draw a box around the selected microglia.
●	Ensure the entire cell is included while avoiding excess background.
●	Click OK when done.

Step 6. Thresholding to Create a Binary Image
●	Open Image -> Adjust -> Threshold
●	The thresholding window will open— move the slider to make sure the microglia is highlighted correctly. 
○	Thresholding Method: Huang
○	Color for threshold overlay: Red
○	Dark background: ✅ Enabled
○	Stack histogram: ❌ Disabled
○	Don't reset range: ✅ Enabled
○	Raw values: ❌ Disabled
○	16-bit histogram: ❌ Disabled
●	Click OK on the prompt to continue.

Step 7. Fixing Disconnected Branches
●	Examine the image for broken microglial branches.
●	If branches are disconnected, use:
○	Brush Tool (1-2px) for thicker branches.
○	Pencil Tool (0.5-1px) for faint or fine structures.
●	Click OK when all branches are connected.

Step 8. Defining the Soma
●	Use the Freehand Selection Tool to outline the soma.
●	Press Ctrl+M to measure its area.
●	Click OK to continue.

Step 9. Marking the Soma Center
●	Use the Multi-Point Tool to place a marker at the center of the soma.
●	Click OK when done.
(click outside of microglia with rectangle tool before using multi point tool)

Step 10. Skeletonization and Connectivity Check
●	The script will skeletonize the microglia.
●	Check for missing or broken connections and fix them using the Pencil Tool (0.5px).
●	Click OK when ready.

Step 11. Analyzing the Skeleton
●	The script runs Analyze Skeleton (2D/3D).
●	The results include:
○	Number of branches
○	Number of junctions
○	End-point voxels
●	These results are automatically saved to the Results folder.
●	Ensure that the results only contain one cell. If you connected all branches and cleaning the background, this should be the case.
Step 12. Performing Sholl Analysis
●	The script will prompt you to do Sholl Analysis using the soma's calculated radius. Sholl Analysis has to be run manually. Go to Plugins -> Neuroanatomy -> Sholl -> Sholl Analysis (From Image)
●	Here are the parameters:
○	Shells:
■	Start radius (micron): Add from prompt
■	Step size (micron): 1.000000000000000
■	End radius (micron): 70.000000000000000
■	Hemishells: None. Use full shells
■	Preview: ✅ (Checked)
■	Set Center from Active ROI: Button available
○	Segmentation:
■	Samples per radius: 1
■	Integration: N/A
○	Branching Indices:
■	Primary branches: Infer from starting radius
■	Value: 0
○	Polynomial Fit:
■	Degree: Use degree specified below
■	Value: 4
○	Sholl Decay:
■	Method: Automatically choose
■	Normalizer: Default
○	Output:
■	Plots: Linear plot
■	Tables: Detailed & Summary tables
■	Annotations: ROIs (points and 2D shells)
■	Annotations LUT: mpl-viridis.lut
■	Save files: ✅ (Checked)
■	Destination: Choose the Result subfolder corresponding to the sample
●	Click OK to proceed

Work Protocol for Microglia Counting using Fiji
This protocol guides users to count microglia from a set of images using a macro that automates key steps while allowing manual adjustments.
________________________________________
Step 1: Selecting Directory and Opening Images
1.	Open Fiji.
2.	Run the provided macro.
3.	A dialog box will appear asking you to select the folder containing your images.
4.	Select the appropriate folder and click OK.
5.	The macro will begin processing .tif images from the selected directory.

Step 2: Applying Threshold
1.	The macro will open each image one by one.
2.	A prompt will ask you to apply a threshold so that all microglia somas are visible.
3.	Adjust the thresholding settings:
○	Go to Image → Adjust → Threshold...
○	Modify the sliders to highlight all microglia somas while minimizing background noise. 
4.	Click OK when satisfied.

Step 3: Running Analyze Particles

1.	The macro will automatically run Analyze Particles, which will detect and highlight individual microglia.
2.	Detected microglia will be displayed as overlay masks, and their outlines will be saved in the ROI Manager.
3.	A summary table will also appear with initial measurements.

Step 4: Refining ROIs (Regions of Interest)
1.	A prompt will ask you to check the ROI Manager to remove non-microglia ROIs.Open the ROI Manager and inspect the detected particles.
2.	Select and delete any incorrect ROIs (e.g., debris or non-microglia particles). In case any microglia was missed, use the freehand tool to draw the glia and click on add. 
3.	Once finalized, save the refined ROIs:
○	In ROI Manager, go to Deselect → More >> → Save
○	Save the ROI file in the appropriate results folder.
Step 5: Measuring and Saving Results
1.	The macro will run Measure again to update results with the refined ROIs.
2.	The following files will be saved automatically in a Counting Results folder:
○	Masked Image (_masked.tif) showing detected microglia
○	ROI File (_rois.zip) containing the refined ROIs
○	Measurement Results (_results.csv) with area and count data
Step 6: Closing and Proceeding to the Next Image
1.	The macro will close all open windows.
2.	It will then move to the next image in the directory and repeat the process from Step 2 onward.
Completion
●	Once all images are processed, the macro will display the message:
 “Processing Complete.”
●	Your results will be available in the Counting Results folder.

