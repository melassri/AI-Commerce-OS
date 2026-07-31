from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ai_commerce_os.api.health import router as health_router
from ai_commerce_os.config.settings import Settings, get_settings
from ai_commerce_os.infrastructure.cache.client import create_redis_client
from ai_commerce_os.infrastructure.database.session import create_database_engine
from ai_commerce_os.infrastructure.observability.logging import configure_logging
from ai_commerce_os.presentation.http.middleware import request_context_middleware


def create_app(settings: Settings | None = None) -> FastAPI:
    """Build the HTTP application at the composition root."""
    active_settings = settings or get_settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        configure_logging(
            json_logs=active_settings.is_production,
            level=active_settings.app_log_level,
        )
        app.state.settings = active_settings
        app.state.db_engine = create_database_engine(active_settings.database_url)
        app.state.redis = create_redis_client(active_settings.redis_url)
        structlog.get_logger(__name__).info("application_started", environment=active_settings.app_env)
        yield
        app.state.redis.close()
        app.state.db_engine.dispose()
        structlog.get_logger(__name__).info("application_stopped")

    app = FastAPI(
        title=active_settings.app_name,
        debug=active_settings.app_debug,
        version="0.1.0",
        lifespan=lifespan,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=active_settings.app_cors_origins,
        allow_credentials=bool(active_settings.app_cors_origins),
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.middleware("http")(request_context_middleware)
    app.include_router(health_router)
    return app
