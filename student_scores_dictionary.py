student_scores = {}
student_grades = {}

while True:
    name = input("What is the student's name? (Enter 'quit' to stop): ")
    if name.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    subject = input("What subject was the exam in? ")
    score = int(input("What is the student's score? "))
    student_scores[name] = score

for student, score in student_scores.items():
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print("Student Grades:")
for student, grade in student_grades.items():
    print(f"{student}: {subject} {grade}")

# Next task:

# 2. Adding each entry to the dictionary
