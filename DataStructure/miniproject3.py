#Find the name

def average_percentage_marks(records, student_name):
    if student_name in records:
        marks = records[student_name]
        average = sum(marks) / len(marks)
        return average
    else:
        return None
