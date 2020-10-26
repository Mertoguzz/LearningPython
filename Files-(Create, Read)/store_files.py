import os
BASE_DIR =os.path.dirname(os.path.abspath(__file__))

files_dir=os.path.join(BASE_DIR,"images")

# if not os.path.exists(files_dir):
#     print("Not a valid path")


os.makedirs(files_dir,exist_ok=True)

my_images=range(0,12)

for i in my_images:
    fname=f"{i}.jpg"
    file_path=os.path.join(files_dir,fname)
    if os.path.exists(file_path):
        print("skipped {fname}")
        continue
    with open(file_path ,"w") as _file:
        _file.write("Hello")

