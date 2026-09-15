# File Handling Operations (saving and loading students to/from CSV)
import csv 
from student import Student, SUBJECTS

filename = 'students.csv'

HEADER = ['Name', 'Roll No'] + list(SUBJECTS) + ['Average', 'Grade', 'Created On']


def add_students(students):
    """Save the full list of Student objects to the CSV file."""
    try:
        with open(filename, 'w', newline='') as f:
           
            f.write(','.join(HEADER) + '\n')
            for s in students:
               
                f.write(s.to_csv())
        print(f'Data saved to {filename} file successfully.')
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")


def load_students():
    """Load students from the CSV file and rebuild Student objects.
    Always returns a list (empty list if the file is missing or empty)."""
    students = []
    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for parts in reader:
                if not parts:
                    continue
                name = parts[0]
                roll_no = parts[1]
                
                num_subjects = len(SUBJECTS)
                marks = [int(m) for m in parts[2:2 + num_subjects]]
                # average/grade are recalculated automatically by Student()
                # from marks, so we only need to restore created_on:
                created_on = parts[2 + num_subjects + 2]

                student = Student(name, roll_no, marks)
                student.created_on = created_on
                students.append(student)
        print(f'Data read from {filename} file successfully.')
    except FileNotFoundError:
        print(f"Create a file named {filename} first")
    except Exception as e:
        print(f"Error occurred while reading from file: {e}")

    return students