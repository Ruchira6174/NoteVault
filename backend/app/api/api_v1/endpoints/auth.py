from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import UserRegister, UserLogin, TokenResponse, UserResponse
from app.services.auth_service import AuthService
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from pydantic import BaseModel

class RegisterResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

router = APIRouter()

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserRegister, db: Session = Depends(get_db)):
    """Create account and return access token + user."""
    return AuthService.register_user(db, user_in)

@router.post("/login", response_model=TokenResponse)
async def login(user_in: UserLogin, db: Session = Depends(get_db)):
    """Authenticate user with email or username + password and return JWT token."""
    return AuthService.authenticate_user(db, user_in)

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_active_user)):
    """Return authenticated user."""
    return current_user
