import os
import sys
from PIL import Image

VALID_EXTENSIONS = [".jpg", ".jpeg", ".png"]


if len(sys.argv) > 1:
    folder_path = sys.argv[1]
else:
    folder_path = "photos"

file_names = os.listdir(folder_path)
for file_name in file_names:

    file_ext = os.path.splitext(file_name)[1]
    if (file_ext not in VALID_EXTENSIONS):
        continue


    old_file_path = os.path.join(folder_path, file_name)
    image = Image.open(old_file_path)

    if 36867 in image._getexif().keys():
        date_taken = image._getexif()[36867]
    elif 306 in image._getexif().keys():
        date_taken = image._getexif()[306]
    else:
        print("No date in file: %s" % (file_name))
        continue

    image.close()

    # Format date to "YYYYMMDD-HHmmss"
    date_time = date_taken \
        .replace(":", "")      \
        .replace(" ", "-")

    new_file_name = date_time + file_ext
    new_file_path = os.path.join(folder_path, new_file_name)
    
    if "tests" in new_file_path:
        print("dryrun no renaming: ",new_file_name,new_file_path)
    else:
        os.rename(old_file_path, new_file_path)


