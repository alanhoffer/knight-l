"""Authentication endpoints: register, login, me."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.domain.schemas.user import TokenResponse, UserLogin, UserRegister, UserResponse
from app.infrastructure.database.models.user import User
from app.infrastructure.database.session import get_db
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    data: UserRegister,
    db: Session = Depends(get_db),
) -> UserResponse:
    """Register a new user."""
    return auth_service.register_user(
        db=db,
        username=data.username,
        email=data.email,
        password=data.password,
    )


@router.post("/login", response_model=TokenResponse)
def login(
    data: UserLogin,
    db: Session = Depends(get_db),
) -> TokenResponse:
    """Login and get JWT token."""
    return auth_service.login_user(
        db=db,
        username=data.username,
        password=data.password,
    )


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)) -> UserResponse:
    """Get current authenticated user."""
    return UserResponse.from_user(current_user)
