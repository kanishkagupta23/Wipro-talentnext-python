# 1. Write a program to remove a given item from the set.
sample_set = {10, 20, 30, 40, 50}
item_to_remove = 30
sample_set.discard(item_to_remove)  # discard does not raise error if item is not present
print("1. Set after removing item:", sample_set)

# 2. Write a program to create an intersection of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
intersection_set = set1 & set2  # or set1.intersection(set2)
print("2. Intersection of sets:", intersection_set)

# 3. Write a program to create a union of sets.
union_set = set1 | set2  # or set1.union(set2)
print("3. Union of sets:", union_set)

# 4. Write a program to find the maximum and minimum value in a set.
num_set = {23, 1, 56, 9, 34}
max_val = max(num_set)
min_val = min(num_set)
print("4. Maximum value in set:", max_val)
print("   Minimum value in set:", min_val)