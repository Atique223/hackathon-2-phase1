# CLI Contract: Todo Application

## Overview
This document defines the command-line interface contract for the In-Memory Python Console Todo App.

## Commands

### Add Todo
- **Command**: `add "todo description"`
- **Input**: Todo description as a string (quoted if containing spaces)
- **Output**: Success message with assigned ID
- **Example**: `add "Buy groceries"` → "Added todo #1: Buy groceries"

### List Todos
- **Command**: `list` or `view`
- **Input**: None
- **Output**: Formatted list of all todos with IDs and completion status
- **Example**:
  ```
  1. [ ] Buy groceries
  2. [x] Finish report
  ```

### Update Todo
- **Command**: `update <id> "new description"`
- **Input**: Todo ID (integer) and new description string
- **Output**: Success message confirming update
- **Example**: `update 1 "Buy groceries - milk and eggs"` → "Updated todo #1"

### Complete Todo
- **Command**: `complete <id>` or `done <id>`
- **Input**: Todo ID (integer)
- **Output**: Success message confirming completion
- **Example**: `complete 1` → "Marked todo #1 as complete"

### Delete Todo
- **Command**: `delete <id>`
- **Input**: Todo ID (integer)
- **Output**: Success message confirming deletion
- **Example**: `delete 1` → "Deleted todo #1"

## Error Handling
- Invalid commands show help message
- Invalid IDs show appropriate error message
- Empty inputs show appropriate error message
- All errors include user-friendly messages

## Exit Codes
- 0: Success
- 1: General error
- 2: Invalid input/command