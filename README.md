# image_splat
Some tools to allow for the generation and display of images pertaining to a given input prompt

REQUIREMENTS:  
google_images_download  
pyglet  
textblob  
Pillow  

Usage:
in main play.py, be sure to add 'from megtools import imageGen'  
Images can then be generated from a given text by calling  
'imageGen.image_response(text, image_flavour, image_samples, image_format)'  
image_flavour should be a string describing in two or fewer words what sort of images you want to see, e.g. 'Fantasy art'  
image_samples should be an integer. This is the pool of image results to choose from when picking the image to display.  
image_format should be one of: 'png' , 'jpg', 'gif', 'bmp'  
if image_format is 'gif', animated gifs will be displayed.  

included is a batch file installer for the required packages for windows.  
