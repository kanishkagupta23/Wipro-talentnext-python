# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
sample_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
print("1. 4th element from first:", sample_tuple[3])
print("   4th element from last:", sample_tuple[-4])

# 2. Write a program to check whether an element exists in a tuple or not.
element = 50
if element in sample_tuple:
    print("2. Element exists in tuple")
else:
    print("2. Element does not exist in tuple")

# 3. Write a program to convert a list into a tuple.
sample_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(sample_list)
print("3. Converted tuple:", converted_tuple)

# 4. Write a program to find the index of an item in a tuple.
item_to_find = 60
if item_to_find in sample_tuple:
    idx = sample_tuple.index(item_to_find)
    print("4. Index of", item_to_find, "is", idx)
else:
    print("4. Item not found in tuple.")

# 5. Write a program to replace last value of tuples in a list to 100.
tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
modified_list = [t[:-1] + (100,) for t in tuple_list]
print("5. Modified list:", modified_list)
