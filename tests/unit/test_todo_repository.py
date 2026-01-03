"""
Unit tests for the TodoRepository.
"""

import pytest
from src.todo.models.todo import Todo
from src.todo.repositories.todo_repository import TodoRepository


def test_add_todo():
    """Test adding a todo to the repository."""
    repo = TodoRepository()
    todo = repo.add_todo("Test todo")

    assert isinstance(todo, Todo)
    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.completed is False
    assert len(repo.get_all_todos()) == 1


def test_add_todo_with_empty_title():
    """Test that adding a todo with empty title raises an error."""
    repo = TodoRepository()
    with pytest.raises(ValueError):
        repo.add_todo("")


def test_add_todo_with_whitespace_title():
    """Test that adding a todo with whitespace-only title raises an error."""
    repo = TodoRepository()
    with pytest.raises(ValueError):
        repo.add_todo("   ")


def test_get_all_todos():
    """Test getting all todos from the repository."""
    repo = TodoRepository()
    repo.add_todo("First todo")
    repo.add_todo("Second todo")

    todos = repo.get_all_todos()
    assert len(todos) == 2
    assert todos[0].id == 1
    assert todos[0].title == "First todo"
    assert todos[1].id == 2
    assert todos[1].title == "Second todo"


def test_get_todo_by_id():
    """Test getting a todo by its ID."""
    repo = TodoRepository()
    added_todo = repo.add_todo("Test todo")

    retrieved_todo = repo.get_todo_by_id(added_todo.id)
    assert retrieved_todo is not None
    assert retrieved_todo.id == added_todo.id
    assert retrieved_todo.title == added_todo.title
    assert retrieved_todo.completed == added_todo.completed


def test_get_todo_by_id_not_found():
    """Test getting a todo that doesn't exist."""
    repo = TodoRepository()
    todo = repo.add_todo("Test todo")

    retrieved_todo = repo.get_todo_by_id(999)
    assert retrieved_todo is None


def test_update_todo():
    """Test updating a todo's title."""
    repo = TodoRepository()
    original_todo = repo.add_todo("Original title")

    success = repo.update_todo(original_todo.id, "Updated title")
    assert success is True

    updated_todo = repo.get_todo_by_id(original_todo.id)
    assert updated_todo.title == "Updated title"


def test_update_todo_not_found():
    """Test updating a todo that doesn't exist."""
    repo = TodoRepository()
    success = repo.update_todo(999, "New title")
    assert success is False


def test_update_todo_empty_title():
    """Test that updating a todo with empty title raises an error."""
    repo = TodoRepository()
    original_todo = repo.add_todo("Original title")

    with pytest.raises(ValueError):
        repo.update_todo(original_todo.id, "")


def test_update_todo_whitespace_title():
    """Test that updating a todo with whitespace-only title raises an error."""
    repo = TodoRepository()
    original_todo = repo.add_todo("Original title")

    with pytest.raises(ValueError):
        repo.update_todo(original_todo.id, "   ")


def test_mark_complete():
    """Test marking a todo as complete."""
    repo = TodoRepository()
    todo = repo.add_todo("Test todo")
    assert todo.completed is False

    success = repo.mark_complete(todo.id)
    assert success is True

    completed_todo = repo.get_todo_by_id(todo.id)
    assert completed_todo.completed is True


def test_mark_complete_not_found():
    """Test marking a todo as complete that doesn't exist."""
    repo = TodoRepository()
    success = repo.mark_complete(999)
    assert success is False


def test_mark_incomplete():
    """Test marking a todo as incomplete."""
    repo = TodoRepository()
    todo = repo.add_todo("Test todo")
    repo.mark_complete(todo.id)
    assert todo.completed is True

    success = repo.mark_incomplete(todo.id)
    assert success is True

    incomplete_todo = repo.get_todo_by_id(todo.id)
    assert incomplete_todo.completed is False


def test_mark_incomplete_not_found():
    """Test marking a todo as incomplete that doesn't exist."""
    repo = TodoRepository()
    success = repo.mark_incomplete(999)
    assert success is False


def test_delete_todo():
    """Test deleting a todo."""
    repo = TodoRepository()
    todo = repo.add_todo("Test todo")

    success = repo.delete_todo(todo.id)
    assert success is True
    assert len(repo.get_all_todos()) == 0


def test_delete_todo_not_found():
    """Test deleting a todo that doesn't exist."""
    repo = TodoRepository()
    success = repo.delete_todo(999)
    assert success is False


def test_id_sequential_assignment():
    """Test that IDs are assigned sequentially."""
    repo = TodoRepository()
    todo1 = repo.add_todo("First todo")
    todo2 = repo.add_todo("Second todo")
    todo3 = repo.add_todo("Third todo")

    assert todo1.id == 1
    assert todo2.id == 2
    assert todo3.id == 3


def test_multiple_operations():
    """Test multiple operations in sequence."""
    repo = TodoRepository()

    # Add multiple todos
    todo1 = repo.add_todo("First todo")
    todo2 = repo.add_todo("Second todo")
    todo3 = repo.add_todo("Third todo")

    # Verify all exist
    all_todos = repo.get_all_todos()
    assert len(all_todos) == 3

    # Update one
    repo.update_todo(todo2.id, "Updated second todo")
    updated_todo = repo.get_todo_by_id(todo2.id)
    assert updated_todo.title == "Updated second todo"

    # Mark one complete
    repo.mark_complete(todo1.id)
    completed_todo = repo.get_todo_by_id(todo1.id)
    assert completed_todo.completed is True

    # Delete one
    repo.delete_todo(todo3.id)
    remaining_todos = repo.get_all_todos()
    assert len(remaining_todos) == 2