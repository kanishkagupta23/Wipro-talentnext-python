# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
my_list = [10, 20, 30, 40, 50]
print("List items:", my_list)
print("Access using index:")
for i in range(len(my_list)):
    print(f"Element at index {i}:", my_list[i])

# 2. Write a program to append a new item to the end of the list.
my_list.append(60)
print("After appending 60:", my_list)

# 3. Write a program to reverse the order of the items in the list.
my_list.reverse()
print("Reversed list:", my_list)

# 4. Write a program to print the number of occurrences of a specified element in a list.
specified_element = 20
occurrences = my_list.count(specified_element)
print(f"Number of occurrences of {specified_element}:", occurrences)

# 5. Write a program to append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("After appending list1 to the front of list2:", list2)

# 6. Write a program to insert a new item before the second element in an existing list.
my_list = [10, 20, 30, 40, 50]
my_list.insert(1, 15) # Inserts 15 before the second element (index 1)
print("After inserting 15 before the second element:", my_list)

# 7. Write a program to remove the item from a specified index in a list.
remove_index = 2
removed_item = my_list.pop(remove_index)
print(f"After removing element at index {remove_index} ({removed_item}):", my_list)

# 8. Write a program to remove the first occurrence of a specified element from a list.
specified_element = 40
if specified_element in my_list:
    my_list.remove(specified_element)
    print(f"After removing the first occurrence of {specified_element}:", my_list)
else:
    print(f"{specified_element} is not in the list.")