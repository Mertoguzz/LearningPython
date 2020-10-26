import os
import requests
import shutil
from download_util import download_file

THIS_FILE_PATH=os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)

DOWNLOADS_DIR=os.path.join(BASE_DIR,"downloads")

os.makedirs(DOWNLOADS_DIR,exist_ok=True)

downloaded_img_path=os.path.join(DOWNLOADS_DIR,"nature.jpg")
url  ="https://scx2.b-cdn.net/gfx/news/2019/2-nature.jpg"


# for small items
# req=requests.get(url,stream=True)
# req.raise_for_status()
# with open(downloaded_img_path,"wb") as _file:
#     _file.write(req.content)

download_file(url,DOWNLOADS_DIR)
