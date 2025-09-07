# todo_list.py
import json

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add multiple tasks
def add_tasks():
    tasks = load_tasks()
    print("Enter tasks (press Enter without typing to stop):")
    while True:
        task = input("Task: ")
        if task.strip() == "":
            break
        tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully!")
    save_tasks(tasks)

# List tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

# Mark task as done
def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[index]['task']}' marked as done!")
    else:
        print("Invalid task number!")

# Delete task
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed['task']}' deleted!")
    else:
        print("Invalid task number!")

# Main Menu
while True:
    print("\n--- To-Do List App ---")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_tasks()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        index = int(input("Enter task number to mark done: ")) - 1
        mark_done(index)
    elif choice == "4":
        list_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    elif choice == "5":
        break
    else:
        print("Invalid choice, try again!")
