import csv

# Load existing data from the CSV file if available
student_scores = {}
try:
    with open('student_scores.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_scores[row['Name']] = int(row['Score'])
except FileNotFoundError:
    pass  # Continue if the file doesn't exist

student_grades = {}

while True:
    name = input("What is the student's name? (Enter 'quit' to stop): ")
    if name.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    subject = input("What subject was the exam in? ")
    score = int(input("What is the student's score? "))
    student_scores[name] = score

    # Save the entry to the CSV file
    with open('student_scores.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Subject', 'Score'])
        if file.tell() == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow({'Name': name, 'Subject': subject, 'Score': score})

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
