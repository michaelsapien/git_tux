"""
from the dictioanry thus created from question_1, 
write a program to accept a key word from  user and return a array of dictinary with item name and its the match rate


eg:

Enter keyword: Pink apple
result:[
    {
        "name": "Granny Smith Apples",
        "mathch rate":80
    }
    {
        "name": "Pink Lady Apples",
        "mathch rate":95
    }
    {
        "name": "Honey Crisp apple",
        "mathch rate":85
    }
]
match rate is percentage

match rate shown below are random not generated using program

Remember user can give any keyword in any format you have to clean it
"""
import json

def match_rate(item_name, keyword):
    # Split the item name into words
    item_name_list = item_name.split()
    
    # Split the keyword into words
    keyword_list = keyword.split()

    matched_words = 0

    # Count the number of matched words
    for item_word in item_name_list:
        if item_word in keyword_list:
            matched_words += 1

    # Calculate match rate as percentage of matched words
    match_rate = (matched_words / len(keyword_list)) * 100

    return match_rate

with open('data.json', 'r') as file:
    data = json.load(file)

keyword = input("Enter keyword: ")
keyword=keyword.lower()

matched_items_list = []
for item in data["items"]: 
    item_name=item["name"].lower()   
    matched_items_list.append({
        "name":item_name,
        "match_rate": match_rate(item_name, keyword)
    })
    
print(json.dumps(matched_items_list, indent=4))