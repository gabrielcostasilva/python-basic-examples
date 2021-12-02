from json import dumps, loads

json_content = '{"name": "John Doe", "age": 37, "job": null, "married": false}'
json_dict = loads(json_content)
print(json_dict["name"])
print(json_dict)

json_dict_back = dumps(json_dict)
print(json_dict_back)

print(dumps(["item 1", "item 2", "item 3"], indent=4))
