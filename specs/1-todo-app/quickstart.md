# Quickstart Guide for Todo In-Memory Python Console App

## Prerequisites
- Python 3.13+
- uv package manager

## Setup
1. Clone the repository
2. Install dependencies: `uv sync` (if there are dependencies) or just run the Python script directly
3. Run the application: `python src/main.py` (or wherever the main file is located)

## Usage
1. Run the application
2. Select options from the menu:
   - 1. Add task
   - 2. View tasks
   - 3. Update task
   - 4. Delete task
   - 5. Mark task complete/incomplete
   - 6. Exit

## Development
- All source code is located in the `/src` directory
- Tasks are stored in memory only and reset on application restart
- Follow PEP 8 conventions for Python code