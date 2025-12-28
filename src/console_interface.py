"""
ConsoleInterface class to manage user interaction and menu display.
"""
from typing import Optional
from .task_manager import TaskManager


class ConsoleInterface:
    """
    Manages user interaction and menu display for the todo application.
    """

    def __init__(self, task_manager: TaskManager):
        """
        Initialize the ConsoleInterface with a TaskManager instance.

        Args:
            task_manager (TaskManager): The TaskManager instance to interact with
        """
        self.task_manager = task_manager

    def display_tasks(self):
        """
        Display all tasks in the console with their ID, title, description, and completion status.
        """
        try:
            tasks = self.task_manager.get_all_tasks()

            if not tasks:
                print("\n📋 No tasks found. Add a task to get started!")
                return

            print("\n📋 YOUR TASKS:")
            print("=" * 60)
            for i, task in enumerate(tasks, 1):
                status_icon = "✅" if task.completed else "⏳"
                status_text = "Completed" if task.completed else "Pending"
                print(f"{i:2d}. [{status_icon} {status_text}] ID: {task.id}")
                print(f"    Title: {task.title}")
                if task.description:
                    print(f"    Description: {task.description}")
                print("-" * 60)
            print(f"Total tasks: {len(tasks)}")
        except Exception as e:
            print(f"❌ An error occurred while displaying tasks: {e}")

    def add_task(self):
        """
        Prompt user for task details and add a new task.
        """
        print("\n➕ ADD A NEW TASK:")
        print("-" * 30)
        title = input("Enter task title: ").strip()

        if not title:
            print("❌ Error: Task title cannot be empty!")
            return

        description = input("Enter task description (optional): ").strip()
        try:
            new_task = self.task_manager.add_task(title, description)
            print(f"✅ Task '{new_task.title}' added successfully with ID {new_task.id}")
        except ValueError as e:
            print(f"❌ Error adding task: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred while adding task: {e}")

    def get_task_id_from_user(self, action: str) -> Optional[int]:
        """
        Prompt user for a task ID and validate it.

        Args:
            action (str): The action being performed (e.g., "update", "delete")

        Returns:
            Optional[int]: The task ID if valid, None otherwise
        """
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            try:
                user_input = input(f"Enter task ID to {action}: ").strip()

                if not user_input:
                    print("Error: Task ID cannot be empty!")
                    attempts += 1
                    continue

                task_id = int(user_input)
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer!")
                    attempts += 1
                    continue

                return task_id
            except ValueError:
                print("Error: Please enter a valid integer for task ID!")
                attempts += 1
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                attempts += 1

        print(f"Failed to get valid task ID after {max_attempts} attempts.")
        return None

    def update_task(self):
        """
        Prompt user for task ID and new details to update an existing task.
        """
        print("\n✏️  UPDATE A TASK:")
        print("-" * 30)
        task_id = self.get_task_id_from_user("update")
        if task_id is None:
            return

        # Check if task exists
        task = self.task_manager.find_task_by_id(task_id)
        if task is None:
            print(f"❌ Error: Task with ID {task_id} not found!")
            return

        print(f"Current task: {task.title}")
        new_title = input(f"Enter new title (or press Enter to keep '{task.title}'): ").strip()

        if new_title == "":
            new_title = None  # Use None to indicate no change
        elif not new_title:  # Empty string after strip
            print("❌ Error: Task title cannot be empty!")
            return

        current_description = task.description if task.description else ""
        new_description = input(f"Enter new description (or press Enter to keep '{current_description}'): ").strip()

        if new_description == "":
            new_description = None  # Use None to indicate no change

        success = self.task_manager.update_task(task_id, new_title, new_description)
        if success:
            print(f"✅ Task {task_id} updated successfully!")
        else:
            print(f"❌ Error: Failed to update task {task_id}")

    def delete_task(self):
        """
        Prompt user for task ID and delete the task.
        """
        print("\n🗑️  DELETE A TASK:")
        print("-" * 30)
        task_id = self.get_task_id_from_user("delete")
        if task_id is None:
            return

        success = self.task_manager.delete_task(task_id)
        if success:
            print(f"✅ Task {task_id} deleted successfully!")
        else:
            print(f"❌ Error: Task with ID {task_id} not found!")

    def mark_task_complete(self):
        """
        Prompt user for task ID and mark the task as complete or incomplete.
        """
        print("\n✅ MARK TASK COMPLETE/INCOMPLETE:")
        print("-" * 40)
        task_id = self.get_task_id_from_user("mark")
        if task_id is None:
            return

        # Check if task exists
        task = self.task_manager.find_task_by_id(task_id)
        if task is None:
            print(f"❌ Error: Task with ID {task_id} not found!")
            return

        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            try:
                status_input = input("Enter 1 for complete, 0 for incomplete: ").strip()
                if not status_input:
                    print("❌ Error: Input cannot be empty!")
                    attempts += 1
                    continue

                if status_input == "1":
                    completed = True
                    break
                elif status_input == "0":
                    completed = False
                    break
                else:
                    print("❌ Error: Please enter 1 for complete or 0 for incomplete!")
                    attempts += 1
                    continue
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                attempts += 1

        if attempts >= max_attempts:
            print(f"❌ Failed to get valid status after {max_attempts} attempts.")
            return

        try:
            success = self.task_manager.mark_task_complete(task_id, completed)
            if success:
                status = "completed" if completed else "incomplete"
                print(f"✅ Task {task_id} marked as {status} successfully!")
            else:
                print(f"❌ Error: Failed to update task {task_id}")
        except Exception as e:
            print(f"❌ An error occurred while marking task complete: {e}")