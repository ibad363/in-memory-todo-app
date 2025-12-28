"""
Main application file for the Todo In-Memory Python Console App.
"""
from .task_manager import TaskManager
from .console_interface import ConsoleInterface


def main():
    """
    Main function to run the Todo application.
    """
    print("Welcome to the Todo In-Memory Python Console App!")
    print("Manage your tasks efficiently in memory.")

    try:
        task_manager = TaskManager()
        console_interface = ConsoleInterface(task_manager)
    except Exception as e:
        print(f"Failed to initialize the application: {e}")
        return

    while True:
        print("\n" + "="*50)
        print("TODO APP MENU")
        print("="*50)
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task complete/incomplete")
        print("6. Exit")
        print("-"*50)

        try:
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                console_interface.add_task()
            elif choice == "2":
                console_interface.display_tasks()
            elif choice == "3":
                console_interface.update_task()
            elif choice == "4":
                console_interface.delete_task()
            elif choice == "5":
                console_interface.mark_task_complete()
            elif choice == "6":
                print("Thank you for using the Todo App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nInput ended unexpectedly. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()