
# CodeOrbit Tech - Python Programming Internship
# Task 2: To-Do List CLI Application

import os

# File used to save tasks
FILE_NAME = "tasks.txt"


# Load tasks from the text file
def load_tasks():
    tasks = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    task = line.strip()
                    if task:
                        tasks.append(task)

        except OSError:
            print("Error: Unable to load saved tasks.")

    return tasks


# Save tasks to the text file
def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")

    except OSError:
        print("Error: Unable to save tasks.")
        return False

    return True


# Add a new task
def add_task(tasks):
    task = input("Enter your task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)

    if save_tasks(tasks):
        print("Task added successfully!")


# Display all tasks
def view_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter the task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)

            if save_tasks(tasks):
                print(f"Task removed successfully: {removed_task}")
            else:
                # Restore the task if saving fails
                tasks.insert(task_number - 1, removed_task)

        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input! Please enter a number.")


# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n================================")
        print("        TO-DO LIST APP")
        print("================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


# Start the application
if __name__ == "__main__":
    main()
