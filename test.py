print("📊 Welcome to your traking system 📊")

class task:
    def __init__(self , task  , status):
        self.task = task
        self.status = status

tasks = {task()}

def add_task():
    task = task()
    tasks.append(task)
    print("Task added successfully")

def remove_task():
    task = input("enter the task to remove:")
    tasks.remove(task)
    print(f"task -{task}- removed successfully")

def view_tasks():
    print("tasks:")
    for task in tasks:
        print(task)

def status_task():
    status = input("Enter the status of the task: ")
    tasks.append(status)
    print("Status added successfully")

def main():
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. status of task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            status_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()