# 1. Write a program to add a key and value to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("1.", sample_dict)

# 2. Write a program to concatenate the following dictionaries to create a new one.
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result_dict = {}
for d in (dic1, dic2, dic3):
    result_dict.update(d)
print("2.", result_dict)

# 3. Write a program to check if a given key already exists in a dictionary.
check_dict = {1: 10, 2: 20, 3: 30}
key = 2  # Change key to check
if key in check_dict:
    print("3. Key exists")
else:
    print("3. Key does not exist")

# 4. Write a program to iterate over a dictionary using for loop and print the keys alone,
# values alone and both keys and values.
iterate_dict = {1: 10, 2: 20, 3: 30}
print("4. Keys alone:")
for k in iterate_dict:
    print(k)
print("Values alone:")
for v in iterate_dict.values():
    print(v)
print("Both keys and values:")
for k, v in iterate_dict.items():
    print(f"{k}: {v}")

# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of the keys.
squares = {i: i**2 for i in range(1, 16)}
print("5.", squares)

# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
sum_dict = {1: 10, 2: 20, 3: 30}
total = sum(sum_dict.values())
print("6.", total)