from collections.abc import Generator

from sqlalchemy.engine import Engine
from sqlmodel import Session, create_engine


def create_database_engine(database_url: str) -> Engine:
    """Create the synchronous SQLAlchemy engine used by SQLModel repositories."""
    return create_engine(database_url, pool_pre_ping=True)


def get_session(engine: Engine) -> Generator[Session]:
    """Yield a database session for future HTTP dependencies."""
    with Session(engine) as session:
        yield session
