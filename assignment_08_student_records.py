# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


#                        SOLUTION
def main():
    # Dictionary to store student records with their IDs as the key
    students = {}

    while True:
        print("\n" + "=" * 40)
        print(" STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add a Student")
        print("2. Display All Students")
        print("3. Calculate Average Score for a Specific Student")
        print("4. Quit")
        print("=" * 40)

        choice = input("Enter your choice (1-4): ").strip()

        # 1. Add a Student
        if choice == "1":
            name = input("Enter student's full name: ").strip()
            student_id = input("Enter student ID (e.g., 20240001): ").strip()

            if student_id in students:
                print(f"Error: Student ID '{student_id}' already exists!")
                continue

            try:
                num_scores = int(input("How many scores do you want to enter? "))
                if num_scores < 0:
                    print("Number of scores cannot be negative.")
                    continue
            except ValueError:
                print("Error: Please enter a valid whole number.")
                continue

            scores = []
            for i in range(num_scores):
                while True:
                    try:
                        score = float(input(f"  Enter score #{i + 1}: "))
                        scores.append(score)
                        break
                    except ValueError:
                        print("  Invalid input. Please enter a valid number for the score.")

            # Store student record in dictionary
            students[student_id] = {
                "name": name,
                "scores": scores
            }
            print(f"\nSuccess: Student record for '{name}' added successfully!")

        # 2. Display All Students
        elif choice == "2":
            if not students:
                print("\nNo student records found.")
            else:
                print("\n" + "-" * 75)
                print(f"{'ID':<12} | {'Name':<20} | {'Scores':<22} | {'Average':<8}")
                print("-" * 75)

                for s_id, record in students.items():
                    scores_list = record["scores"]
                    scores_str = str(scores_list) if scores_list else "None"
                    avg_score = sum(scores_list) / len(scores_list) if scores_list else 0.0

                    print(f"{s_id:<12} | {record['name']:<20} | {scores_str:<22} | {avg_score:<8.2f}")
                print("-" * 75)

        # 3. Calculate Average Score for a Specific Student
        elif choice == "3":
            if not students:
                print("\nNo student records available.")
                continue

            search_id = input("Enter student ID: ").strip()

            if search_id in students:
                student = students[search_id]
                scores = student["scores"]

                if scores:
                    average = sum(scores) / len(scores)
                    print(f"\nStudent: {student['name']} (ID: {search_id})")
                    print(f"Scores: {scores}")
                    print(f"Average Score: {average:.2f}")
                else:
                    print(f"\nStudent: {student['name']} (ID: {search_id}) has no recorded scores.")
            else:
                print(f"\nError: Student ID '{search_id}' not found.")

        # 4. Quit
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()