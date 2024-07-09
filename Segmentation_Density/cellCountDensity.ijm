////Cell Count Density
//Semi-automated macro to count cells in an image and compute area of the image for density calculations
//Set up to select the DAPI channel of a 3 channel fluorescent image
// Cassady S. Olson

//Sets input and output directory and file type to look for
#@ File (label = "Input directory", style = "directory") input
#@ File (label = "Output Directory", style = "directory") output
#@ String (label = "File suffix", value = ".tif") suffix

// Gets list of files from the folder
arr=getFileList(input);

// Sorts file list in appropriate numerical order bc imagej is dumb
arr_num= extract_digits(arr);
Array.sort(arr_num, arr);


// Function to sort the file list 
function extract_digits(a) {
	arr2 = newArray; //return array containing digits
	for (i = 0; i < a.length; i++) {
		str = a[i];
		digits = "";
		for (j = 0; j < str.length; j++) {
			ch = str.substring(j, j+1);
			if(!isNaN(parseInt(ch)))
				digits += ch;
		}
		arr2[i] = parseInt(digits);
	}
	return arr2;
}

// Total number of images
totalImages = arr.length;
fileNumber = 0;

// Creates a table to save the area measurement to 
report = "Area";
Table.create(report);
Table.update();

//For loop to get the cell counts and area
for (i = 0; i < totalImages; i++){
	fileNumber = fileNumber + 1; 
	// Opens the composite file and selects the dapi channel
	// not needed for the colormetric images  
	open(input + File.separator + arr[i]);
	imageTitle = getTitle();
	run("Split Channels");
	selectWindow("C3-" + imageTitle);
	close();
	selectWindow("C1-" + imageTitle);
	close();
	// Brightness and contrast adjustments 
	resetMinAndMax();
	run("Brightness/Contrast...");
	waitForUser;
	//run("Enhance Contrast", "saturated=0.85");
	// Sets file type to 8-bit (needed for thresholding)
	run("8-bit");
	// Run the thresholding 
	setAutoThreshold("Default Dark");
	setThreshold(50, 255);
	
	run("Convert to Mask");
	//waitForUser;
	// adjustments to the thresholding mask to make it "more accurate"
	run("Fill Holes");
	run("Watershed");
	//waitForUser;
	// Count the number of cells (creates a table)
	run("Analyze Particles...", "size=10-Infinity show=Overlay clear summarize");
	//waitForUser;
	// get the area of the image and save it to the table 
	run("Measure");
	reportGet = Table.get("Area",0);
	selectWindow(report);
	Table.set("Area", fileNumber-1, reportGet);
	Table.update();
	
	// close open image windows
	close("*");
	

}
selectWindow("Area")
saveAs("Results", output + File.separator + "Area.csv")
selectWindow("Summary")
saveAs("Results", output + File.separator + "Summary.csv")
