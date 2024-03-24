student_scores = {}

name = input("What is your name? ")
score = int(input("What is your score? "))  # Convert score to integer

student_scores[name] = score  # Add the entered name and score to the dictionary

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
