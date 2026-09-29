import uuid
from typing import Optional
from datetime import datetime

# pyrefly: ignore [missing-import]
from pydantic import BaseModel, EmailStr, Field, ConfigDict


# ---------- Register ----------

class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

    college: str = Field(..., max_length=150)
    branch: str = Field(..., max_length=100)
    semester: int = Field(..., ge=1, le=8)

    bio: Optional[str] = None


# ---------- Login ----------

class UserLogin(BaseModel):
    email_or_username: str
    password: str


# ---------- Token ----------

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- User Response ----------

class UserResponse(BaseModel):
    id: uuid.UUID
    full_name: str
    username: str
    email: EmailStr

    college: str
    branch: str
    semester: int
    bio: Optional[str]

    is_verified: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ---------- Register Response ----------

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse