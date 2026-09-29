from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.database import get_db
from app.schemas.auth import (
    UserRegister,
    TokenResponse,
    UserResponse,
)
from app.services.auth_service import AuthService
from app.dependencies.auth import get_current_active_user
from app.models.user import User


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


router = APIRouter()


# ---------------- Register ----------------

@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user_in: UserRegister,
    db: Session = Depends(get_db),
):
    return AuthService.register_user(db, user_in)


# ---------------- Login (OAuth2) ----------------

@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return AuthService.authenticate_user(
        db=db,
        # pyrefly: ignore [unexpected-keyword]
        email_or_username=form_data.username,
        # pyrefly: ignore [unexpected-keyword]
        password=form_data.password,
    )


# ---------------- Current User ----------------

@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: User = Depends(get_current_active_user),
):
    return current_user