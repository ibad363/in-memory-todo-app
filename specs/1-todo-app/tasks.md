# Tasks: Todo In-Memory Python Console App

## Feature Overview
Build a command-line Todo application that allows a user to manage tasks entirely in memory. The application supports basic CRUD-style task management and runs in the terminal with Python 3.13+ and uv package manager.

## Phase 1: Setup
**Goal**: Initialize project structure and development environment

**Independent Test**: Project structure exists with proper directories and can run a basic Python script

- [X] T001 Create project directory structure with /src, /specs, /history directories
- [X] T002 [P] Create pyproject.toml file with basic configuration for uv
- [X] T003 [P] Create README.md with project description and setup instructions
- [X] T004 Create CLAUDE.md with Claude Code instructions for this project

## Phase 2: Foundational Components
**Goal**: Implement core data structures and validation logic that all user stories depend on

**Independent Test**: Core Task and TaskManager classes exist with proper validation and in-memory storage

- [X] T005 Create Task class in src/task.py with id, title, description, completed attributes
- [X] T006 Implement Task validation for required fields in src/task.py
- [X] T007 Create TaskManager class in src/task_manager.py with in-memory storage
- [X] T008 Implement auto-incrementing ID functionality in TaskManager
- [X] T009 Implement basic add_task method in TaskManager with validation

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1)
**Goal**: Implement core functionality to add tasks and view all tasks

**Independent Test**: Can add a task and view the list of tasks to verify it appears with correct information

**Acceptance Scenarios**:
1. Given I am using the todo app, When I add a task with title and description, Then the task appears in the task list with a unique ID and status as incomplete
2. Given I have added tasks to the app, When I view all tasks, Then I see all tasks with their ID, title, description, and completion status

- [X] T010 [US1] Implement get_all_tasks method in TaskManager
- [X] T011 [US1] Create ConsoleInterface class in src/console_interface.py
- [X] T012 [US1] Implement display_tasks method in ConsoleInterface
- [X] T013 [US1] Implement add_task method in ConsoleInterface with user input
- [X] T014 [US1] Create main menu loop in src/main.py with add/view options
- [X] T015 [US1] Integrate TaskManager with ConsoleInterface in main application
- [X] T016 [US1] Test basic add and view functionality

## Phase 4: User Story 2 - Update and Delete Tasks (Priority: P2)
**Goal**: Implement functionality to update existing tasks and delete tasks by ID

**Independent Test**: Can update or delete a task and verify the changes are reflected in the task list

**Acceptance Scenarios**:
1. Given I have existing tasks, When I update a task's title or description, Then the changes are reflected when I view the task list
2. Given I have existing tasks, When I delete a task by its ID, Then the task is removed from the task list

- [X] T017 [US2] Implement update_task method in TaskManager
- [X] T018 [US2] Implement delete_task method in TaskManager
- [X] T019 [US2] Implement update_task method in ConsoleInterface with user input
- [X] T020 [US2] Implement delete_task method in ConsoleInterface with user input
- [X] T021 [US2] Add update and delete options to main menu in src/main.py
- [X] T022 [US2] Test update and delete functionality

## Phase 5: User Story 3 - Mark Tasks Complete/Incomplete (Priority: P3)
**Goal**: Implement functionality to mark tasks as complete or incomplete

**Independent Test**: Can mark a task as complete/incomplete and verify the status change is visible in the task list

**Acceptance Scenarios**:
1. Given I have tasks in the list, When I mark a task as complete, Then the task shows as completed when viewing the list
2. Given I have completed tasks, When I mark a task as incomplete, Then the task shows as pending when viewing the list

- [X] T023 [US3] Implement mark_task_complete method in TaskManager
- [X] T024 [US3] Implement mark_task_complete method in ConsoleInterface with user input
- [X] T025 [US3] Add mark complete/incomplete option to main menu in src/main.py
- [X] T026 [US3] Test mark complete/incomplete functionality

## Phase 6: Error Handling and Edge Cases
**Goal**: Implement proper error handling and validation for all operations

**Independent Test**: Application handles invalid inputs and edge cases gracefully without crashing

**Addressed Edge Cases**:
- User tries to update/delete a task that doesn't exist
- Empty input for task title
- Empty task list when viewing tasks
- Invalid input (non-numeric ID) when selecting a task

- [X] T027 Implement error handling for invalid task IDs in all operations
- [X] T028 Implement validation for empty task titles in add/update operations
- [X] T029 Implement message for empty task list when viewing tasks
- [X] T030 Add input validation to prevent crashes from invalid user input
- [X] T031 Test error handling for all edge cases

## Phase 7: Polish & Cross-Cutting Concerns
**Goal**: Complete the application with proper formatting, documentation, and final validation

**Independent Test**: Complete application works as specified with good user experience

- [X] T032 Improve UI formatting and user experience in ConsoleInterface
- [X] T033 Add comprehensive docstrings to all classes and methods
- [X] T034 Ensure code follows PEP 8 conventions and snake_case naming
- [X] T035 Test complete user flow: add task → view tasks → mark complete → view updated status
- [X] T036 Validate all functional requirements (FR-001 through FR-010) are implemented
- [X] T037 Update README.md with complete usage instructions
- [X] T038 Final validation that all success criteria are met

## Dependencies
- User Story 2 (Update/Delete) depends on Phase 2 (Foundational Components) being completed
- User Story 3 (Mark Complete/Incomplete) depends on Phase 2 (Foundational Components) being completed
- All user stories depend on Phase 1 (Setup) being completed

## Parallel Execution Examples
- Tasks T002 and T003 can be executed in parallel during Phase 1
- Tasks T017-T020 can be worked on in parallel with T023-T024 during Phase 4 and 5
- All error handling tasks (T027-T030) can be implemented in parallel after core functionality

## Implementation Strategy
- **MVP Scope**: Complete Phase 1, Phase 2, and Phase 3 for basic add/view functionality
- **Incremental Delivery**: Each phase delivers independently testable functionality
- **Risk Mitigation**: Error handling implemented in Phase 6 after core functionality