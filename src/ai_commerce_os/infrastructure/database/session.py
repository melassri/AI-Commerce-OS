from collections.abc import Generator

from sqlmodel import Session, create_engine
from sqlalchemy.engine import Engine


def create_database_engine(database_url: str) -> Engine:
    """Create the synchronous SQLAlchemy engine used by SQLModel repositories."""
    return create_engine(database_url, pool_pre_ping=True)


def get_session(engine: Engine) -> Generator[Session, None, None]:
    """Yield a database session for future HTTP dependencies."""
    with Session(engine) as session:
        yield session
