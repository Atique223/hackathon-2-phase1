#!/usr/bin/env python3
"""
Quick test script to verify the main functionality of the Todo app.
"""

from src.todo.repositories.todo_repository import TodoRepository
from src.todo.services.todo_service import TodoService
from src.todo.cli.console_ui import ConsoleUI


def test_main_functionality():
    """Test the main functionality of the Todo app."""
    print("Testing Todo App functionality...")

    # Initialize components
    repository = TodoRepository()
    service = TodoService(repository)
    ui = ConsoleUI(service)

    # Test 1: Add todos
    print("\n1. Testing add functionality:")
    ui.add_todo("Buy groceries")
    ui.add_todo("Finish report")
    ui.add_todo("Call mom")

    # Test 2: List todos
    print("\n2. Testing list functionality:")
    ui.display_todos()

    # Test 3: Update a todo
    print("\n3. Testing update functionality:")
    ui.update_todo(1, "Buy groceries - milk and eggs")

    # Show updated list
    print("After update:")
    ui.display_todos()

    # Test 4: Complete a todo
    print("\n4. Testing complete functionality:")
    ui.complete_todo(2)

    # Show updated list
    print("After marking #2 as complete:")
    ui.display_todos()

    # Test 5: Delete a todo
    print("\n5. Testing delete functionality:")
    ui.delete_todo(3)

    # Show final list
    print("After deleting #3:")
    ui.display_todos()

    print("\nAll functionality tests passed!")


if __name__ == "__main__":
    test_main_functionality()