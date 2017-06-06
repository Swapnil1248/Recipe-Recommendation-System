# For a particular user get his liked products with rating > 3.
#
# then from the list of products obtained iterate over the ingredients to generate the recommendation
#
# check for ingredients in the shorted_list for each item in the list (intersection of two lists)
#
# Look for products with common ingredients with the help of a dictionary
from collections import defaultdict
import json
short_listed = ["egg","wheat","butter","onion","garlic","milk","vegetable_oil","cream","tomato","olive_oil","black_pepper","pepper","vanilla",
"cayenne","vinegar","cane_molasses","bell_pepper","cinnamon","parsley","chicken"]

fav_list = ["B000H28ABW"]
item_to_ingredient_dict = defaultdict(lambda: [])

with open("srep00196-s3.csv") as f:
    for line in f:
        li = line.strip()
        if not li.startswith("#"):
            arr = li.split(",")
            dish_name = arr[0]
            item_to_ingredient_dict[dish_name] = arr[2:]

item_to_ingredient_dict["B000H28ABW"] = ["vinegar","chilli","pepper","salt","onion","cheese","comino","garlic","oregano","chicken","turkey","beef","tomato"]
# load inverted index
inverted_index = dict()
with open('inverted_index.json') as json_data:
    inverted_index = json.load(json_data)

recommended_list = []

for item in fav_list:
    recommended_prod = defaultdict(lambda: 0.0)
    count  = 0

    for ingredient in item_to_ingredient_dict[item]:
        if ingredient in short_listed:
            count += 1

    for ingredient in item_to_ingredient_dict[item]:
        if ingredient in short_listed:
            count += 1
            for prod in inverted_index[ingredient]:
                if prod != item:
                    recommended_prod[prod] += 1


    # print(recommended_prod)
    temp = []
    for key in  recommended_prod:
        if recommended_prod[key] / count >= 0.50:
            temp.append(key)

    recommended_list.append(set(temp))

#print the recommended list
from functools import reduce
print(reduce(set.intersection, recommended_list))

for prod in recommended_list:
     print(len(prod))