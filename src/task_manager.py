"""
TaskManager class to manage collection of tasks in memory.
"""
from typing import List, Optional
from .task import Task


class TaskManager:
    """
    Manages a collection of Task entities stored in memory with operations to add,
    view, update, delete, and mark complete/incomplete.
    """

    def __init__(self):
        """
        Initialize the TaskManager with an empty list of tasks and next ID counter.
        """
        self.tasks: List[Task] = []
        self.next_id = 1

    def get_next_id(self) -> int:
        """
        Get the next available ID and increment the counter.

        Returns:
            int: The next available ID for a new task
        """
        current_id = self.next_id
        self.next_id += 1
        return current_id

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and description.

        Args:
            title (str): Title of the task (required)
            description (str): Description of the task (optional)

        Returns:
            Task: The newly created Task object

        Raises:
            ValueError: If title is empty
        """
        task_id = self.get_next_id()
        new_task = Task(task_id, title, description, completed=False)
        self.tasks.append(new_task)
        return new_task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            List[Task]: List of all Task objects
        """
        return self.tasks.copy()

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id (int): ID of the task to find

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id (int): ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title.strip() if title.strip() else task.title
        if description is not None:
            task.description = description.strip() if description else ""

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int, completed: bool) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id (int): ID of the task to update
            completed (bool): Whether the task should be marked as completed

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        task.completed = completed
        return True