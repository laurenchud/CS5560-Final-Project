# CS5560-Final-Project

This code takes an input text file, a number of training sets, and a number of tests as an input and prints the results to the console of how many device types, vendors, and products were guessed correctly from the banner.

The main file combines all of the files to run and print the results, the training.py file trains the data, and the parse_dataset.py file processes the text file in order to generate tuples of the banner type, banner, ips, device, vendor, and product.  The evaluate_banner.py file processes each banner and sorts out key words to use for evaluating the <device, vendor, product> tuple and the make_guess.py file takes the key words and makes an educated guess with the apriori algorithm based on the training data.

The banners.txt file contains 4,919 unique banners from Censys that contain the following format:
"number": {
      "banner type":
      "banner":
      "ips":
      "device":
      "vendor":
      "product":
}
