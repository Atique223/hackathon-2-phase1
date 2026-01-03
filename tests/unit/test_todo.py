"""
Unit tests for the Todo model.
"""

import pytest
from src.todo.models.todo import Todo


def test_todo_creation():
    """Test creating a valid Todo object."""
    todo = Todo(id=1, title="Test todo", completed=False)
    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.completed is False


def test_todo_creation_defaults():
    """Test creating a Todo object with default completion status."""
    todo = Todo(id=1, title="Test todo")
    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.completed is False


def test_todo_mark_complete():
    """Test marking a todo as complete."""
    todo = Todo(id=1, title="Test todo", completed=False)
    todo.mark_complete()
    assert todo.completed is True


def test_todo_mark_incomplete():
    """Test marking a todo as incomplete."""
    todo = Todo(id=1, title="Test todo", completed=True)
    todo.mark_incomplete()
    assert todo.completed is False


def test_todo_update_title():
    """Test updating a todo's title."""
    todo = Todo(id=1, title="Old title", completed=False)
    todo.update_title("New title")
    assert todo.title == "New title"


def test_todo_update_title_validation():
    """Test that updating a todo's title validates the new title."""
    todo = Todo(id=1, title="Test todo", completed=False)
    with pytest.raises(ValueError):
        todo.update_title("")


def test_todo_string_representation():
    """Test the string representation of a todo."""
    todo = Todo(id=1, title="Test todo", completed=False)
    assert str(todo) == "1. [ ] Test todo"

    todo.mark_complete()
    assert str(todo) == "1. [x] Test todo"


def test_todo_repr():
    """Test the developer-friendly representation of a todo."""
    todo = Todo(id=1, title="Test todo", completed=True)
    repr_str = repr(todo)
    assert "Todo(id=1" in repr_str
    assert "title='Test todo'" in repr_str
    assert "completed=True" in repr_str


def test_todo_id_validation():
    """Test that Todo validates the ID."""
    with pytest.raises(ValueError):
        Todo(id=0, title="Test todo", completed=False)

    with pytest.raises(ValueError):
        Todo(id=-1, title="Test todo", completed=False)

    with pytest.raises(ValueError):
        Todo(id="1", title="Test todo", completed=False)


def test_todo_title_validation():
    """Test that Todo validates the title."""
    with pytest.raises(ValueError):
        Todo(id=1, title="", completed=False)

    with pytest.raises(ValueError):
        Todo(id=1, title="   ", completed=False)

    with pytest.raises(ValueError):
        Todo(id=1, title=123, completed=False)


def test_todo_completed_validation():
    """Test that Todo validates the completed status."""
    with pytest.raises(ValueError):
        Todo(id=1, title="Test todo", completed="True")

    with pytest.raises(ValueError):
        Todo(id=1, title="Test todo", completed=1)