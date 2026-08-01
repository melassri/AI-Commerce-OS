# AI-Commerce-OS Agent Guide

## Project Philosophy

AI-Commerce-OS is a production-oriented, modular commerce platform. The project favors clear boundaries, explicit contracts, small reversible changes, and operational safety. Build foundations before features, keep knowledge close to its owning module, and optimize for maintainability by both human contributors and future AI agents.

## Coding Conventions

- Use Python 3.13, type annotations, and the configured Ruff and Mypy rules.
- Keep names explicit and domain-oriented; avoid ambiguous helpers and catch-all utility modules.
- Keep modules cohesive. Public module contracts must be intentional and documented.
- Keep configuration in settings and environment variables. Do not embed secrets, environment names, or infrastructure addresses in application code.
- Prefer small, focused commits and avoid unrelated formatting or refactors in feature changes.

## Review Workflow

1. Read the relevant architecture and module documentation before changing code.
2. Define the smallest change that satisfies the task and its acceptance criteria.
3. Run `make format`, `make check`, and any relevant focused tests before review.
4. Review the diff for unwanted files, generated artifacts, secrets, and boundary violations.
5. Explain behavior, tests, risks, and follow-up work in the change description.

## Architecture Principles

- Preserve inward dependency direction: presentation and infrastructure depend on application and domain layers, never the reverse.
- Keep bounded contexts independent; communicate across contexts through explicit contracts and events.
- Put business rules in the owning domain and application layer, not in transports, ORM models, or background adapters.
- Treat the composition root as the location for wiring dependencies, not business behavior.
- Design asynchronous integration around domain events and an eventual transactional-outbox boundary.

## Forbidden Patterns

- Do not import another module's internal domain, application, or infrastructure implementation.
- Do not place business logic in FastAPI route handlers, Pydantic settings, SQLModel entities, or migration scripts.
- Do not access databases, Redis, HTTP clients, or message brokers directly from domain code.
- Do not add global mutable state, hidden I/O, broad exception suppression, or untyped `Any` escape hatches.
- Do not introduce shared packages merely to bypass a module boundary.

## Repository Strategy

- `src/ai_commerce_os/` contains the composition root and platform adapters.
- `src/ai_commerce_os/modules/` contains bounded contexts and their future layers.
- `packages/` is reserved for narrowly governed shared kernel and cross-cutting packages.
- `tests/` mirrors the unit, integration, and contract testing levels.
- `docs/` and `planning/` are source-controlled project knowledge, not generated output.

## Testing Philosophy

- Prefer fast, deterministic unit tests for domain and application behavior.
- Use integration tests for infrastructure adapters and contract tests for external interfaces.
- Test observable behavior and boundaries instead of implementation details.
- Keep tests isolated: external services must be explicit test dependencies, never incidental local state.
- A change is not ready until its relevant quality checks and tests pass.
