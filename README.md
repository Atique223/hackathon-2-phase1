# In-Memory Python Console Todo App

A simple command-line todo application that stores tasks in memory only. This application provides core functionality for adding, viewing, updating, deleting, and marking todos as complete.

## Features

- Add new todo items
- View all todos with completion status
- Update existing todo items
- Mark todos as complete/incomplete
- Delete todos
- In-memory storage (no persistence)

## Requirements

- Python 3.13+

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -e .
   ```
   Or if using uv:
   ```bash
   uv sync
   ```

## Usage

Run the application:
```bash
python -m src.main
```

### Available Commands

- `add "todo description"` - Add a new todo
- `list` or `view` - Show all todos
- `update <id> "new description"` - Update a todo
- `complete <id>` or `done <id>` - Mark a todo as complete
- `delete <id>` - Delete a todo
- `help` - Show help message
- `quit` or `exit` - Exit the application

### Example Usage

```
Todo App > add "Buy groceries"
Added todo #1: Buy groceries

Todo App > add "Finish report"
Added todo #2: Finish report

Todo App > list
1. [ ] Buy groceries
2. [ ] Finish report

Todo App > complete 1
Marked todo #1 as complete

Todo App > list
1. [x] Buy groceries
2. [ ] Finish report

Todo App > quit
Goodbye!
```

## Project Structure

```
src/
├── todo/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── todo.py           # Todo data model
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── todo_repository.py # In-memory repository
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_service.py   # Business logic layer
│   └── cli/
│       ├── __init__.py
│       └── console_ui.py     # Console interface
├── main.py                 # Application entry point
└── config.py               # Configuration settings

tests/
├── unit/
│   ├── test_todo.py
│   ├── test_todo_repository.py
│   └── test_todo_service.py
├── integration/
│   └── test_cli_integration.py
└── conftest.py
```

## Running Tests

To run all tests:
```bash
pytest
```

To run unit tests only:
```bash
pytest tests/unit/
```

To run integration tests only:
```bash
pytest tests/integration/
```

## Architecture

The application follows a clean architecture with distinct layers:

- **Models**: Data structures (Todo entity)
- **Repositories**: Data access layer (in-memory storage)
- **Services**: Business logic layer (TodoService)
- **CLI**: User interface layer (ConsoleUI)# hackathon-2-phase1
