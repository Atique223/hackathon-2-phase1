"""
Unit tests for the TodoService.
"""

import pytest
from src.todo.models.todo import Todo
from src.todo.repositories.todo_repository import TodoRepository
from src.todo.services.todo_service import TodoService


def test_add_todo():
    """Test adding a todo through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    todo = service.add_todo("Test todo")

    assert isinstance(todo, Todo)
    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.completed is False

    # Verify it's in the repository
    all_todos = service.get_all_todos()
    assert len(all_todos) == 1


def test_get_all_todos():
    """Test getting all todos through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    service.add_todo("First todo")
    service.add_todo("Second todo")

    todos = service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].title == "First todo"
    assert todos[1].title == "Second todo"


def test_update_todo():
    """Test updating a todo through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    original_todo = service.add_todo("Original title")

    success = service.update_todo(original_todo.id, "Updated title")
    assert success is True

    # Verify the update
    updated_todo = service.get_todo_by_id(original_todo.id)
    assert updated_todo.title == "Updated title"


def test_update_todo_not_found():
    """Test updating a todo that doesn't exist."""
    repo = TodoRepository()
    service = TodoService(repo)

    success = service.update_todo(999, "New title")
    assert success is False


def test_mark_complete():
    """Test marking a todo as complete through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    todo = service.add_todo("Test todo")
    assert todo.completed is False

    success = service.mark_complete(todo.id)
    assert success is True

    completed_todo = service.get_todo_by_id(todo.id)
    assert completed_todo.completed is True


def test_mark_complete_not_found():
    """Test marking a todo as complete that doesn't exist."""
    repo = TodoRepository()
    service = TodoService(repo)

    success = service.mark_complete(999)
    assert success is False


def test_mark_incomplete():
    """Test marking a todo as incomplete through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    todo = service.add_todo("Test todo")
    service.mark_complete(todo.id)
    assert todo.completed is True

    success = service.mark_incomplete(todo.id)
    assert success is True

    incomplete_todo = service.get_todo_by_id(todo.id)
    assert incomplete_todo.completed is False


def test_mark_incomplete_not_found():
    """Test marking a todo as incomplete that doesn't exist."""
    repo = TodoRepository()
    service = TodoService(repo)

    success = service.mark_incomplete(999)
    assert success is False


def test_delete_todo():
    """Test deleting a todo through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    todo = service.add_todo("Test todo")

    success = service.delete_todo(todo.id)
    assert success is True

    # Verify it's gone
    all_todos = service.get_all_todos()
    assert len(all_todos) == 0


def test_delete_todo_not_found():
    """Test deleting a todo that doesn't exist."""
    repo = TodoRepository()
    service = TodoService(repo)

    success = service.delete_todo(999)
    assert success is False


def test_get_todo_by_id():
    """Test getting a todo by ID through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    added_todo = service.add_todo("Test todo")

    retrieved_todo = service.get_todo_by_id(added_todo.id)
    assert retrieved_todo is not None
    assert retrieved_todo.id == added_todo.id
    assert retrieved_todo.title == added_todo.title


def test_get_todo_by_id_not_found():
    """Test getting a todo by ID that doesn't exist."""
    repo = TodoRepository()
    service = TodoService(repo)

    retrieved_todo = service.get_todo_by_id(999)
    assert retrieved_todo is None


def test_validate_todo_id():
    """Test validating a todo ID through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    todo = service.add_todo("Test todo")

    # Valid ID should return True
    is_valid = service.validate_todo_id(todo.id)
    assert is_valid is True

    # Invalid ID should return False
    is_valid = service.validate_todo_id(999)
    assert is_valid is False


def test_multiple_operations():
    """Test multiple operations through the service."""
    repo = TodoRepository()
    service = TodoService(repo)

    # Add multiple todos
    todo1 = service.add_todo("First todo")
    todo2 = service.add_todo("Second todo")
    todo3 = service.add_todo("Third todo")

    # Verify all exist
    all_todos = service.get_all_todos()
    assert len(all_todos) == 3

    # Update one
    service.update_todo(todo2.id, "Updated second todo")
    updated_todo = service.get_todo_by_id(todo2.id)
    assert updated_todo.title == "Updated second todo"

    # Mark one complete
    service.mark_complete(todo1.id)
    completed_todo = service.get_todo_by_id(todo1.id)
    assert completed_todo.completed is True

    # Delete one
    service.delete_todo(todo3.id)
    remaining_todos = service.get_all_todos()
    assert len(remaining_todos) == 2