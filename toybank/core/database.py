from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


engine = create_engine("sqlite:///toybank.db?check_same_thread=false")


@contextmanager
def get_session() -> Session:
    """
    Yields a DB session on given datasource.
    On exception, rollbacks session.
    On success, commits and closes session.
    """
    maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = maker()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
