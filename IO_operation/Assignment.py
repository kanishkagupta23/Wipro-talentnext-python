# 1. Write a program to read the entire content from a txt file and display it to the user.

file_path = 'sample.txt'  

with open(file_path, 'r') as f:
    content = f.read()
    print("Assignment 1 Output:")
    print(content)
    print('-' * 40)


# 2. Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Assignment 2:\nEnter number of lines to read: "))
with open(file_path, 'r') as f:
    print("Assignment 2 Output:")
    for _ in range(n):
        line = f.readline()
        if not line:
            break
        print(line, end='')
    print('\n' + '-' * 40)


# 3. Write a program to accept input from user and append it to a txt file.

user_input = input("Assignment 3:\nEnter text to append: ")
with open(file_path, 'a') as f:
    f.write(user_input + '\n')
print("Assignment 3 Output: Appended successfully.")
print('-' * 40)


# 4. Write a program to read contents from a txt file line by line and store each line into a list.

lines = []
with open(file_path, 'r') as f:
    lines = [line.rstrip('\n') for line in f]
print("Assignment 4 Output:")
print(lines)
print('-' * 40)


# 5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

longest_word = ''
with open(file_path, 'r') as f:
    for line in f:
        for word in line.split():
            if len(word) > len(longest_word):
                longest_word = word
print("Assignment 5 Output:")
print("Longest word:", longest_word)
print('-' * 40)


# 6. Write a program to count the frequency of a user entered word in a txt file.

search_word = input("Assignment 6:\nEnter the word to search for: ")
count = 0
with open(file_path, 'r') as f:
    for line in f:
        words = line.split()
        count += words.count(search_word)
print(f"Assignment 6 Output:\nFrequency of '{search_word}':", count)
print('-' * 40)
