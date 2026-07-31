from fastapi.testclient import TestClient

from ai_commerce_os.app import create_app
from ai_commerce_os.config.settings import Settings


def test_liveness_returns_ok() -> None:
    app = create_app(Settings(app_env="test"))
    with TestClient(app) as client:
        response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness_returns_ok() -> None:
    app = create_app(Settings(app_env="test"))
    with TestClient(app) as client:
        response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
