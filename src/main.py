#!/usr/bin/env python3
"""
Main entry point for the Todo application.
"""

import sys
from src.todo.repositories.todo_repository import TodoRepository
from src.todo.services.todo_service import TodoService
from src.todo.cli.console_ui import ConsoleUI


def main():
    """Main function to run the Todo application."""
    print("Welcome to the Todo App!")
    print("Type 'help' for available commands or 'quit' to exit.")

    # Initialize the application components
    repository = TodoRepository()
    service = TodoService(repository)
    ui = ConsoleUI(service)

    # Main application loop
    while True:
        try:
            user_input = input("Todo App > ").strip()

            if not user_input:
                continue

            command, args = ui.parse_command(user_input)

            if command in ['quit', 'exit']:
                print("Goodbye!")
                break
            elif command in ['help', '?']:
                ui.show_help()
            elif command == 'add':
                if len(args) >= 1:
                    title = args[0] if len(args) == 1 else ' '.join(args)
                    ui.add_todo(title)
                else:
                    print("Usage: add \"todo description\"")
            elif command in ['list', 'view']:
                if len(args) == 0:
                    ui.display_todos()
                else:
                    print("Usage: list or view (no additional arguments needed)")
            elif command == 'update':
                if len(args) >= 2:
                    try:
                        todo_id = int(args[0])
                        new_title = args[1] if len(args) == 2 else ' '.join(args[1:])
                        ui.update_todo(todo_id, new_title)
                    except ValueError:
                        print("Usage: update <id> \"new description\" (id must be a number)")
                else:
                    print("Usage: update <id> \"new description\"")
            elif command in ['complete', 'done']:
                if len(args) == 1:
                    try:
                        todo_id = int(args[0])
                        ui.complete_todo(todo_id)
                    except ValueError:
                        print("Usage: complete <id> or done <id> (id must be a number)")
                else:
                    print("Usage: complete <id> or done <id>")
            elif command == 'delete':
                if len(args) == 1:
                    try:
                        todo_id = int(args[0])
                        ui.delete_todo(todo_id)
                    except ValueError:
                        print("Usage: delete <id> (id must be a number)")
                else:
                    print("Usage: delete <id>")
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()