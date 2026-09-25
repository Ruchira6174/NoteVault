import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class ProfileBase(BaseModel):
    full_name: Optional[str] = Field(None, max_length=255)
    profile_photo: Optional[str] = Field(None, description="URL of the profile photo")
    bio: Optional[str] = Field(None, max_length=1000)
    college: Optional[str] = Field(None, max_length=255)
    university: Optional[str] = Field(None, max_length=255)
    course: Optional[str] = Field(None, max_length=100)
    branch: Optional[str] = Field(None, max_length=100)
    semester: Optional[int] = Field(None, ge=1, le=12)
    joined_year: Optional[int] = Field(None, ge=1900, le=2100)

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: uuid.UUID
    user_id: uuid.UUID
    average_rating: float
    total_resources: int
    total_sales: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PublicCreatorProfile(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    full_name: Optional[str]
    profile_photo: Optional[str]
    bio: Optional[str]
    college: Optional[str]
    university: Optional[str]
    course: Optional[str]
    branch: Optional[str]
    average_rating: float
    total_resources: int

    model_config = ConfigDict(from_attributes=True)
