#https://bama.ir/api/car/search?brand=samand&image=1


import pandas as pd

import requests_html
session = requests_html.HTMLSession()
url = session.get('https://bama.ir/cad/api/filter/all?mileageFrom=1&region=ardebil%2Cardabil&pageIndex=1')
js = url.json()
for i in js['data']['prices']['items']:
    # print(f'{i["title"]} ---- {i["modelyear"]} ---- {i["price"]}')
    dic = {'title' :i["title"] , 'year':i["modelyear"]  , 'price' :i["price"] }
    print(dic)
