import csv

# Load existing data from the CSV file if available
student_scores = {}
try:
    with open('student_scores.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_scores[row['Name']] = {
                'Score': int(row['Score']),
                'Grade': row['Grade']
            }
except FileNotFoundError:
    pass  # Continue if the file doesn't exist

student_grades = {}

while True:
    name = input("What is the student's name? (Enter 'quit' to stop): ")
    if name.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    subject = input("What subject was the exam in? ")
    score = int(input("What is the student's score? "))
    student_scores[name] = {
        'Score': score,
        'Grade': ''  # Initialize Grade as empty, it will be filled later
    }

    # Assign grade and save the entry to the CSV file
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[name] = grade

    # Save the entry to the CSV file
    with open('student_scores.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Subject', 'Score', 'Grade'])
        if file.tell() == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow({'Name': name, 'Subject': subject, 'Score': score, 'Grade': grade})

print("Student Grades:")
for student, grade in student_grades.items():
    print(f"{student}: {subject} {grade}")
