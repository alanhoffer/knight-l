"""User model for authentication."""

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.utils import _utc_now


class User(Base):
    """User table - authentication and profile."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=_utc_now)
    last_login = Column(DateTime, nullable=True)

    characters = relationship("Character", back_populates="user")
