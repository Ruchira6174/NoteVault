import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class ReviewBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=2000)

class ReviewCreate(ReviewBase):
    resource_id: uuid.UUID

class ReviewUpdate(BaseModel):
    rating: Optional[int] = Field(None, ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=2000)

class ReviewResponse(ReviewBase):
    id: uuid.UUID
    resource_id: uuid.UUID
    reviewer_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
