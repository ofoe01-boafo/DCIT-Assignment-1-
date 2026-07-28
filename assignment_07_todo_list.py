# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


#                    SOLUTION
def main():
    tasks = []

    while True:
        print("\n-- TO-DO LIST MENU --")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()

        # 1. Add a Task
        if choice == "1":
            task_description = input("Enter task description: ").strip()
            if task_description:
                tasks.append(task_description)
                print(f"Task '{task_description}' successfully added!")
            else:
                print("Task description cannot be empty.")

        # 2. View All Tasks
        elif choice == "2":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        # 3. Delete a Task
        elif choice == "3":
            if not tasks:
                print("Your to-do list is empty. Lucky you!.")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    task_num = int(
                        input("\nEnter the task number to delete: ")
                    )
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"The task '{removed_task}' has been deleted successfully.")
                    else:
                        print("Error: Invalid task number.")
                except ValueError:
                    print("Error: Please enter a valid numerical index.")

        # 4. Quit
        elif choice == "4":
            print("Thank you for using the To-Do List app. See ya next time!")
            break

        else:
            print("Invalid selection. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()