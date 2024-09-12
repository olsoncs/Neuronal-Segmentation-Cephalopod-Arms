**Segmentation Measurements**

Cassady S. Olson

**Overview:**

ProximalDistalAnalysis.mlx is custom MATLAB code to evaluate changes in the segmentation pattern down the proximal-distal axis of the octopus arm. Three parameters are examined: segments/sucker, sucker width, and segment width.

ExternalInternalAnalysis.mlx is custom MATLAB code to evaluate changes in the segmentation pattern between the external side of the axial nerve cord (ExA) and the internal side of the axial nerve cord (InA) and down the proximal-distal axis of the arm. Three parameters are examined: segment width, density of nuclei within the segments, and cross sectional area of the segments. 

GroupAvgSem.m is a custom MATLAB function to find the average and standard error of the mean (SEM) based on conditions. 

sigstar by Rob Campbell (2024) (raacampbell/sigstar (https://github.com/raacampbell/sigstar)) is used to apply significance stars over the plots. 

Within the data folder, there are three MATLAB files containing measurements for Arm 1, Arm 2, and cross sectional area in a data structure. The series for Arm 1 was sectioned longitudinally, stained with acetylated alpha tubulin and counterstained with phalloidin and DAPI. The series for Arm 2 was sectioned longitudinally and stained with Hematoxylin and Eosin (H&E). The series for cross sectional area was sectioned horizontally and staied with acetylated alpha tubulin. 

**Hardware Requirements:**

A standard computer with enough RAM to run MATLAB is required. 

**Software Requirements:**

MATLAB v. 2021b or later

**OS Requirements** 

This code is supported on Windows and macOS. It has been tested on Windows v. 10.0.19045 and macOS Catalina v.10.15.7.

**Dependancies**

Statistics and Machine learning toolbox in MATLAB

**Time to install:**

With MATLAB already installed, time to install the Statitistics and Machine Learning Toolbox is ~2 minutes. 

**************************
**Instructions to run:** 

Both of the codes are live scripts, so output should be displayed without needing to run the code. 

ProximalDistalAnalysis.mlx

Analyzes Arm1_Measurement.mat and Arm2_Measurement.mat

Expected run time: 15 seconds

1. Open the code in MATLAB
2. Verify the data path is correct given operating system (line 5)
3. Run Code
4. Expected output:
   
	a. segment/sucker plot down the proximal-distal axis for arm 1 and arm 2

	b. sucker width plot down the proximal-distal axis for arm 1 and arm 2

	c. stats plot for a 2 way anova for segment width

	d. segment width plot down the proximal-axis for arm 1 and arm 2 with significance stars

ExternalInternalAnalysis.mlx

Analyzes Arm1_Measurement.mat

Expected run time: 20 seconds

1. Open the code in MATLAB
2. Verify the data path is correct given operating system (line 5)
3. Run Code
4. Expected output:
   
	a. stats plot for a 2 way anova for segment width

	b. segment width plot down the proximal-axis subdivided by internal and external ANC for arm 1 with significance stars

	c. stats plot for a 2 way anova for nuclei density

	d. nuclei density plot down the proximal-distal axis subdivided by internal and external ANC for arm 1 with significance stars

   	e. cross sectional area plot across four levels of the ANC from oral to aboral, subdivided by internal and external ANC

