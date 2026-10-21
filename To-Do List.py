#To do List

tasks = []

def show_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task():
    """Remove a task by number."""
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    """Save tasks to a file."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved!")

def load_tasks():
    """Load tasks from a file."""
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded!")
    except FileNotFoundError:
        print("No saved tasks found.")

def main():
    load_tasks()  # Load tasks when the program starts
    while True:
        print("\nOptions: (1) Show Tasks (2) Add Task (3) Remove Task (4) Save (5) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            save_tasks()
        elif choice == "5":
            save_tasks()
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
