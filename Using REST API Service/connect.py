import requests
import pprint #beautifier
import pandas as pd
api_key="xxxxxxxxxxxxxxxxxxx"
api_key_v4="yyyyyyyyyyyyyyyyyyy"

#HTTP requests methods
"""
GET -grab data
POST-add or update data
PATCH
DELETE
PUT

https://api.themoviedb.org/3/movie/550?api_key=sssssssssssssss
"""
## whats our endpoint(url)
## whatis the HTTP method we need
movie_id=500
api_version=3
api_base_url=f"https://api.themoviedb.org/{api_version}"
endpoint_path=f"/movie/{movie_id}"
endpoint=f"{api_base_url}{endpoint_path}?api_key={api_key}"

req=requests.get(endpoint)#, data={"api_key":api_key})
# print(req.status_code)
# print(req.text)

#using v4
movie_id=500
api_version=4
api_base_url=f"https://api.themoviedb.org/{api_version}"
endpoint_path=f"/movie/{movie_id}"
endpoint=f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers={
'Authorization':f'Bearer {api_key_v4}',
'Content-Type':'application/json;charset=utf-8'
}

req=requests.get(endpoint,headers=headers)#, data={"api_key":api_key})
# print(req.status_code)
# print(req.text)


api_base_url=f"https://api.themoviedb.org/{api_version}"
endpoint_path=f"/search/movie"
search_query="The Matrix"
endpoint=f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
r=requests.get(endpoint)
pprint.pprint(r.json())

if  r.status_code in range(200,299):
    data =r.json()
    results=data['results']
    if len(results)  > 0:
        # print(results[0].keys())
        movie_ids=set()
        for result in results:
            _id=result['id']
            # print(result['title'],_id)
            movie_ids.add(_id)
        # print (list(movie_ids))    

output='movies.csv'
movie_data=[]
for movie_id in movie_ids:
    api_version=3
    api_base_url=f"https://api.themoviedb.org/{api_version}"
    endpoint_path=f"/movie/{movie_id}"
    endpoint=f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r=requests.get(endpoint)
    if  r.status_code in range(200,299):
        data=r.json()
        movie_data.append(data)
    # print(r.json())

df=pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output,index=False)