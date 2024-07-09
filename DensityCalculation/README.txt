Segmentation Density
Cassady S. Olson
 
Overview: 
cellCountDensity.ijm is an ImageJ macro designed to semi-automatically count cells and compute an area of an image for density caclulations. It is intended to select the DAPI channel of a 3 channel fluorescent image, though can be modified to run on other image types.

Within the data folder, there are three 3-channel fluorescent images to run this code on. These images are patches from the octopus axial nerve cord, stained with acetylated alpha tubulin, phallodin and DAPI.

Hardware Requirements: 
A standard computer with enough RAM to run ImageJ/FIJI

Software Requirements: 
ImageJ/FIJI v. 1.54f

OS Requirements 
This code is supported on Windows and macOS. It has been tested on Windows v. 10.0.19045 and macOS Catalina v.10.15.7.

In FIJI, make sure Area is selected under "Analyze">"Set Measurements"

Time to install: With ImageJ/FIJI already installed, time to install macro is the time to download and open. 

Instructions to run: 
cellCountDensity.ijm
Analyzes three_ant_1, three_ant_2, and three_ant_3
Expected time to run: 30 seconds on these three images. Time to run will increase with more images added. 
1. Open code in ImageJ/FIJI
2. Run the code
3. A window will pop up to set the input and output directory. Set the input directory as the data folder. Set output folder as desired location to save results. 
4. Once input and output are set, click OK to continue running the code. 
5. Code will select DAPI channel then pause for manual brightness/contrast adjustments. Use the GUI to adjust the brightness/contrast so that all nuclei/cells are highlighted. 
6. Once desired brightness/constrast is set, click "OK" on the Action Required window to continue running the code.
7. Repeat 5-6 for all images. 
8. Expected output (saved in selected output directory): 
	a. Area.csv containing total area of image
	b. Summary.csv containing cell counts for each image