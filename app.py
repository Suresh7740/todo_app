class LoginSystem:
    def __init__(self):
        # Hardcoded usernames and passwords
        self.users = {
            "admin": "password123",
            "user1": "mypassword",
            "guest": "guest123"
        }

    def login(self):
        print("Welcome to the Login Page!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.users and self.users[username] == password:
            print(f"Login successful! Welcome, {username}.")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False


class TodoApp:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)
        print(f"Task '{task}' added.")

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

    def run(self):
        while True:
            print("\nTodo App Menu:")
            print("1. Add task")
            print("2. Show tasks")
            print("3. Remove task")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                task = input("Enter task description: ")
                self.add_task(task)
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                try:
                    task_num = int(input("Enter task number to remove: "))
                    self.remove_task(task_num)
                except ValueError:
                    print("Please enter a valid task number.")
            elif choice == "4":
                print("Exiting app.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    # Create an instance of the LoginSystem
    login_system = LoginSystem()

    # Require login before accessing the To-Do App
    while True:
        success = login_system.login()
        if success:
            break

    # Launch the To-Do App after successful login
    todo_app = TodoApp()
    todo_app.run()
