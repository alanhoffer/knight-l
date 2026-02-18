"""Authentication service: register, login, token validation."""

from datetime import timedelta

from sqlalchemy.orm import Session

from app.config import settings

from app.domain.schemas.user import TokenResponse, UserResponse
from app.infrastructure.database.models.user import User
from app.utils.exceptions import ValidationException
from app.utils.security import create_access_token, hash_password, verify_password


def register_user(db: Session, username: str, email: str, password: str) -> UserResponse:
    """Register a new user. Raises ValidationException if username or email exists."""
    if db.query(User).filter(User.username == username).first():
        raise ValidationException("Username already registered")

    if db.query(User).filter(User.email == email).first():
        raise ValidationException("Email already registered")

    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserResponse.from_user(user)


def login_user(db: Session, username: str, password: str) -> TokenResponse:
    """Authenticate user and return JWT token. Raises ValidationException if invalid."""
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise ValidationException("Invalid username or password")

    expires_delta = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": str(user.id), "username": user.username},
        expires_delta=expires_delta,
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        expires_in=settings.access_token_expire_minutes * 60,
    )
