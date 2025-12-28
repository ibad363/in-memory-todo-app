# Data Model for Todo In-Memory Python Console App

## Task Entity
- **id**: integer, unique, auto-incremented
- **title**: string (required)
- **description**: string (optional)
- **completed**: boolean (default: False)

## TaskList Entity
- **tasks**: collection of Task entities stored in memory
- **next_id**: integer to track the next available ID for auto-increment

## Validation Rules
- Task title must not be empty
- Task ID must be unique within the TaskList
- Task ID must be a positive integer
- Task description can be empty but not null

## State Transitions
- Task.completed: False → True (when marking as complete)
- Task.completed: True → False (when marking as incomplete)