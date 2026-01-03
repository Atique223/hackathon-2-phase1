"""
Todo model representing a single todo item.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with an ID, title, and completion status.

    Attributes:
        id (int): Unique identifier for the todo item
        title (str): The content/description of the todo item
        completed (bool): Status indicating whether the todo is completed (True) or active (False)
    """

    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")

        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Title must be a non-empty string")

        if not isinstance(self.completed, bool):
            raise ValueError("Completed must be a boolean value")

    def mark_complete(self):
        """Mark the todo as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the todo as incomplete."""
        self.completed = False

    def update_title(self, new_title: str):
        """Update the title of the todo."""
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Title must be a non-empty string")
        self.title = new_title.strip()

    def __str__(self) -> str:
        """String representation of the todo."""
        status = "x" if self.completed else " "
        return f"{self.id}. [{status}] {self.title}"

    def __repr__(self) -> str:
        """Developer-friendly representation of the todo."""
        return f"Todo(id={self.id}, title='{self.title}', completed={self.completed})"