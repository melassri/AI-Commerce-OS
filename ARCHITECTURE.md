# AI-Commerce-OS Architecture

## Overall Architecture

AI-Commerce-OS is a modular monolith with a Clean Architecture orientation. It is designed to begin as a single deployable service while preserving bounded-context boundaries that can support future independent deployment or asynchronous integration when justified.

The FastAPI application is the inbound HTTP adapter and composition root. It wires configuration, observability, persistence, caching, and future message infrastructure without owning business behavior.

## Module Organization

`src/ai_commerce_os/modules/` is reserved for bounded contexts such as catalog, supplier, workflow, and AI. Each module owns its language, behavior, interfaces, tests, and documentation. A module should expose explicit contracts rather than allow other modules to depend on its internals.

The platform-level package contains cross-cutting adapters and startup composition. Shared packages are exceptional and are limited to stable, broadly owned primitives.

## Dependency Direction

Dependencies flow inward:

```text
Presentation / Infrastructure
            ↓
       Application
            ↓
          Domain
```

The domain is independent of FastAPI, SQLModel, Redis, and external transports. Infrastructure implements interfaces required by the application or domain. Presentation adapters translate external input and output at the system edge.

## Application Layers

- **Domain** — entities, value objects, domain services, invariants, and domain events.
- **Application** — use cases, orchestration, transaction boundaries, and ports.
- **Infrastructure** — database, cache, event broker, and external-provider adapters.
- **Presentation** — HTTP routes, request/response schemas, and other inbound transports.

No layer is required to exist until a module has a clear responsibility for it.

## Infrastructure

PostgreSQL is the system of record and SQLModel is the current persistence integration. Alembic owns schema migrations. Redis provides an integration point for caching and future coordination needs. Structlog provides structured operational logs. Settings are supplied by environment-driven Pydantic configuration.

Infrastructure dependencies are created at the composition root and passed into application-level ports. The domain layer must not know which infrastructure implementation is active.

## Event-Driven Vision

Modules will publish domain events when meaningful state transitions occur. Cross-module consumers will depend on event contracts rather than internal module implementations. Durable publication should use a transactional outbox once persistence-backed events are introduced, so state changes and event records are committed together.

Synchronous calls remain appropriate for simple, local use cases. Events are introduced to preserve module autonomy and reliability, not as a default transport for every interaction.
