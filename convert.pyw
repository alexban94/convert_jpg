from PIL import Image
import os
import sys

# Load image, save image as specified file type with same name, delete original image.


def convert(paths, new_type):
    for path in paths:
        if not os.path.exists(path) or "." not in path:
            print("Error: the specified file does not exist or is a directory.")
            continue

        # Take first and last (in case more than one . in filename.)
        new_file, old_type = path.split(".")[0], path.split(".")[-1]

        if old_type == new_type:
            # Do nothing, no need to convert.
            print("Image is already the desired format.")
            continue
        elif old_type.lower() not in ["png", "webp", "jpg", "jpeg", "jfif", "pjpeg", "pjp"]:
            print("File not supported.")
            continue

        # Read image and save as new file type.
        with Image.open(path) as img:
            if img.mode != 'RGB':
                # Convert as RGB cannot support alpha channel of RGBA/P.
                img = img.convert('RGB')
            img.save(new_file + "." + new_type)
        # Delete original file.
        os.remove(path)


def test():
    # Specify test folder of images.
    test_dir = "W:\\test_folder\\*"
    import glob
    convert(glob.glob(test_dir), 'jpg')
    test_paths = glob.glob(test_dir)
    for path in test_paths:
        if ".jpg" not in path:
            print("Failed to convert an image: " + path)


if __name__ == "__main__":
    # Added functionality for multiple files.
    if len(sys.argv) >= 2:
        convert(sys.argv[1:], new_type='jpg')
    else:
        sys.exit()



