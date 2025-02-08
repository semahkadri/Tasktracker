import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description):
    tasks = load_tasks()
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']} - {task['description']}")

def mark_complete(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTask Tracker")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                index = int(input("Enter task number to complete: "))
                mark_complete(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
