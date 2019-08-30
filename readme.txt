OS used: Windows 10 64bits
Python version: 3.7
IDE: Spyder
Dataset: Downloaded from Keras

DESCRIPTION:
The “path” is actually the folder location which is in the “Working Directory”. “Working Directory” address can be seen on the top-right side of the Spyder window. Here “gatto” is a folder name that consist of images and the resized images are also being stored in “gatto” folder.
This worked perfectly. It converted all files to their respective black and white forms. Initially the folder had 1991 images and after running the code, it had 3882 i.e., exactly double images. Unlike the most popular way to grayscale images i.e., by OpenCV, here I have used pillow because it works perfectly fine in Anaconda Navigator os Spyder ide. The code is tested in both Linux and Windows and in both places it worked perfectly fine. Sometimes it may take some time to convert all images but if the ide is not disturbed till conversion, then it will surely give expected results. 
