# Todo In-Memory Python Console App

A command-line Todo application that allows you to manage tasks entirely in memory. The application supports basic CRUD-style task management and runs in the terminal.

## Features

- Add tasks with title and description
- View all tasks with their status
- Update existing tasks
- Delete tasks by ID
- Mark tasks as complete/incomplete
- Menu-driven console interface
- Comprehensive error handling and input validation
- User-friendly interface with emoji indicators

## Prerequisites

- Python 3.13+
- uv package manager

## Setup

1. Clone the repository
2. Install dependencies: `uv sync` (if there are dependencies) or just run the Python script directly
3. Run the application: `python src/main.py` or `uv run -m src`

## Usage

Run the application and select options from the menu:

1. **Add task** - Create a new task with title and optional description
2. **View tasks** - Display all tasks with their ID, title, description, and completion status
3. **Update task** - Modify an existing task's title or description
4. **Delete task** - Remove a task by its ID
5. **Mark task complete/incomplete** - Toggle the completion status of a task
6. **Exit** - Quit the application

### Examples:
- When adding a task, enter a title and optional description
- When updating a task, you can keep existing values by pressing Enter
- When marking complete/incomplete, enter 1 for complete or 0 for incomplete

## Development

All source code is located in the `/src` directory. Tasks are stored in memory only and reset on application restart. Follow PEP 8 conventions for Python code.

### Project Structure:
- `src/task.py` - Task class definition
- `src/task_manager.py` - Task management logic
- `src/console_interface.py` - User interface logic
- `src/main.py` - Main application entry point

## Error Handling

The application includes comprehensive error handling for:
- Invalid task IDs
- Empty task titles
- Non-numeric inputs
- Empty task lists
- Other edge cases