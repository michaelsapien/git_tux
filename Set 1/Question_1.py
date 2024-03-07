"""
create a new  array of dictionary by extracting data from data.json
new dictionay thus created should be as shown below


[
    {
     "name": "Organic Honeycrisp Apples Bag",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    },
    {
     "name": "Granny Smith Apples",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    }
    .
    .
    .
    .
    
]


Remember to extract all items above illustrated are just sample

Reference : https://www.w3schools.com/python/python_lists_comprehension.asp
"""


import json

with open('data.json', 'r') as file:
    data = json.load(file)

product_list = []
for item in data["items"]:
    categories=item["categories"]
    product_dict = {
        "name": item["name"],
        "categories": [category['name'] for category in categories],
        "image": item["images"]["tile"]["large"],
        "base_price": item["base_price"],
        "availability_status": item["availability_status"]
    }
    product_list.append(product_dict)

print(json.dumps(product_list, indent=4))