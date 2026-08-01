import uvicorn
from fastapi import FastAPI

from ai_commerce_os.app import create_app
from ai_commerce_os.config.settings import get_settings


def get_app() -> FastAPI:
    """Create the ASGI application."""
    return create_app()


app = get_app()


def run() -> None:
    """Run the production ASGI server through the installed console script."""
    settings = get_settings()
    uvicorn.run(app, host=settings.app_host, port=settings.app_port)
