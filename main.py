import os
import sys
from PIL import Image

# Set list of valid file extensions
VALID_EXTENSIONS = [".jpg", ".jpeg", ".png"]



if len(sys.argv) < 1:
    folder_path = sys.argv[1]
else:
    folder_path = "photos"

file_names = os.listdir(folder_path)

for file_name in file_names:

    file_ext = os.path.splitext(file_name)[1]
    if (file_ext not in VALID_EXTENSIONS):
        continue

    # Create the old file path
    old_file_path = os.path.join(folder_path, file_name)

    # Open the image
    image = Image.open(old_file_path)

    # Get the date taken from EXIF metadata
    date_taken = image._getexif()[36867]
    image.close()

    # Reformat the date taken to "YYYYMMDD-HHmmss"
    date_time = date_taken \
        .replace(":", "")      \
        .replace(" ", "-")

    new_file_name = date_time + file_ext
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(old_file_path, new_file_path)


