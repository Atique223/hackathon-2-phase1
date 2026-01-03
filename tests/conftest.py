"""
Pytest configuration and fixtures for the Todo application tests.
"""

import pytest
from src.todo.repositories.todo_repository import TodoRepository
from src.todo.services.todo_service import TodoService


@pytest.fixture
def todo_repository():
    """Create a fresh TodoRepository for each test."""
    return TodoRepository()


@pytest.fixture
def todo_service(todo_repository):
    """Create a TodoService with a fresh repository for each test."""
    return TodoService(todo_repository)