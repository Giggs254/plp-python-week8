
# ==========================================
# PERSONAL MINI-TOOLKIT
# PLP WEEK 8 FINAL PROJECT
# ==========================================



# Simple Calculator
def calculator():
    """Perform basic mathematical operations."""

    print("\n========== SIMPLE CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Choose an operation (1-4): ")

    if operation not in ["1", "2", "3", "4"]:
        print("Invalid operation selected.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "1":
            result = num1 + num2
            print("Result:", result)

        elif operation == "2":
            result = num1 - num2
            print("Result:", result)

        elif operation == "3":
            result = num1 * num2
            print("Result:", result)

        elif operation == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")


# To-Do List Manager
def todo_manager():
    """Manage a list of user tasks."""

    tasks = []

    while True:
        print("\n========== TO-DO LIST MANAGER ==========")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Return to main menu")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            task = input("Enter your task: ")

            if task.strip():
                tasks.append(task)
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            print("\nYOUR TASKS:")

            if len(tasks) == 0:
                print("No tasks have been added yet.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please select 1, 2 or 3.")


# Grade Checker
def grade_checker():
    """Check a student's grade based on marks."""

    print("\n========== GRADE CHECKER ==========")

    try:
        marks = float(input("Enter your marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")

        elif marks >= 80:
            grade = "A"
            print("Grade:", grade)
            print("Excellent performance!")

        elif marks >= 70:
            grade = "B"
            print("Grade:", grade)
            print("Very good performance!")

        elif marks >= 60:
            grade = "C"
            print("Grade:", grade)
            print("Good performance!")

        elif marks >= 50:
            grade = "D"
            print("Grade:", grade)
            print("Fair performance.")

        else:
            grade = "E"
            print("Grade:", grade)
            print("You need to improve.")

    except ValueError:
        print("Invalid input. Please enter numerical marks.")


# Notes Manager
def notes_manager():
    """Allow users to save and view notes."""

    notes = []

    while True:
        print("\n========== NOTES MANAGER ==========")
        print("1. Add a note")
        print("2. View notes")
        print("3. Return to main menu")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            note = input("Enter your note: ")

            if note.strip():
                notes.append(note)
                print("Note saved successfully!")
            else:
                print("Note cannot be empty.")

        elif choice == "2":
            print("\nYOUR SAVED NOTES:")

            if len(notes) == 0:
                print("No notes saved yet.")
            else:
                for index, note in enumerate(notes, start=1):
                    print(f"{index}. {note}")

        elif choice == "3":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please select 1, 2 or 3.")

def display_menu():
    """Display the main menu of the toolkit."""
    print("\n================================")
    print("       PERSONAL MINI-TOOLKIT")
    print("================================")
    print("1. Simple Calculator")
    print("2. To-Do List Manager")
    print("3. Grade Checker")
    print("4. Notes Manager")
    print("5. Exit")
    print("================================")



# Main program loop
while True:
    display_menu()

    choice = input("Select a tool (1-5): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_manager()

    elif choice == "3":
        grade_checker()

    elif choice == "4":
        notes_manager()

    elif choice == "5":
        print("\nThank you for using Personal Mini-Toolkit!")
        break

    else:
        print("\nInvalid choice. Please select between 1 and 5.")



