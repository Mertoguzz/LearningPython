import datetime
import requests
from requests_html import HTML

now=datetime.datetime.now()
year=now.year

#comma separated values(csv)

def url_to_txt(url,filename="world.html",save=False):
    req=requests.get(url)
    if req.status_code==200:
        html_text=req.text
        if  save:
            with open(f"world-{year}.html",'w') as _file:
                _file.write(html_text)
        return html_text    

    return ""    


url="https://www.boxofficemojo.com/year/world/"

html_text=url_to_txt(url)
r_html=HTML(html=html_text)
table_class=".imdb-scroll-table"
r_table=r_html.find(table_class)

if len(r_table)==1:
    parsed_table=r_table[0]
    rows=parsed_table.find("tr")
    header=rows[0]
    for row in rows[1:]:
        print(row.text)
