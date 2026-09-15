# OOP -> To Manage Student Data
from datetime import datetime

SUBJECTS = ('English', 'Maths', 'Computer', 'Physics')


class Student:
    total_students = 0

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks
        self.average = self.__calculate_average()
        self.grade = self.__calculate_grade()
        self.created_on = datetime.now().strftime('%d/%m/%Y')
        Student.total_students += 1

    def __calculate_average(self):
        return round(sum(self.__marks) / len(self.__marks))

    def __calculate_grade(self):
        avg = self.average
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 65:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    def get_marks(self):
        return self.__marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Average: {self.average}")
        print(f"Grade: {self.grade}")
        print(f"Created On: {self.created_on}")

    def to_csv(self):
        marks_str = ','.join(str(m) for m in self.__marks)
       
        return f"{self.name},{self.roll_no},{marks_str},{self.average},{self.grade},{self.created_on}\n"