# Claude Code Agent Context for Todo App Feature

## Technology Stack
- **Language**: Python 3.13+
- **Package Manager**: uv
- **Architecture**: In-memory console application
- **Storage**: In-memory only (no persistence)
- **Interface**: Menu-driven console interface

## Project Structure
- `/src` - Source code files
- `/specs/1-todo-app` - Feature specification, plan, and related artifacts
- `/history` - Prompt History Records and Architectural Decision Records

## Key Implementation Notes
- All tasks stored in memory only
- Auto-incrementing ID system for tasks
- Menu-driven interface with 6 options
- Input validation to prevent crashes
- Follows PEP 8 Python conventions