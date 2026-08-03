// =============================================================================
// PROGRAMMING FUNDAMENTALS — Assignment 7
// =============================================================================
//
// TASK: Console-Based To-Do List Application
//
// Build a simple to-do list program that runs entirely in the console and
// allows the user to manage their tasks interactively using a menu.
//
// -----------------------------------------------------------------------------
// FEATURES YOUR PROGRAM MUST SUPPORT
// -----------------------------------------------------------------------------
//
//   1. Add a Task
//      - Prompt the user to type a task description.
//      - Add it to the list and confirm it was added.
//
//   2. View All Tasks
//      - Display all tasks currently in the list, numbered from 1.
//      - If the list is empty, print a friendly message saying so.
//
//   3. Delete a Task
//      - Show the list of tasks with their numbers.
//      - Ask the user which task number they want to remove.
//      - Remove the task and confirm the deletion.
//      - If the task number is invalid, print an error message.
//
//   4. Quit
//      - End the program with a farewell message.
//
// -----------------------------------------------------------------------------
// HOW THE MENU SHOULD LOOK
// -----------------------------------------------------------------------------
//
//   ============================
//        TO-DO LIST MENU
//   ============================
//   1. Add task
//   2. View tasks
//   3. Delete task
//   4. Quit
//   Enter your choice (1-4):
//
// -----------------------------------------------------------------------------
// EXPECTED INTERACTION EXAMPLE
// -----------------------------------------------------------------------------
//
//   Enter your choice (1-4): 1
//   Enter task: Buy groceries
//   Task added: "Buy groceries"
//
//   Enter your choice (1-4): 2
//   Your Tasks:
//   1. Buy groceries
//   2. Study for exams
//
//   Enter your choice (1-4): 3
//   Enter task number to delete: 1
//   Task "Buy groceries" has been removed.
//
//   Enter your choice (1-4): 4
//   Goodbye!
//
// -----------------------------------------------------------------------------
// REQUIREMENTS
// -----------------------------------------------------------------------------
// - Store tasks in a vector<string> (a dynamic list of text).
// - Use a loop to keep the menu running until the user chooses to quit.
// - Each feature MUST be implemented in its own function (see scaffold below).
// - Handle invalid menu choices gracefully (print an error, do not crash).
//

//
// =============================================================================
// YOUR CODE BELOW — remove the // symbols from the scaffold and fill it in
// =============================================================================

//                      SOLUTION
#include <iostream>
#include <vector>
#include <string>

// Display the main menu to the user
void displayMenu() {
    std::cout << "=================================\n";
    std::cout << "        TO-DO LIST MENU          \n";
    std::cout << "=================================\n";
    std::cout << "1. Add task\n";
    std::cout << "2. View tasks\n";
    std::cout << "3. Delete task\n";
    std::cout << "4. Quit\n";
}

// 1: Add a task
void addTask(std::vector<std::string>& tasks) {
    std::cout << "Enter task: ";
    std::string taskDescription;
    std::getline(std::cin >> std::ws, taskDescription); 

    tasks.push_back(taskDescription);
    std::cout << "Task added: \"" << taskDescription << "\"\n";
}

// 2: View all current task
void viewTasks(const std::vector<std::string>& tasks) {
    if (tasks.empty()) {
        std::cout << "Your list is currently empty! You can add one if you have to.\n";
        return;
    }

    std::cout << "Your Tasks:\n";
    for (size_t i = 0; i < tasks.size(); ++i) {
        std::cout << (i + 1) << ". " << tasks[i] << "\n";
    }
}

// 3: Delete a task
void deleteTask(std::vector<std::string>& tasks) {
    if (tasks.empty()) {
        std::cout << "No tasks available to delete. Lucky you!\n";
        return;
    }

    std::cout << "Enter task number to delete: ";
    int taskNumber;
    
    if (!(std::cin >> taskNumber)) {
        std::cin.clear();
        std::cin.ignore(10000, '\n'); 
        std::cout << "Invalid input! Please enter a valid number.\n";
        return;
    }


    if (taskNumber >= 1 && static_cast<size_t>(taskNumber) <= tasks.size()) {
        std::string removedTask = tasks[taskNumber - 1];
        tasks.erase(tasks.begin() + (taskNumber - 1));
        std::cout << "Task \"" << removedTask << "\" has been removed.\n";
    } else {
        std::cout << "Error: Invalid task number.\n";
    }
}

int main() {
    std::vector<std::string> tasks; 
    int choice = 0;

    displayMenu();


    while (choice != 4) {
        std::cout << "\nEnter your choice (1-4): ";
        
        if (!(std::cin >> choice)) {
            std::cin.clear();
            std::cin.ignore(10000, '\n'); 
            std::cout << "Invalid choice! Please enter a number between 1 and 4.\n";
            continue;
        }

        switch (choice) {
            case 1:
                addTask(tasks);
                break;
            case 2:
                viewTasks(tasks);
                break;
            case 3:
                deleteTask(tasks);
                break;
            case 4:
                std::cout << "Goodbye! See ya later!\n";
                break;
            default:
                std::cout << "Invalid option! Please enter a number from 1 to 4.\n";
                break;
        }
    }

    return 0;
}
