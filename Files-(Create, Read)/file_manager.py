  #    //operationSystems
import os 
#absolute path
this_file_path=os.path.abspath(__file__)

BASE_DIR=os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR=os.path.dirname(BASE_DIR)

#relativepath
email_txt=os.path.join("templates","email.txt") 

content=""
with open (email_txt,'r') as _file:
    content=_file.read()



print(content.format(name='Mert'))    