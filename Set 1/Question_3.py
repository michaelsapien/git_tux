"""
once match rate is found, pop out items with match rate below 70% and 
sort dictionary using the match rate in accending order
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
    matched_items_dict={
        "name":item_name,
        "match_rate": match_rate(item_name, keyword)
    }
    if matched_items_dict.get('match_rate')>=50.0:
        matched_items_list.append(matched_items_dict)
        
sorted_items_list = sorted(matched_items_list, key=lambda x: x["match_rate"])
print(json.dumps(sorted_items_list, indent=4))