from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.core.database import get_db
from app.dependencies.auth import get_current_active_user
from app.models.user import User
from app.schemas.resource import ResourceCreate, ResourceUpdate, ResourceResponse
from app.services.resource_service import ResourceService
from pydantic import BaseModel

router = APIRouter()

class PublishRequest(BaseModel):
    publish: bool

@router.post("", response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
async def create_resource(
    resource_in: ResourceCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create new resource metadata."""
    return ResourceService.create_resource(db, current_user.id, resource_in)

@router.get("/me", response_model=List[ResourceResponse])
async def get_my_resources(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Return my library."""
    return ResourceService.get_my_resources(db, current_user.id)

@router.get("/{resource_id}", response_model=ResourceResponse)
async def get_resource(
    resource_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Owner can access complete resource."""
    return ResourceService.get_resource_by_id(db, resource_id, current_user.id)

@router.patch("/{resource_id}", response_model=ResourceResponse)
async def update_resource(
    resource_id: UUID,
    resource_in: ResourceUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update title, description, visibility, price, tags."""
    return ResourceService.update_resource(db, resource_id, current_user.id, resource_in)

@router.delete("/{resource_id}")
async def delete_resource(
    resource_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Soft delete resource."""
    return ResourceService.delete_resource(db, resource_id, current_user.id)

@router.patch("/{resource_id}/publish", response_model=ResourceResponse)
async def publish_resource(
    resource_id: UUID,
    request: PublishRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Publish or unpublish listing."""
    return ResourceService.publish_resource(db, resource_id, current_user.id, request.publish)
