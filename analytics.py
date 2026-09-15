# Pandas: Read CSV and Display analytics reports

import pandas as pd



FILENAME = 'students.csv'


def load_dataframe():
    try:
        df = pd.read_csv(FILENAME)
        return df
    except FileNotFoundError:
        print(f"File {FILENAME} not found. Please ensure the file exists.")
        return None


def show_all_students():
    df = load_dataframe()
    if df is None:
        return
    print("ALL Students")
    print(df.to_string(index=False))


def show_summary():
    df = load_dataframe()
    if df is None:
        return
    print("\nAnalytics Report:")
    print(f"Total Students: {len(df)}")
    print(f"Average Marks: {df['Average'].mean():.2f}")
    print(f"Highest Marks: {df['Average'].max():.2f}")
    print(f"Lowest Marks: {df['Average'].min():.2f}")
    print("Grade Distribution:")
    print(df['Grade'].value_counts().to_string())


def show_top_students():
    df = load_dataframe()
    if df is None:
        return
    top3 = df.sort_values("Average", ascending=False).head(3)
    print("\nTop 3 Students:")
    # BUG WAS HERE: original used "Roll no" (lowercase "no"), but the
    # actual CSV column (once file_handler.py is fixed) is "Roll No".
    # Pandas KeyError otherwise. Fixed: matched the real column name.
    print(top3[["Name", "Roll No", "Average", "Grade"]].to_string(index=False))


def show_failing():
    df = load_dataframe()
    if df is None:
        return
    failing = df[df['Grade'] == 'F']
    if failing.empty:
        print("\nNo failing students found. Well done! Class")
       
        return
    print("\nFailing Students:")
    print(failing[["Name", "Roll No", "Average", "Grade"]].to_string(index=False))


def search_student():
    try:
        df = load_dataframe()
        if df is None:
            return
        roll_no = input("Enter Roll Number to search: ").strip()
       
        student = df[df['Roll No'] == roll_no]
        if student.empty:
            print(f"No student found with Roll Number: {roll_no}")
           
            return
        print("--Student found--")
        print(student.to_string(index=False))
    except Exception as e:
        print(f"An error occurred while searching for the student: {e}")