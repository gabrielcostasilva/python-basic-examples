def format_set(anInput):
    splitted_entries = anInput.split(sep=",")
    only_numeric_values = [int(x) for x in anInput if x.isnumeric()]
    return set(only_numeric_values)

first_set = input("Enter a set of positive integers separated by comma for the first set: ").strip()
second_set = input("Enter a set of positive integers separated by comma for the second set: ").strip()

first_set_formatted = format_set(first_set)
second_set_formatted = format_set(second_set)

print(f"Union set is {first_set_formatted.union(second_set_formatted)}")
print(f"Intersection set is {first_set_formatted.intersection(second_set_formatted)}")