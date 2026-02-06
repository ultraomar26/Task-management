print("📊 Welcome to your traking system 📊")

class task:
    def __init__(self, task_name, status):
        self.task = task_name
        self.status = status

    def __str__(self):
        return f"Task: {self.task} | Status: {self.status}"

tasks = []

def add_task():
    task_name = input("Enter the task name: ")
    task_status = input("Enter the task status: ")
    new_task = task(task_name, task_status)
    tasks.append(new_task)
    print("Task added successfully")

def remove_task():
    task_name = input("Enter the task to remove: ")
    for t in tasks:
        if t.task == task_name:
            tasks.remove(t)
            print(f"Task -{task_name}- removed successfully")
            return
    print(f"Task -{task_name}- not found")

def view_tasks():
    print("\nTasks:")
    for t in tasks:
        print(t)

def status_task():
    task_name = input("Enter the name of the task to update: ")
    for t in tasks:
        if t.task == task_name:
            new_status = input(f"Enter new status for '{task_name}': ")
            t.status = new_status
            print("Status updated successfully")
            return
    print(f"Task -{task_name}- not found")

def main():
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Update status of task")
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