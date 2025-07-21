#Create a dictionary that contains a list of people and one interesting fact about each of them. Display each person and their interesting fact. Change a fact about one of the people, add an additional person, and display the updated list. Run the program multiple times to observe if the order changes.
# Step 1: Create the initial dictionary
facts = {
    'Jeff': 'Is afraid of Dogs.',
    'David': 'Plays the piano.',
    'Jason': 'Can fly an airplane.'
}

# Step 2: Display each person and fact
for person, fact in facts.items():
    print(f"{person}: {fact}")

print()  # Blank line for readability

# Step 3: Change a fact about one person
facts['Jeff'] = 'Is afraid of heights.'

# Step 4: Add an additional person and fact
facts['Jill'] = 'Can hula dance.'

# Step 5: Display the new list
for person, fact in facts.items():
    print(f"{person}: {fact}")