# Architecture

AI-Commerce-OS is a modular monolith prepared for bounded contexts and asynchronous integration.

Dependency direction is `presentation -> application -> domain`; infrastructure implements interfaces defined inward. A module must not import another module's internals. Cross-context communication should use explicit contracts and domain events, with a transactional outbox when persistence is introduced.

`src/ai_commerce_os` is the composition root only. Place future business capabilities in `modules/<bounded-context>/` using `domain/`, `application/`, `infrastructure/`, and `presentation/` subpackages. Put carefully governed shared primitives in `packages/shared` or `packages/core`.
