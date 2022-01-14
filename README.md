# Right Click JPEG
A simple script to convert an image file to JPEG format, with instructions to install it as an option within the Windows 10 right-click context menu. This is mainly for the purpose of dealing with WEBP images, which are not yet supported by a number of applications.

The script works by loading the selected image, saving it as a JPEG and then deleting the original image. **Please note** that transparency data for the image will be lost as it is not supported by the JPEG format.

## Compiling
To compile the script yourself:
1. Setup a python environment with `pyinstaller` and `pillow` installed.
2. From the command line or terminal run `pyinstaller convert_jpeg.pyw`. Optionally include the flag `--onefile` to compile the script to a singular .exe file.
3. This will create a /dist folder where the application executable can be found.

## Installation
To add this to the context menu:
1. Download the /convert_jpg folder or compile the script yourself.
2. Place this in an appropriate directory and make a note of the exact location of the main executable, e.g. `C:\Program Files (x86)\Convert_jpg\convert.exe`.
3. Open the Windows Registry Editor.
