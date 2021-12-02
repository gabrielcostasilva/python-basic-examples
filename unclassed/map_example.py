vector = [{"name": "John Doe", "age": 37}, {"name": "Anna Doe", "age": 35}]

# for item in vector:
#     print(item["name"])

print(list(map(lambda item: item["name"], vector)))
