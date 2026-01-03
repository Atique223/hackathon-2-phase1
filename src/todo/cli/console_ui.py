"""
Console user interface for the Todo application.
"""

from typing import Optional
from src.todo.services.todo_service import TodoService


class ConsoleUI:
    """
    Console-based user interface for the Todo application.
    Handles user input and displays output.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the console UI with a todo service.

        Args:
            todo_service: The TodoService instance to use
        """
        self.todo_service = todo_service

    def display_todos(self):
        """Display all todos in a formatted list."""
        todos = self.todo_service.get_all_todos()
        if not todos:
            print("No todos found.")
            return

        for todo in todos:
            print(todo)

    def add_todo(self, title: str) -> bool:
        """
        Add a new todo.

        Args:
            title: The title of the todo to add

        Returns:
            True if the todo was added successfully, False otherwise
        """
        try:
            todo = self.todo_service.add_todo(title)
            print(f"Added todo #{todo.id}: {todo.title}")
            return True
        except ValueError as e:
            print(f"Error adding todo: {e}")
            return False

    def update_todo(self, todo_id: int, new_title: str) -> bool:
        """
        Update a todo's title.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            True if the todo was updated successfully, False otherwise
        """
        try:
            if self.todo_service.validate_todo_id(todo_id):
                success = self.todo_service.update_todo(todo_id, new_title)
                if success:
                    print(f"Updated todo #{todo_id}")
                    return True
                else:
                    print(f"Todo #{todo_id} not found")
                    return False
            else:
                print(f"Todo #{todo_id} not found")
                return False
        except ValueError as e:
            print(f"Error updating todo: {e}")
            return False

    def complete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            True if the todo was marked complete successfully, False otherwise
        """
        if self.todo_service.validate_todo_id(todo_id):
            success = self.todo_service.mark_complete(todo_id)
            if success:
                print(f"Marked todo #{todo_id} as complete")
                return True
            else:
                print(f"Todo #{todo_id} not found")
                return False
        else:
            print(f"Todo #{todo_id} not found")
            return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted successfully, False otherwise
        """
        if self.todo_service.validate_todo_id(todo_id):
            success = self.todo_service.delete_todo(todo_id)
            if success:
                print(f"Deleted todo #{todo_id}")
                return True
            else:
                print(f"Todo #{todo_id} not found")
                return False
        else:
            print(f"Todo #{todo_id} not found")
            return False

    def show_help(self):
        """Display help information with available commands."""
        print("Available commands:")
        print("  add \"todo description\" - Add a new todo")
        print("  list or view - Show all todos")
        print("  update <id> \"new description\" - Update a todo")
        print("  complete <id> or done <id> - Mark a todo as complete")
        print("  delete <id> - Delete a todo")
        print("  help - Show this help message")
        print("  quit or exit - Exit the application")

    def parse_command(self, user_input: str) -> tuple:
        """
        Parse user input into command and arguments.

        Args:
            user_input: The raw user input string

        Returns:
            A tuple containing (command, args) where command is the command string
            and args is a list of arguments
        """
        if not user_input.strip():
            return None, []

        # More robust parsing that handles quoted strings properly
        import re
        # This regex splits on spaces but keeps quoted strings together
        pattern = r'(?:")([^"]*)(?:")|(?:\')([^\']*)(?:\')|(\S+)'
        matches = re.findall(pattern, user_input.strip())

        # Each match is a tuple of (double_quoted, single_quoted, unquoted)
        parts = [match[0] or match[1] or match[2] for match in matches]

        if not parts:
            return None, []

        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        return command, args