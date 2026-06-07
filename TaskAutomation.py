# TASK AUTOMATION WITH PYTHON (1: MOVE ALL .jpg FILES TO A NEW FILE)


import os
import shutil

src_folder ='source_folder'

dest_folder ='JPG_Files'

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

for file in os.listdir(src_folder):
    if file.endswith(".jpg"):
        src_path =os.path.join(src_folder,file)

        dest_path =os.path.join(dest_folder,file)

        shutil.move (src_path ,dest_path)

        print(f"Moved:{file}")

print ("all jpg files have been moved in JPG.files successfully...")

