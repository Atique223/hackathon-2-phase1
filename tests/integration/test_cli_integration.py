"""
Integration tests for the CLI interface and full application flow.
"""

from unittest.mock import Mock, patch
import sys
from io import StringIO
from src.todo.repositories.todo_repository import TodoRepository
from src.todo.services.todo_service import TodoService
from src.todo.cli.console_ui import ConsoleUI


def test_add_and_list_todos():
    """Test adding a todo and then listing todos."""
    repo = TodoRepository()
    service = TodoService(repo)
    ui = ConsoleUI(service)

    # Add a todo
    result = ui.add_todo("Test todo")
    assert result is True

    # Capture the output when displaying todos
    captured_output = StringIO()
    import sys
    original_stdout = sys.stdout
    sys.stdout = captured_output

    ui.display_todos()
    output = captured_output.getvalue()
    sys.stdout = original_stdout

    # Check that the todo is in the output
    assert "Test todo" in output
    assert "[ ]" in output  # Check for uncompleted status


def test_add_update_complete_delete_flow():
    """Test the full flow of adding, updating, completing, and deleting a todo."""
    repo = TodoRepository()
    service = TodoService(repo)
    ui = ConsoleUI(service)

    # Add a todo
    add_result = ui.add_todo("Initial todo")
    assert add_result is True

    # Verify it exists
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].title == "Initial todo"
    assert todos[0].completed is False

    # Update the todo
    update_result = ui.update_todo(1, "Updated todo")
    assert update_result is True

    # Verify the update
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].title == "Updated todo"

    # Complete the todo
    complete_result = ui.complete_todo(1)
    assert complete_result is True

    # Verify completion
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].completed is True

    # Delete the todo
    delete_result = ui.delete_todo(1)
    assert delete_result is True

    # Verify deletion
    todos = service.get_all_todos()
    assert len(todos) == 0


def test_command_parsing():
    """Test that the command parsing works correctly."""
    repo = TodoRepository()
    service = TodoService(repo)
    ui = ConsoleUI(service)

    # Test simple command
    cmd, args = ui.parse_command("add test")
    assert cmd == "add"
    assert args == ["test"]

    # Test command with quoted argument
    cmd, args = ui.parse_command('add "test with spaces"')
    assert cmd == "add"
    assert args == ["test with spaces"]

    # Test command with multiple quoted arguments
    cmd, args = ui.parse_command('update 1 "new title"')
    assert cmd == "update"
    assert args == ["1", "new title"]

    # Test command with mixed quotes
    cmd, args = ui.parse_command("update 1 'new title'")
    assert cmd == "update"
    assert args == ["1", "new title"]


def test_error_handling_invalid_ids():
    """Test that the system handles invalid IDs gracefully."""
    repo = TodoRepository()
    service = TodoService(repo)
    ui = ConsoleUI(service)

    # Try to update a non-existent todo
    captured_output = StringIO()
    import sys
    original_stdout = sys.stdout
    sys.stdout = captured_output

    ui.update_todo(999, "New title")
    output = captured_output.getvalue()
    sys.stdout = original_stdout

    # Should indicate that the todo was not found
    assert "not found" in output.lower()

    # Try to complete a non-existent todo
    captured_output = StringIO()
    sys.stdout = captured_output

    ui.complete_todo(999)
    output = captured_output.getvalue()
    sys.stdout = original_stdout

    assert "not found" in output.lower()

    # Try to delete a non-existent todo
    captured_output = StringIO()
    sys.stdout = captured_output

    ui.delete_todo(999)
    output = captured_output.getvalue()
    sys.stdout = original_stdout

    assert "not found" in output.lower()


def test_empty_input_handling():
    """Test that the system handles empty inputs gracefully."""
    repo = TodoRepository()
    service = TodoService(repo)
    ui = ConsoleUI(service)

    # Try to add an empty todo (should fail)
    captured_output = StringIO()
    import sys
    original_stdout = sys.stdout
    sys.stdout = captured_output

    result = ui.add_todo("")
    output = captured_output.getvalue()
    sys.stdout = original_stdout

    assert result is False
    assert "error" in output.lower() or "valueerror" in output.lower()


def test_ui_integration_with_service_layer():
    """Test that the UI layer correctly interacts with the service layer."""
    repo = TodoRepository()
    service = TodoService(repo)
    ui = ConsoleUI(service)

    # Add a todo through UI
    ui.add_todo("UI test todo")

    # Verify it's in the repository through the service
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].title == "UI test todo"

    # Update through UI
    ui.update_todo(1, "Updated UI test todo")

    # Verify the update through the service
    todos = service.get_all_todos()
    assert todos[0].title == "Updated UI test todo"

    # Complete through UI
    ui.complete_todo(1)

    # Verify completion through the service
    todos = service.get_all_todos()
    assert todos[0].completed is True

    # Delete through UI
    ui.delete_todo(1)

    # Verify deletion through the service
    todos = service.get_all_todos()
    assert len(todos) == 0