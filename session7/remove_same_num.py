original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_set = set()
unique_list = []

for item in original_list:
    if item not in unique_set:
        unique_set.add(item)
        unique_list.append(item)

print("The list after removing duplicates:", unique_list)
