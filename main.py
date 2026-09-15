# Entry point of the program

from student import Student, SUBJECTS
from file_handler import add_students, load_students
from analytics import show_all_students, show_summary, show_top_students, show_failing, search_student

students = load_students()


def add_student():
    try:
        name = input("Enter Student name : ").strip()
        roll_no = input("Enter Student Roll Number : ").strip()
        if not name or not roll_no:
            raise ValueError("Name and Roll Number cannot be empty.")
        for s in students:
            if s.roll_no == roll_no:
                raise ValueError("Roll Number already exists. Please enter a unique Roll Number.")
        marks = []
        for subject in SUBJECTS:
          
            mark = int(input(f'Enter marks for {subject} Marks is between 0-100: ').strip())
            if not 0 <= mark <= 100:
                raise ValueError("Marks must be between 0 and 100.")
            marks.append(mark)
        s = Student(name, roll_no, marks)
        students.append(s)
        print(f"Student {name} added successfully.")
    except ValueError as e:
        print(f"Invalid input. {e}")


def display_students():
    if not students:
        print("No student added yet. Please add students first.")
        return
    print(f"Total Students: {Student.total_students}")
    for s in students:
        s.display()
        print('-------------------')


def main():
    print('=' * 27)
    print('Student Management System')
    print('=' * 27)
    while True:
        try:
            print("\n1. Add Student")
            print("2. View All Students (memory)")
            print("3. Analytics - View Full Table")
            print("4. Analytics - Class Summary")
            print("5. Analytics - Top 3 Students")
            print("6. Analytics - Failing Students")
            print("7. Analytics - Search Student")
            print("8. Save & Exit")

            choice = int(input("\nEnter choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                display_students()
            elif choice == 3:
                show_all_students()
            elif choice == 4:
                show_summary()
            elif choice == 5:
                show_top_students()
            elif choice == 6:
                show_failing()
            elif choice == 7:
                search_student()
            elif choice == 8:
                add_students(students)
                print("Goodbye!")
                break
            else:
              
                print("Invalid choice. Enter 1 to 8.")

        except ValueError:
            print("Please enter a valid number.")


main()