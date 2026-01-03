# Data Model: In-Memory Python Console Todo App (Phase I)

## Todo Entity

### Fields
- **id** (int): Unique identifier for the todo item, assigned sequentially
- **title** (str): The content/description of the todo item
- **completed** (bool): Status indicating whether the todo is completed (True) or active (False)

### Validation Rules
- **id**: Must be a positive integer, unique within the todo list
- **title**: Must be a non-empty string (1+ characters)
- **completed**: Must be a boolean value (True/False)

### State Transitions
- **Active** (completed=False) → **Completed** (completed=True): When user marks todo as complete
- **Completed** (completed=True) → **Active** (completed=False): When user marks todo as incomplete (optional future enhancement)

## Todo List Collection

### Structure
- **Type**: In-memory Python list containing Todo entities
- **Access**: Sequential ID-based access for operations
- **Constraints**: No persistence, exists only during application runtime

### Operations Supported
- Add new todo (append to list)
- Retrieve all todos (iterate through list)
- Update todo by ID (find by ID, modify properties)
- Delete todo by ID (find by ID, remove from list)
- Mark complete/incomplete by ID (find by ID, update completion status)

## Data Flow

### Creation
1. User provides title via CLI
2. System assigns next available ID (auto-increment)
3. Todo object created with id, title, completed=False
4. Todo added to in-memory list

### Retrieval
1. System iterates through in-memory list
2. Returns all Todo objects for display

### Update
1. User provides ID and new title
2. System finds Todo by ID in list
3. Updates title property of existing Todo

### Completion
1. User provides ID
2. System finds Todo by ID in list
3. Updates completed property to True

### Deletion
1. User provides ID
2. System finds Todo by ID in list
3. Removes Todo from list