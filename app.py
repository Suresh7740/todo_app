# app.py

class TodoApp:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)
        print(f"Task '{task}' added!")

    def show_tasks(self):
        if not self.todos:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(self.todos, 1):
                print(f"{idx}. {task}")

    def remove_task(self, index):
        try:
            removed_task = self.todos.pop(index - 1)
            print(f"Task '{removed_task}' removed!")
        except IndexError:
            print("Invalid task number.")

if __name__ == "__main__":
    app = TodoApp()

    while True:
        print("\nTodo App Menu:")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            app.add_task(task)
        elif choice == "2":
            app.show_tasks()
        elif choice == "3":
            task_num = int(input("Enter task number to remove: "))
            app.remove_task(task_num)
        elif choice == "4":
            print("Exiting app.")
            break
        else:
            print("Invalid choice, please try again.")