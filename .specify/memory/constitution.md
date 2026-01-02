<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial creation)
- Added sections: All principles and governance based on project requirements
- Templates requiring updates: N/A (new constitution)
- Follow-up TODOs: None
-->
# AI-native Todo Application Constitution

## Core Principles

### I. Simplicity First
Start minimal and evolve incrementally. Each phase must introduce only the minimum required new complexity. No premature optimization or overengineering before the corresponding phase. Focus on deterministic behavior especially in Phase I in-memory logic.

### II. Clear Separation of Concerns
Maintain distinct boundaries between domain logic, infrastructure, and interfaces. All business logic must be testable without UI dependencies. Each phase builds cleanly on the previous with clear layer separation.

### III. Progressive Enhancement
Every phase progressively enhances the previous one while maintaining core functionality. AI components must be optional and non-blocking to core functionality. Each phase must be fully functional on its own before advancing.

### IV. AI-Native Readiness
Design decisions must anticipate AI integration. Architectural choices should support future AI capabilities without blocking current functionality. Ensure clean interfaces that can accommodate AI agents operating via defined tools and contracts.

### V. Developer Ergonomics
Prioritize readable code, clear structure, and fast iteration. Console UX must be intuitive, explicit, and error-tolerant. Dependencies should be minimized in early phases with clear documentation of architectural changes between phases.

### VI. Deterministic Behavior
Especially critical for Phase I in-memory logic. All operations must have predictable, repeatable outcomes. Business logic must be testable and maintain consistent behavior across phases.

## Technical Standards

### Code Quality Requirements
- Python code must follow PEP 8 and idiomatic patterns
- Phase I must be fully in-memory (no filesystem or database persistence)
- Functional correctness prioritized over premature optimization
- Dependency minimization in early phases
- Clear boundaries between domain logic, infrastructure, and interfaces

### Architecture Constraints
- Phase I: No external databases, no web frameworks, no background workers
- Phase II: REST-first API design, typed models, schema-driven validation
- Phase III: AI agents must operate via defined tools and contracts
- Phase IV: Must run locally via Minikube with one-command startup
- Phase V: Must support event-driven and scalable architecture

### Documentation Requirements
- Explicit documentation of architectural changes between phases
- All changes must be small, testable, and reference code precisely
- Backward compatibility where feasible between phases
- Documentation required at every phase transition

## Development Workflow

### Implementation Guidelines
- Clarify and plan first - keep business understanding separate from technical plan
- Do not invent APIs, data, or contracts; ask targeted clarifiers if missing
- Never hardcode secrets or tokens; use `.env` and docs
- Prefer the smallest viable diff; do not refactor unrelated code
- Cite existing code with code references; propose new code in fenced blocks

### Quality Gates
- Clear, testable acceptance criteria included
- Explicit error paths and constraints stated
- Smallest viable change; no unrelated edits
- Code references to modified/inspected files where relevant
- All business logic must be testable without UI dependencies

### Testing Requirements
- TDD mandatory: Tests written → User approved → Tests fail → Then implement
- Red-Green-Refactor cycle strictly enforced
- Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas
- All business logic must be testable without UI dependencies

## Governance

This constitution supersedes all other practices and development guidelines. All implementation work must align with these principles. Amendments require explicit documentation, approval process, and migration plan if applicable. All PRs and reviews must verify compliance with these principles. Complexity must be justified with clear rationale tied to project phases and requirements.

**Version**: 1.0.0 | **Ratified**: 2026-01-03 | **Last Amended**: 2026-01-03