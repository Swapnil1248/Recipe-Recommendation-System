import json

short_listed = ["egg","wheat","butter","onion","garlic","milk","vegetable_oil","cream","tomato","olive_oil","black_pepper","pepper","vanilla",
"cayenne","vinegar","cane_molasses","bell_pepper","cinnamon","parsley","chicken"]

inveretd_dict = dict()
for item in short_listed:
    inveretd_dict[item] = []

with open("srep00196-s3.csv") as f:
    for line in f:
        li = line.strip()
        if not li.startswith("#"):
            arr = li.split(",")
            dish_name = arr[0]
            arr = arr[2:]
            for item in arr:
                if item in short_listed:
                    temp_list = inveretd_dict[item]
                    temp_list.append(dish_name)

with open('inverted_index.json', 'w') as fp:
    json.dump(inveretd_dict, fp)