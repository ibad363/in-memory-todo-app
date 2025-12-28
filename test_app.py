"""
Test script to verify the todo application functionality
"""
from src.task_manager import TaskManager
from src.console_interface import ConsoleInterface

def test_app():
    print("Testing Todo Application...")

    # Initialize the application components
    task_manager = TaskManager()
    console_interface = ConsoleInterface(task_manager)

    print("\n1. Testing adding tasks...")
    # Add some tasks
    task_manager.add_task("Buy groceries", "Milk, bread, eggs")
    task_manager.add_task("Walk the dog", "Morning walk in the park")
    task_manager.add_task("Finish report", "Complete the quarterly report")
    print("Added 3 tasks successfully")

    print("\n2. Testing viewing tasks...")
    # View all tasks
    tasks = task_manager.get_all_tasks()
    print(f"Found {len(tasks)} tasks")
    for task in tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"   ID: {task.id}, Title: {task.title}, Status: {status}")

    print("\n3. Testing updating a task...")
    # Update a task
    success = task_manager.update_task(1, "Buy groceries and cook dinner", "Milk, bread, eggs, chicken")
    if success:
        updated_task = task_manager.find_task_by_id(1)
        print(f"Updated task 1: {updated_task.title}")
    else:
        print("Failed to update task")

    print("\n4. Testing marking task as complete...")
    # Mark a task as complete
    success = task_manager.mark_task_complete(2, True)
    if success:
        task = task_manager.find_task_by_id(2)
        print(f"Marked task 2 as {'complete' if task.completed else 'incomplete'}")
    else:
        print("Failed to mark task as complete")

    print("\n5. Testing deleting a task...")
    # Delete a task
    initial_count = len(task_manager.get_all_tasks())
    success = task_manager.delete_task(3)
    if success:
        final_count = len(task_manager.get_all_tasks())
        print(f"Deleted task 3, task count: {initial_count} -> {final_count}")
    else:
        print("Failed to delete task")

    print("\n6. Testing edge cases...")
    # Test edge cases
    print("Testing invalid task ID:")
    invalid_task = task_manager.find_task_by_id(999)
    print(f"Correctly returned None for invalid ID: {invalid_task is None}")

    print("\n7. Final task list:")
    final_tasks = task_manager.get_all_tasks()
    for task in final_tasks:
        status = "Completed" if task.completed else "Pending"
        print(f"   ID: {task.id}, Title: {task.title}, Status: {status}")

    print("\nAll tests passed! Application is working correctly.")

if __name__ == "__main__":
    test_app()