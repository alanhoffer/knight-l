"""Database session management."""

from sqlalchemy.orm import Session, sessionmaker

from app.infrastructure.database.base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """Dependency for database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
