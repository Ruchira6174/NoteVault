import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserRegister(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    password: str = Field(..., min_length=8, description="Strong password, min 8 characters")

class UserLogin(BaseModel):
    email_or_username: str = Field(..., description="Email or username for login")
    password: str = Field(..., description="User password")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
