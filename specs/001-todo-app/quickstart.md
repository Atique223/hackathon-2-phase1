# Quickstart: In-Memory Python Console Todo App

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone the repository
2. Install dependencies: `uv sync`
3. Run the application: `python -m src.main`

## Usage
### Basic Commands
- `add "todo description"` - Add a new todo
- `list` - View all todos
- `update <id> "new description"` - Update a todo
- `complete <id>` - Mark a todo as complete
- `delete <id>` - Delete a todo

### Example Workflow
```
$ python -m src.main
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
Todo App >
```

## Development
1. Run tests: `pytest`
2. Run specific test: `pytest tests/unit/test_todo.py`
3. Run all tests: `pytest tests/`

## Project Structure
- `src/todo/models/` - Data models
- `src/todo/repositories/` - Data access layer
- `src/todo/services/` - Business logic
- `src/todo/cli/` - Console interface
- `tests/` - Unit and integration tests