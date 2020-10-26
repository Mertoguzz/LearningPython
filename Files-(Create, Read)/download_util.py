import os
import requests
import shutil


def download_file(url,directory,fname=None):

    if fname==None:
        fname=os.path.basename(url)

        path=os.path.join(directory,fname)
        with requests.get(url,stream=True) as req:
            with open(path,'wb') as  file_obj:
                shutil.copyfileobj(req.raw, file_obj)
        return path
