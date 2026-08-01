# Architecture Decision Record Index

This index tracks architecture decisions. Product, pricing, supplier, and other business decisions are intentionally out of scope.

| ID | Decision | Status |
| --- | --- | --- |
| ADR-001 | Use a modular monolith as the initial deployment architecture. | Accepted |
| ADR-002 | Apply inward dependency direction and Clean Architecture layer boundaries. | Accepted |
| ADR-003 | Use FastAPI as the inbound HTTP adapter and composition root. | Accepted |
| ADR-004 | Use PostgreSQL, SQLModel, and Alembic for persistence integration and schema migration. | Accepted |
| ADR-005 | Use Redis as a platform cache and coordination integration point. | Accepted |
| ADR-006 | Use structured logging and environment-driven settings. | Accepted |
| ADR-007 | Prepare cross-module integration around explicit contracts and durable domain events. | Accepted |

New records should state context, decision, consequences, status, and superseded records where applicable.
