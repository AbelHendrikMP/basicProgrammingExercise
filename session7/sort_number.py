NumList = [10, 20, 5, 40, 30, 72, 34]
smallest = largest = NumList[0]
for num in NumList:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("The Smallest Element in this List is:", smallest)
print("The Largest Element in this List is:", largest)
