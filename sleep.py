class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print(f"Task '{title}' created.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.completed = True
            print(f"Task '{task.title}' marked as completed.")
        else:
            print("Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("Tasks:")
        for index, task in enumerate(self.tasks):
            status = "✔️" if task.completed else "❌"
            print(f"{index+1}. [{status}] {task.title}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Create Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.create_task(title, description)
        elif choice == '2':
            task_manager.show_tasks()
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            task_manager.complete_task(task_index)
        elif choice == '3':
            task_manager.show_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
