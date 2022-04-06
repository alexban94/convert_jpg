# Right Click JPEG
A simple script to convert an image file to JPEG format, with instructions to install it as an option within the Windows 10 right-click context menu. This is mainly for the purpose of dealing with WEBP images, which are not yet supported by a number of applications.

The script works by loading the selected image, saving it as a JPEG and then deleting the original image. **Please note** that transparency data for the image will be lost as it is not supported by the JPEG format.

## Compiling
To compile the script yourself:
1. Setup a python environment with `pyinstaller` and `pillow` installed.
2. From the command line or terminal run `pyinstaller convert_jpeg.pyw`. Optionally include the flag `--onefile` to compile the script to a singular .exe file.
3. This will create a */dist* folder where the application executable can be found.

## Installation
To add this to the context menu:
1. Download the */convert_jpg folder* or compile the script yourself.
2. Place this in an appropriate directory and make a note of the exact location of the main executable, e.g. `C:\Program Files (x86)\Convert_jpg\convert_jpg.exe`.
3. Open the Windows Registry Editor and navigate to `HKEY_CLASSES_ROOT\SystemFileAssociations\`. 
4. Choose the image file extensions you want to associate with the application; personally I required it for .png and .webp.
5. Open the the specified folder e.g. '.png' and right click `Shell`, select **New > Key** and name it *"convert_jpg"*.
6. On the right hand side, double click **(Default)** and in the value data field write the text you want to appear on the context menu, such as "Convert to JPEG".
7. Right click the *convert_jpg* folder and again create a new key, this time naming it *command*.
8. In the Value data field write: `"<exe location>" "%1"`, where `<exe location>` is your own personal location for the executable from step 2.
  
Once these steps are complete you can repeat this for other file extensions, and when right clicking files of these types the entry should appear on the context menu. If this is unclear, please refer to [this article](https://thegeekpage.com/add-any-program-to-right-click-context-menu/) and [this stackoverflow explanation](https://stackoverflow.com/a/47745854).
  
**Note:** for the .webp extension, on my personal computer there was no `Shell` folder, so I simply created that as a new key within `.webp` before continuing with step 5.
