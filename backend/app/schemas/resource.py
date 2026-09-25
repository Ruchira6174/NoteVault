import uuid
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from app.core.constants import Visibility, ResourceStatus
from app.schemas.profile import PublicCreatorProfile

class ResourceBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    description: Optional[str] = Field(None, max_length=5000)
    subject: Optional[str] = Field(None, max_length=255)
    university: Optional[str] = Field(None, max_length=255)
    course: Optional[str] = Field(None, max_length=100)
    branch: Optional[str] = Field(None, max_length=100)
    semester: Optional[int] = Field(None, gt=0, le=12)
    tags: Optional[List[str]] = Field(default_factory=list)
    visibility: Visibility = Field(default=Visibility.PRIVATE)
    is_paid: bool = Field(default=False)
    price: Decimal = Field(default=Decimal("0.00"), ge=0)
    currency: str = Field(default="USD", max_length=3)

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=255)
    description: Optional[str] = Field(None, max_length=5000)
    subject: Optional[str] = Field(None, max_length=255)
    university: Optional[str] = Field(None, max_length=255)
    course: Optional[str] = Field(None, max_length=100)
    branch: Optional[str] = Field(None, max_length=100)
    semester: Optional[int] = Field(None, gt=0, le=12)
    tags: Optional[List[str]] = None
    visibility: Optional[Visibility] = None
    is_paid: Optional[bool] = None
    price: Optional[Decimal] = Field(None, ge=0)
    currency: Optional[str] = Field(None, max_length=3)

class ResourceResponse(ResourceBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    average_rating: float
    downloads: int
    views: int
    status: ResourceStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ResourceCardResponse(BaseModel):
    id: uuid.UUID
    title: str
    subject: Optional[str]
    university: Optional[str]
    price: Decimal
    is_paid: bool
    average_rating: float
    preview_thumbnail: Optional[str]
    ai_score: Optional[float]
    creator: PublicCreatorProfile

    model_config = ConfigDict(from_attributes=True)

class ResourceDetailResponse(ResourceResponse):
    creator: PublicCreatorProfile
    preview_thumbnail: Optional[str]
    ai_score: Optional[float]
    # Includes detailed fields for single-resource views

    model_config = ConfigDict(from_attributes=True)
