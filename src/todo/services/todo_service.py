"""
Service layer for managing Todo operations.
"""

from typing import List, Optional
from src.todo.models.todo import Todo
from src.todo.repositories.todo_repository import TodoRepository


class TodoService:
    """
    Service class for managing Todo operations.
    Acts as an interface between the CLI and the repository.
    """

    def __init__(self, repository: TodoRepository):
        """
        Initialize the service with a repository.

        Args:
            repository: The TodoRepository instance to use
        """
        self.repository = repository

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo.

        Args:
            title: The title/description of the todo

        Returns:
            The created Todo object
        """
        return self.repository.add_todo(title)

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos.

        Returns:
            List of all Todo objects
        """
        return self.repository.get_all_todos()

    def update_todo(self, todo_id: int, new_title: str) -> bool:
        """
        Update a todo's title.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            True if the todo was found and updated, False otherwise
        """
        return self.repository.update_todo(todo_id, new_title)

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            True if the todo was found and marked complete, False otherwise
        """
        return self.repository.mark_complete(todo_id)

    def mark_incomplete(self, todo_id: int) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            True if the todo was found and marked incomplete, False otherwise
        """
        return self.repository.mark_incomplete(todo_id)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        return self.repository.delete_todo(todo_id)

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        return self.repository.get_todo_by_id(todo_id)

    def validate_todo_id(self, todo_id: int) -> bool:
        """
        Validate if a todo with the given ID exists.

        Args:
            todo_id: The ID to validate

        Returns:
            True if a todo with the ID exists, False otherwise
        """
        return self.repository.get_todo_by_id(todo_id) is not None