# Todo In-Memory Python Console App Constitution

## Core Principles

### Code Quality Standards
All Python code must follow PEP 8 conventions. Variable and function names must be clear, descriptive, and snake_case. Functions should be single-responsibility and no longer than 30 lines. Code must include inline comments for complex logic. Maintain a clean project structure: /src, /specs, /history, README.md, CLAUDE.md.

### Specification-Driven Development
Every feature must have a corresponding spec file in /specs before implementation. Use Spec-Kit Plus workflow for all development: /sp.specify → /sp.plan → /sp.tasks → /sp.implement. No manual coding allowed; all implementation must be generated via Claude Code guided by specs.

### Task Management Rules
Tasks must have unique IDs and include: Title (string), Description (string), Status (Pending/Complete). All operations (Add, Delete, Update, View, Mark Complete) must respect data consistency. Task listing must show status indicators clearly.

### Documentation Standards
README.md must include setup instructions, usage guide, and project structure explanation. CLAUDE.md must include Claude Code instructions, AI prompts used, and iterative steps. All specifications, plans, and ADRs must be stored in /history folder for reusable intelligence.

### AI-Oriented Development
All AI-generated code must follow human-readable formatting. Prompt History (PHR) for Claude Code must be documented for future reference. AI outputs must be reviewed for correctness, clarity, and completeness before committing.

### Testing and Verification
All implemented features must be verified manually via console. Ensure all basic functionalities work: 1. Add task, 2. Delete task, 3. Update task, 4. View tasks, 5. Mark task as complete/incomplete. No partial implementation allowed; each feature must pass verification before commit.

## Development Workflow
The development workflow follows the Spec-Kit Plus process: /sp.specify → /sp.plan → /sp.tasks → /sp.implement. All code changes must be reviewed and verified through console testing before being committed.

## Governance
Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance. Complexity must be justified. Use CLAUDE.md for runtime development guidance.

**Version**: 1.1.0 | **Ratified**: TODO(RATIFICATION_DATE): Please provide the original ratification date. | **Last Amended**: 2025-12-28
