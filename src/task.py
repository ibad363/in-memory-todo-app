"""
Task class representing a single todo item.
"""
from typing import Optional


class Task:
    """
    Represents a single todo item with id, title, description, and completion status.
    """

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required)
            description (str): Description of the task (optional)
            completed (bool): Completion status of the task (default: False)

        Raises:
            ValueError: If title is empty
            TypeError: If task_id is not an integer
        """
        if not isinstance(task_id, int):
            raise TypeError("Task ID must be an integer")
        if not title or not title.strip():
            raise ValueError("Task title must not be empty")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = bool(completed)

    def __str__(self) -> str:
        """
        String representation of the task for display purposes.

        Returns:
            str: Formatted string representation of the task
        """
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title} - {self.description}"

    def __repr__(self) -> str:
        """
        Developer-friendly representation of the task.

        Returns:
            str: Detailed string representation of the task
        """
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary containing task properties
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }