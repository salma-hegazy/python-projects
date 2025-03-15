import json
TASKS_FILE = "tasks.json"
tasks=[]
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def view_tasks():
    if not tasks:
        print(" No tasks available.")
    else:
        print("\n To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

def complete_task(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f" Task marked as completed: {tasks[index - 1]['task']}")
    else:
        print(" Invalid task number.")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task deleted: {removed_task['task']}")
    else:
        print(" Invalid task number.")
def edit_task(index):
    if 0 < index <= len(tasks):
        new_task = input(f"Enter new description for '{tasks[index - 1]['task']}': ")
        tasks[index - 1]['task'] = new_task  # Update task description
        save_tasks(tasks)  # Save changes
        print(f" Task updated: {new_task}")
    else:
        print("Invalid task number.")

tasks = load_tasks()

while True:
    print("\nOptions: [1] Add Task  [2] View Tasks  [3] Complete Task  [4] Delete Task  [5] Exit  [6] Edit task ")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter task number to complete: "))
        complete_task(index)
    elif choice == "4":
        view_tasks()
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "5":
        print(" Exiting... Your tasks are saved!")
        break
    elif choice == "6":
        view_tasks()
        index = int(input("Enter task number to edit: "))
        edit_task(index)

    else:
        print(" Invalid choice, try again.")