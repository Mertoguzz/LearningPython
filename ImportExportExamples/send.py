import sys
import requests
from datetime import datetime
from formatting import format_msg

def send(name,website=None,verbose=True):
    if website!=None:
        msg=format_msg(my_name=name,my_website=website)
    else:
        msg=format_msg(my_name=name)
    req =requests.get("http://httpbin.org/json")
    if  verbose:
        print(name,website)
    if req.status_code==200:
            return req.json()
    else:   
            return "Error"
    

if __name__ == "__main__":
    print(sys.argv)
    name="Unk"
    if len(sys.argv)>1:
        name =sys.argv[1]
    response=send(name,verbose=True)
    print(response)