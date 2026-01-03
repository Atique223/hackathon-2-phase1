"""
In-memory repository for managing Todo items.
"""

from typing import List, Optional
from src.todo.models.todo import Todo


class TodoRepository:
    """
    In-memory repository for managing Todo items.
    Stores todos in a Python list with sequential ID assignment.
    """

    def __init__(self):
        """Initialize the repository with an empty list and ID counter."""
        self._todos: List[Todo] = []
        self._next_id = 1

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo to the repository.

        Args:
            title: The title/description of the todo

        Returns:
            The created Todo object with assigned ID
        """
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty")

        todo = Todo(id=self._next_id, title=title.strip(), completed=False)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the repository.

        Returns:
            List of all Todo objects
        """
        return self._todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_title: str) -> bool:
        """
        Update the title of an existing todo.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            True if the todo was found and updated, False otherwise
        """
        if not new_title or not new_title.strip():
            raise ValueError("Todo title cannot be empty")

        for todo in self._todos:
            if todo.id == todo_id:
                todo.update_title(new_title)
                return True
        return False

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            True if the todo was found and marked complete, False otherwise
        """
        for todo in self._todos:
            if todo.id == todo_id:
                todo.mark_complete()
                return True
        return False

    def mark_incomplete(self, todo_id: int) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            True if the todo was found and marked incomplete, False otherwise
        """
        for todo in self._todos:
            if todo.id == todo_id:
                todo.mark_incomplete()
                return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        for i, todo in enumerate(self._todos):
            if todo.id == todo_id:
                del self._todos[i]
                return True
        return False