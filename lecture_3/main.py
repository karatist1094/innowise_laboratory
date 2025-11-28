"""
Student Grade Analyzer Program

This program manages student grades and provides analysis features including:
- Adding students and grades
- Generating reports with statistics
- Finding top performers

Student data structure:
{
    "name": "student_name",
    "grades": []  # empty list to be filled later
}
"""
students = [] # Initialize an empty list to store student data


def info() -> None:
    """
    Display the main menu of the Student Grade Analyzer program.

    Shows all available options to the user:
    - Add new student
    - Add grades for existing student
    - Generate comprehensive report
    - Find top performing student
    - Exit the application

    The menu is formatted with clear section headers and separators
    for better readability and user experience.
    """
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")
    print("-" * 35)


def add_student() -> None:
    """
    Add a new student to the system.

    Prompts the user to enter a student name and checks if a student
    with that name already exists in the database. If the name is unique,
    creates a new student record with an empty grades list. If the name
    already exists, displays an error message.

    Student data structure:
    {
        "name": "student_name",
        "grades": []  # empty list to be filled later
    }

    Returns:
        None
    """
    name: str = input("Please enter student's name: ").strip()
    exists: bool = False

    # Check if student already exists
    for student in students:
        if student["name"] == name:
            exists = True
            break

    # Add new student or show error
    if not exists:
        students.append({"name": name, "grades": []})
        print(f"Student '{name}' added successfully!")
    else:
        print("Student with that name already exists")


def add_grades() -> None:
    """
    Add grades for an existing student.

    Prompts the user to enter a student name, searches for the student,
    and if found, allows adding multiple grades. Grades must be integers
    between 0 and 100. User can type 'done' to finish grade entry.

    Handles:
    - Student not found
    - Invalid grade values
    - Grade range validation
    """
    student_name: str = input("Please enter student's name: ").strip()
    student_exists: bool = False

    for student in students:
        if student["name"] == student_name:
            student_exists = True
            print(
                f"Student '{student_name}' found. "
                f"Enter grades (0-100). Type 'done' to finish."
            )

            while True:
                grade_input: str = input("Please enter grade: ").strip()

                if grade_input.lower() == "done":
                    print("Grade entry completed.")
                    break

                try:
                    grade: int = int(grade_input)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                        print(f"Grade {grade} added successfully!")
                    else:
                        print("Grade must be between 0 and 100. Try again.")
                except ValueError:
                    print("Invalid grade. Try again.")
            break

    if not student_exists:
        print("Student with that name doesn't exist")


def show_report() -> None:
    """
    Generate and display a comprehensive report of all students.

    Shows each student's average grade and calculates overall statistics
    including maximum, minimum, and overall average grades.

    Handles:
    - Students with no grades (shows N/A)
    - Empty student list
    - Division by zero for students without grades
    """
    print("\n--- Student Report ---")

    students_with_grades = [student for student in students if student["grades"]]
    if not students_with_grades:
        print("No students with grades available.")
        return

    averages: list[float] = []

    for student in students:
        try:
            average_grade: float = sum(student["grades"]) / len(student["grades"])
            averages.append(average_grade)
            print(f"{student['name']}'s average grade is {average_grade:.1f}.")
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")

    print("---")
    print(f"Max Average: {max(averages):.1f}")
    print(f"Min Average: {min(averages):.1f}")
    print(f"Overall Average: {sum(averages) / len(averages):.1f}")


def find_top_performer() -> None:
    """
    Find and display the student with the highest average grade.

    Filters students with grades, calculates averages, and identifies
    the top performer. Handles cases where no students have grades
    or unexpected errors occur during calculation.

    Uses max() with lambda function to compare student averages.
    """
    students_with_grades = [student for student in students if student["grades"]]

    if not students_with_grades:
        print("No students with grades available.")
        return

    try:
        top_student = max(
            students_with_grades,
            key=lambda student: sum(student["grades"]) / len(student["grades"])
        )

        average_grade = sum(top_student["grades"]) / len(top_student["grades"])
        print(f"Top performer: {top_student['name']} with average grade: {average_grade:.1f}")

    except Exception as error:
        print(f"Error finding top performer: {error}")


def main_menu() -> None:
    """
    Display and handle the main program menu in an infinite loop.

    Continuously shows the menu, processes user input, and calls
    appropriate functions based on the user's choice. Handles
    invalid input and provides user-friendly error messages.

    The loop exits only when the user selects the exit option (5).
    """
    while True:
        info()
        try:
            choice: int = int(input("Enter your choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                add_grades()
            elif choice == 3:
                show_report()
            elif choice == 4:
                find_top_performer()
            elif choice == 5:
                print("Thank you for using Student Grade Analyzer. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("You typed an invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
