---
description: "Task list for In-Memory Python Console Todo App implementation"
---

# Tasks: In-Memory Python Console Todo App (Phase I)

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included based on the requirement for pytest testing in the plan.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/todo/
- [x] T002 Initialize Python 3.13+ project with pyproject.toml
- [x] T003 [P] Create directory structure: src/todo/models/, src/todo/repositories/, src/todo/services/, src/todo/cli/
- [x] T004 [P] Create __init__.py files in all package directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Todo data model in src/todo/models/todo.py
- [x] T006 Create in-memory TodoRepository in src/todo/repositories/todo_repository.py
- [x] T007 [P] Create configuration file in src/config.py
- [x] T008 [P] Set up pytest configuration in pyproject.toml
- [x] T009 Create conftest.py for test configuration in tests/conftest.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Todos (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todos and view them in a list, delivering the fundamental value of a todo application.

**Independent Test**: Can be fully tested by adding a new todo and viewing the list. Delivers the fundamental value of a todo application.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Unit test for Todo model in tests/unit/test_todo.py
- [x] T011 [P] [US1] Unit test for TodoRepository add functionality in tests/unit/test_todo_repository.py
- [x] T012 [P] [US1] Unit test for TodoRepository list functionality in tests/unit/test_todo_repository.py
- [x] T013 [P] [US1] Unit test for TodoService add functionality in tests/unit/test_todo_service.py
- [x] T014 [P] [US1] Unit test for TodoService list functionality in tests/unit/test_todo_service.py

### Implementation for User Story 1

- [x] T015 [US1] Implement Todo model with id, title, completed fields in src/todo/models/todo.py
- [x] T016 [US1] Implement TodoRepository add_todo method in src/todo/repositories/todo_repository.py
- [x] T017 [US1] Implement TodoRepository get_all_todos method in src/todo/repositories/todo_repository.py
- [x] T018 [US1] Create TodoService in src/todo/services/todo_service.py
- [x] T019 [US1] Implement TodoService add_todo method in src/todo/services/todo_service.py
- [x] T020 [US1] Implement TodoService get_all_todos method in src/todo/services/todo_service.py
- [x] T021 [US1] Create ConsoleUI in src/todo/cli/console_ui.py
- [x] T022 [US1] Implement ConsoleUI add_todo command handling in src/todo/cli/console_ui.py
- [x] T023 [US1] Implement ConsoleUI list_todos command handling in src/todo/cli/console_ui.py
- [x] T024 [US1] Create main application entry point in src/main.py
- [x] T025 [US1] Integrate all components in main.py with basic CLI loop

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Mark Todos Complete (Priority: P2)

**Goal**: Allow users to modify existing todo items or mark them as completed by selecting a todo by ID and either updating its content or marking it as complete.

**Independent Test**: Can be fully tested by updating a todo's content and marking a todo as complete. Delivers the ability to manage existing tasks.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T026 [P] [US2] Unit test for TodoService update functionality in tests/unit/test_todo_service.py
- [x] T027 [P] [US2] Unit test for TodoService complete functionality in tests/unit/test_todo_service.py
- [x] T028 [P] [US2] Unit test for TodoRepository update functionality in tests/unit/test_todo_repository.py
- [x] T029 [P] [US2] Unit test for TodoRepository complete functionality in tests/unit/test_todo_repository.py

### Implementation for User Story 2

- [x] T030 [US2] Implement TodoRepository update_todo method in src/todo/repositories/todo_repository.py
- [x] T031 [US2] Implement TodoRepository mark_complete method in src/todo/repositories/todo_repository.py
- [x] T032 [US2] Implement TodoService update_todo method in src/todo/services/todo_service.py
- [x] T033 [US2] Implement TodoService mark_complete method in src/todo/services/todo_service.py
- [x] T034 [US2] Implement ConsoleUI update_todo command handling in src/todo/cli/console_ui.py
- [x] T035 [US2] Implement ConsoleUI complete_todo command handling in src/todo/cli/console_ui.py
- [x] T036 [US2] Add validation for ID existence in all relevant methods

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Delete Todos (Priority: P3)

**Goal**: Allow users to remove completed or unwanted tasks from their todo list by selecting a todo by ID and removing it from the list.

**Independent Test**: Can be fully tested by deleting a todo and verifying it no longer appears in the list. Delivers the ability to remove tasks.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T037 [P] [US3] Unit test for TodoService delete functionality in tests/unit/test_todo_service.py
- [x] T038 [P] [US3] Unit test for TodoRepository delete functionality in tests/unit/test_todo_repository.py

### Implementation for User Story 3

- [x] T039 [US3] Implement TodoRepository delete_todo method in src/todo/repositories/todo_repository.py
- [x] T040 [US3] Implement TodoService delete_todo method in src/todo/services/todo_service.py
- [x] T041 [US3] Implement ConsoleUI delete_todo command handling in src/todo/cli/console_ui.py
- [x] T042 [US3] Add delete command to main CLI loop in src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T043 [P] Implement error handling for invalid IDs in all operations in src/todo/services/todo_service.py
- [x] T044 [P] Implement error handling for empty inputs in src/todo/cli/console_ui.py
- [x] T045 [P] Add input validation for special characters in todo text
- [x] T046 [P] Create README.md with setup and usage instructions
- [x] T047 [P] Add help command to CLI in src/todo/cli/console_ui.py
- [x] T048 [P] Add integration tests in tests/integration/test_cli_integration.py
- [x] T049 [P] Run quickstart validation to ensure all functionality works
- [x] T050 [P] Add command aliases (done for complete, view for list) in src/todo/cli/console_ui.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model in tests/unit/test_todo.py"
Task: "Unit test for TodoRepository add functionality in tests/unit/test_todo_repository.py"
Task: "Unit test for TodoRepository list functionality in tests/unit/test_todo_repository.py"

# Launch all models for User Story 1 together:
Task: "Implement Todo model with id, title, completed fields in src/todo/models/todo.py"
Task: "Create TodoService in src/todo/services/todo_service.py"
Task: "Create ConsoleUI in src/todo/cli/console_ui.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence