from typing import Generator

from sqlalchemy.orm.session import Session

from .database import get_session


def db() -> Generator[Session, None, None]:
    """Yields a db session."""
    with get_session() as session:
        yield session
