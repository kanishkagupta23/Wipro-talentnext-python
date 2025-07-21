''' Problem Statement:
 Your friend has sent you a text file containing 'n' lines.
 There is a secret message that tells you:
   1. The meeting time: Determined by the number of lines in the file (convert to 12-hour format if lines > 12).
   2. The meeting place: Determined by the word that appears the most times in the file (it will be a street name).

 Write a Python program that:
   - Reads the file.
   - Finds the number of lines to determine the meeting time.
   - Finds the word with the maximum frequency to determine the street name.
   - Prints both the time and place.'''

def find_meeting_details(filename):

    with open(filename, 'r') as f:
        lines = f.readlines()

    num_lines = len(lines)
    if num_lines == 0:
        print("No content in the file.")
        return


    if num_lines > 12:
        meeting_hour = num_lines - 12  
        period = "PM"
    else:
        meeting_hour = num_lines
        period = "AM"

    if num_lines == 12:
        period = "PM"
    meeting_time = f"{meeting_hour} {period}"

   
    from collections import Counter
    
    import re
    words = []
    for line in lines:
        words_in_line = re.findall(r'\b\w+\b', line)
        words.extend(words_in_line)
   
    word_counts = Counter(word.lower() for word in words)
    meeting_place = word_counts.most_common(1)[0][0]

    print("Meeting time:", meeting_time)
    print("Meeting place:", meeting_place.title() + " Street")

