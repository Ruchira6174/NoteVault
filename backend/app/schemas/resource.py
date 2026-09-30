import uuid
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from app.core.constants import Visibility, ResourceStatus

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
    visibility: Optional[Visibility] = None
    price: Optional[Decimal] = Field(None, ge=0)
    tags: Optional[List[str]] = None

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

class PublishRequest(BaseModel):
    publish: bool
